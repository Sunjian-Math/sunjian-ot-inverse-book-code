# QR Code Instructions

Generate a QR code for the repository URL with:

```bash
python tools/make_qr.py
```

You may also pass a custom URL explicitly:

```bash
python tools/make_qr.py https://github.com/Sunjian-Math/sunjian-ot-inverse-book-code
```

The script writes:

```text
docs/assets/book_companion_code_qr.png
figures/qrcode/book_companion_code_qr.pdf
```

Use the PNG file for GitHub preview pages and the PDF file for the book manuscript or print production.
