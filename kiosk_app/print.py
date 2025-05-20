# printer_app/script.py
from escpos.printer import Win32Raw
import qrcode
from PIL import Image
import random
import string

def generate_and_print_qr(data):
    printer_name = "POS58 Printer"  # Adjust to your actual printer name

    # Generate QR code
    qr = qrcode.make(data)
    qr.save("qr_code.png")

    # Print QR code
    printer = Win32Raw(printer_name)
    printer.image("qr_code.png")
    printer.text("\n")
    printer.cut()
