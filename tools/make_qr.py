from pathlib import Path
import sys

import qrcode
import PIL.JpegImagePlugin  # noqa: F401; registers JPEG support for Pillow PDF output.


REPOSITORY_URL = "https://github.com/Sunjian-Math/sunjian-ot-inverse-book-code"


def make_qr_code(url: str = REPOSITORY_URL) -> None:
    """Generate QR code images for the companion code repository."""

    repo_root = Path(__file__).resolve().parents[1]

    png_path = repo_root / "docs" / "assets" / "book_companion_code_qr.png"
    pdf_path = repo_root / "figures" / "qrcode" / "book_companion_code_qr.pdf"

    png_path.parent.mkdir(parents=True, exist_ok=True)
    pdf_path.parent.mkdir(parents=True, exist_ok=True)

    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=12,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    qr_image = qr.make_image(fill_color="black", back_color="white").convert("RGB")
    qr_image.save(png_path)
    qr_image.save(pdf_path, resolution=600.0)

    print(f"Repository URL: {url}")
    print(f"PNG saved to: {png_path}")
    print(f"PDF saved to: {pdf_path}")


if __name__ == "__main__":
    url_arg = sys.argv[1] if len(sys.argv) > 1 else REPOSITORY_URL
    make_qr_code(url_arg)
