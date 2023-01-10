import sys
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from datetime import datetime

class Printing:
    def __init__(self):
        self.PDFFile = None

    def create_pages(self, filename, co, client, reference, company):
        file = filename + ".pdf"
        self.PDFFile = Canvas(file, pagesize=A4)
        self.PDFFile.setFont("Helvetica", 12)
        now = datetime.now()
        print("Current date and time : ")
        print(now.strftime("%Y-%m-%d %H:%M:%S"))
        self.PDFFile.drawRightString(19 * cm,27.5 * cm, co)
        self.PDFFile.drawRightString(19 * cm, 25.5 * cm, client)
        self.PDFFile.drawRightString(19 * cm, 23.5 * cm, reference)
        self.PDFFile.drawRightString(19 * cm, 21.5 * cm, company)

        self.PDFFile.save()

