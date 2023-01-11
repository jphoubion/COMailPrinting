from reportlab.lib.units import cm
from datetime import datetime

class Printing:
    def __init__(self):
        self.PDFFile = None

    def create_pages(self, co, client, reference, company):
        now = datetime.now()
        address = co.split('\n')
        self.PDFFile.drawRightString(19 * cm, 28 * cm, f'Anhée, le {now.strftime("%d/%m/%Y")}')
        self.PDFFile.drawString(13 * cm,26 * cm, address[0])
        self.PDFFile.drawString(13 * cm, 25.5 * cm, address[1])
        self.PDFFile.drawString(13 * cm, 25 * cm, address[2])
        self.PDFFile.line(2 * cm, 21.5 * cm, 19 * cm, 21.5 * cm)
        self.PDFFile.line(2 * cm, 23.3 * cm, 19 * cm, 23.3 * cm)
        self.PDFFile.drawString(2 * cm, 22.5 * cm, f"Client : {client}")
        self.PDFFile.drawString(2 * cm, 22 * cm, f"Référence : {reference}")
        self.PDFFile.drawString(15 * cm, 4 * cm, company)
        self.PDFFile.showPage() # Close the page, the next mail will be on another page
