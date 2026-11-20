"""Crop figure illustrations out of the source PDF.

Usage:
    python scripts/crop_figures.py <path-to-original-book.pdf> <manifest.json> <out-dir>

The manifest is a JSON list of ``{"page": <0-based page index>, "key": "fig-X-Y",
"caption": "Fig. X.Y: ..."}`` entries (see figures_manifest.json produced during the
initial extraction pass).

This script locates, for each figure, the caption's top edge (``cap_top``) and the
bottom edge of the paragraph that precedes the figure (``region_top``), then unions
the drawing/image rects that plausibly belong to the figure itself (filtering out
degenerate page-spanning bezier bounding boxes). The final crop's top edge is
``max(union.y0 - pad, region_top)`` -- this clamp is the important part: it must
never let the crop extend above ``region_top``, or the image will bleed into the
last line of the preceding paragraph. A previous version of this script applied the
padding *after* clamping, which allowed exactly that bleed-in on ~half of the
figures (e.g. fig-2-1, fig-4-2).
"""
import json
import os
import re
import sys

import fitz

PAD = 6.0
BOTTOM_GAP = 4.0
PAGE_NUM_RE = re.compile(r"^\s*\d{1,3}\s*$")


def is_degenerate(rect, page_rect):
    """Filter out bogus bezier-curve bboxes with huge extents outside the page."""
    if rect.y0 < -50 or rect.y1 > page_rect.height + 50:
        return True
    if rect.height <= 0 or rect.width <= 0:
        return True
    if rect.height > page_rect.height * 1.2:
        return True
    return False


def crop_figure(doc, item):
    page = doc[item["page"]]
    page_rect = page.rect
    old_rect = fitz.Rect(*item["rect"]) if "rect" in item else None

    first_line = item["caption"].split("\n")[0][:30]
    cap_top = None
    for inst in page.search_for(first_line):
        cap_top = inst.y0
        break
    if cap_top is None and old_rect is not None:
        cap_top = old_rect.y1 + BOTTOM_GAP

    blocks = []
    for b in page.get_text("blocks"):
        text = b[4].strip()
        if not text or PAGE_NUM_RE.match(text):
            continue
        if text.startswith(first_line[:15]):
            continue
        blocks.append(b)
    blocks.sort(key=lambda b: b[1])

    region_top = None
    for b in blocks:
        b_y1 = b[3]
        if b_y1 <= cap_top - 1 and (region_top is None or b_y1 > region_top):
            region_top = b_y1

    candidate_rects = []
    for dr in page.get_drawings():
        r = dr["rect"]
        if is_degenerate(r, page_rect):
            continue
        if r.y1 > cap_top + 1:
            continue
        if region_top is not None and r.y1 <= region_top + 0.5:
            continue
        candidate_rects.append(r)
    for info in page.get_image_info():
        r = fitz.Rect(info["bbox"])
        if is_degenerate(r, page_rect):
            continue
        if r.y1 > cap_top + 1:
            continue
        if region_top is not None and r.y1 <= region_top + 0.5:
            continue
        candidate_rects.append(r)

    if candidate_rects:
        union = candidate_rects[0]
        for r in candidate_rects[1:]:
            union = union | r
    elif old_rect is not None:
        union = fitz.Rect(old_rect.x0, old_rect.y0 + PAD, old_rect.x1, old_rect.y1)
    else:
        raise ValueError(f"no drawings/images found for {item['key']}")

    final_top = max(union.y0 - PAD, region_top) if region_top is not None else union.y0 - PAD
    x0 = old_rect.x0 if old_rect is not None else union.x0
    x1 = old_rect.x1 if old_rect is not None else union.x1
    return fitz.Rect(x0, final_top, x1, cap_top - BOTTOM_GAP)


def main():
    pdf_path, manifest_path, out_dir = sys.argv[1], sys.argv[2], sys.argv[3]
    os.makedirs(out_dir, exist_ok=True)

    doc = fitz.open(pdf_path)
    manifest = json.load(open(manifest_path, encoding="utf-8"))

    for item in manifest:
        page = doc[item["page"]]
        rect = crop_figure(doc, item)
        pix = page.get_pixmap(matrix=fitz.Matrix(3, 3), clip=rect)
        pix.save(os.path.join(out_dir, f"{item['key']}.png"))
        print(f"{item['key']}: {rect}")


if __name__ == "__main__":
    main()
