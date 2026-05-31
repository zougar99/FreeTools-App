#!/usr/bin/env python3
import os

try:
    import qrcode
    from qrcode.image.pil import PilImage
    HAS_QR = True
except ImportError:
    HAS_QR = False

try:
    from PIL import Image
    HAS_PIL = True
except ImportError:
    HAS_PIL = False


def generate_qr(data, filename="qrcode.png"):
    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    return filename


def generate_qr_text(data):
    qr = qrcode.QRCode(box_size=1, border=1)
    qr.add_data(data)
    qr.make(fit=True)
    return qr.text_matrix()


def main():
    print("=" * 50)
    print("     QR CODE GENERATOR")
    print("=" * 50)

    if not HAS_QR:
        print("\nQR code library not installed.")
        print("Install with: pip install qrcode[pil]")
        input("\nPress Enter to exit...")
        return

    data = input("\nEnter text or URL to encode: ")
    if not data:
        print("No data provided!")
        input("Press Enter to exit...")
        return

    print("\nOutput options:")
    print("1. Save as PNG image")
    print("2. Show in terminal (text-based)")

    choice = input("\nSelect (1-2): ")

    if choice == "1":
        filename = input("Filename (default qrcode.png): ") or "qrcode.png"
        result = generate_qr(data, filename)
        print(f"\nQR Code saved as: {result}")
        if HAS_PIL:
            try:
                img = Image.open(result)
                img.show()
            except Exception:
                pass
    elif choice == "2":
        matrix = generate_qr_text(data)
        for row in matrix:
            line = "".join("██" if c else "  " for c in row)
            print(line)
    else:
        print("Invalid option!")

    input("\nPress Enter to exit...")


if __name__ == "__main__":
    main()
