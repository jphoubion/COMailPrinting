from reportlab.lib.units import cm
from datetime import datetime

class Printing:
    def __init__(self):
        self.PDFFile = None

    def create_pages(self, co, is_lawyer, client, reference, company, company_type):
        now = datetime.now()
        address = co.split('\n')
        print(address)
        self.PDFFile.setFont("Helvetica", 10)
        self.PDFFile.drawRightString(19 * cm, 27 * cm, f'Anhée, le {now.strftime("%d/%m/%Y")}')
        self.PDFFile.drawString(12 * cm, 25.5 * cm, f"{client}")
        if "CPAS" in address[0]:
            self.PDFFile.drawString(12 * cm, 25 * cm, f"{address[0]}")
        elif is_lawyer == 1:
            self.PDFFile.drawString(12 * cm,25 * cm, f"MAITRE {address[0]}")
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
        print(address[0])
        if any(civilite in address[0] for civilite in civilite_femme):
            self.PDFFile.drawString(2 * cm, 17 * cm, f"Madame,")
        elif any(civilite in address[0] for civilite in civilite_homme):
            self.PDFFile.drawString(2 * cm, 17 * cm, f"Monsieur,")
        elif is_lawyer == 1:
            self.PDFFile.drawString(2 * cm, 17 * cm, f"Maître,")
        else:
            self.PDFFile.drawString(2 * cm, 17 * cm, f"Madame, Monsieur,")
        self.PDFFile.drawString(2 * cm, 16 * cm, f"Nous nous permettons de vous adresser en annexe la (les) facture(s) concernant votre administré(e).")
        self.PDFFile.drawString(2 * cm, 15.5 * cm, f"Nous vous remercions pour votre intervention dans ce dossier.")
        self.PDFFile.drawString(2 * cm, 14 * cm, f"Nous restons à votre disposition via le 0493/112.112 ou via comptaclient@lcmobility.be pour toutes ")
        self.PDFFile.drawString(2 * cm, 13.5 * cm, f"demandes complémentaires.")
        self.PDFFile.drawString(2 * cm, 13 * cm, f"Nous vous prions d'agréer, cher Maître, l'expression de nos sincères salutations.")
        self.PDFFile.drawString(15 * cm, 4 * cm, company)
        self.PDFFile.drawString(17.5 * cm, 4 * cm, company_type)
        self.PDFFile.drawString(15 * cm, 3.5 * cm, "Le service comptabilité.")
        self.PDFFile.showPage() # Close the page, the next mail will be on another page

