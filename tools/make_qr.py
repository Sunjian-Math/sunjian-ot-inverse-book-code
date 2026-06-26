import sys
from pathlib import Path

import qrcode


def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python tools/make_qr.py <repository_url>")

    url = sys.argv[1]
    out_dir = Path("docs/assets")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "book_companion_code_qr.png"

    img = qrcode.make(url)
    img.save(out_path)
    print(out_path)


if __name__ == "__main__":
    main()
