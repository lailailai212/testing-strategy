"""Convert PDF to high-DPI PNG; crop whitespace on specified pages."""
import sys
from pathlib import Path

import fitz
import numpy as np
from PIL import Image


def crop_whitespace(
    img: Image.Image,
    threshold: int = 245,
    margin: int = 10,
    min_row_pixels: int = 30,
    min_col_pixels: int = 30,
) -> Image.Image:
    """Crop margins and large internal blank bands (e.g. empty PDF page tail)."""
    arr = np.array(img)
    if arr.ndim == 3:
        mask = np.any(arr < threshold, axis=2)
    else:
        mask = arr < threshold
    if not mask.any():
        return img

    row_counts = mask.sum(axis=1)
    col_counts = mask.sum(axis=0)
    content_rows = np.where(row_counts >= min_row_pixels)[0]
    content_cols = np.where(col_counts >= min_col_pixels)[0]
    if len(content_rows) == 0 or len(content_cols) == 0:
        return img

    y_min, y_max = content_rows[0], content_rows[-1]
    x_min, x_max = content_cols[0], content_cols[-1]
    y_min = max(0, y_min - margin)
    x_min = max(0, x_min - margin)
    y_max = min(arr.shape[0] - 1, y_max + margin)
    x_max = min(arr.shape[1] - 1, x_max + margin)
    return img.crop((x_min, y_min, x_max + 1, y_max + 1))


def convert(pdf_path: Path, dpi: int = 300, crop_pages: set[int] | None = None) -> Path:
    out_dir = pdf_path.parent / f"{pdf_path.stem}_png"
    out_dir.mkdir(exist_ok=True)
    zoom = dpi / 72
    mat = fitz.Matrix(zoom, zoom)
    crop_pages = crop_pages or set()

    doc = fitz.open(pdf_path)
    stem = pdf_path.stem
    for i, page in enumerate(doc, start=1):
        pix = page.get_pixmap(matrix=mat, alpha=False)
        img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
        out_file = out_dir / f"{stem}_page{i:02d}.png"
        if i in crop_pages:
            img = crop_whitespace(img)
        img.save(str(out_file), "PNG", optimize=True)
        print(f"Page {i}: {out_file.name} {img.width}x{img.height} ({out_file.stat().st_size // 1024} KB)")
    doc.close()
    print(f"Output: {out_dir}")
    return out_dir


if __name__ == "__main__":
    pdf = Path(sys.argv[1])
    crop = {int(x) for x in sys.argv[2].split(",")} if len(sys.argv) > 2 else set()
    convert(pdf, crop_pages=crop)
