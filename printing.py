from PySide6 import QtPrintSupport, QtGui
from reportlab.lib.units import cm
from reportlab.platypus import Paragraph
from datetime import datetime

from PySide6.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog

class Printing:
    def __init__(self):
        self.PDFFile = None

    def create_pages(self, co, is_lawyer, client, reference, company, company_type):
        # paragraphe = Paragraph("""
        # Bonjour,
        # Je m'appelle JP HOUBION,         Bien à vous.
        # """)
        # paragraphe.wrapOn(self.PDFFile, 100, 100)
        # paragraphe.drawOn(self.PDFFile, 100,100)
        now = datetime.now()
        address = co.split('\n')
        print(address)
        self.PDFFile.setFont("Helvetica", 10)
        self.PDFFile
        self.PDFFile.drawRightString(19 * cm, 27 * cm, f'Anhée, le {now.strftime("%d/%m/%Y")}')
        self.PDFFile.drawString(12 * cm, 25.5 * cm, f"{client}")
        if "CPAS" in address[0]:
            self.PDFFile.drawString(12 * cm, 25 * cm, f"{address[0]}")
        elif is_lawyer == 1:
            self.PDFFile.drawString(12 * cm,25 * cm, f"C/O MAITRE {address[0]}")
        else:
            self.PDFFile.drawString(12 * cm, 25 * cm, f"{address[0]}")
        self.PDFFile.drawString(12 * cm, 24.5 * cm, address[1])
        self.PDFFile.drawString(12 * cm, 24 * cm, address[2])
        self.PDFFile.drawString(13.5 * cm, 24 * cm, address[3])
        self.PDFFile.line(2 * cm, 20.5 * cm, 19 * cm, 20.5 * cm)
        self.PDFFile.line(2 * cm, 22.3 * cm, 19 * cm, 22.3 * cm)
        self.PDFFile.drawString(2 * cm, 21.5 * cm, f"Concerne : {client}")
        self.PDFFile.drawString(2 * cm, 21 * cm, f"Référence : {reference}")
        civilite_femme = ['MME', 'MADAME']
        civilite_homme = ['MR', 'MONSIEUR']
        civilite = ""
        print(address[0])
        if any(civilite in address[0] for civilite in civilite_femme):
            civilite = "Chère Madame,"
        elif any(civilite in address[0] for civilite in civilite_homme):
            civilite = "Cher Monsieur,"
        elif is_lawyer == 1:
            civilite = "Cher Maître,"
        else:
            civilite = "Chère Madame, Monsieur,"

        main_text_bloc = Paragraph(f""" {civilite}<BR/><BR/>
        Nous nous permettons de vous adresser en annexe la (les) facture(s) concernant votre administré(e).<BR/>
        Nous vous remercions pour votre intervention dans ce dossier.<BR/><BR/>

        Nous restons à votre disposition via le <B>0493/112.112</B> ou via <B>comptaclient@lcmobility.be</B> pour toutes demandes complémentaires.<BR/><BR/>      

        Nous vous prions d'agréer, {civilite} l'expression de nos sincères salutations.<BR/>
        """)
        main_text_bloc.wrapOn(self.PDFFile, 500,500)
        main_text_bloc.drawOn(self.PDFFile, 2 * cm, 14 * cm)

        signature_bloc = Paragraph(f"{company} {company_type}<BR/>Le service comptabilité.")
        signature_bloc.wrapOn(self.PDFFile, 200, 200)
        signature_bloc.drawOn(self.PDFFile, 15 * cm, 4 * cm)

        self.PDFFile.showPage() # Close the page, the next mail will be on another page
