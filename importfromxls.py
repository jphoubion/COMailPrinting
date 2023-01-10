import json

from PySide6.QtWidgets import QFileDialog
from openpyxl import Workbook, load_workbook

class ImportFromXls:

    def __init__(self):

        self.wb = Workbook()
        self.sheet = None

    def select_customers_file(self):
        dlg = QFileDialog(filter="*.xlsx;;*.xls")
        dlg.setWindowTitle("Selectionner le fichier des clients")
        dlg.setFileMode(QFileDialog.ExistingFile)
        dlg.setViewMode(QFileDialog.Detail)
        if dlg.exec():
            self.filename = dlg.selectedFiles()
            self.wb = load_workbook(self.filename[0])
            return self.wb.active

    def import_customers(self):
        self.sheet = self.select_customers_file()
        customer_dict = {}
        if self.sheet is not None:
            with open("customers.json", "w") as outfile:
                for row in self.sheet.iter_rows(min_row=2):
                    # building DIC to export to JSON
                    # cleaning C/O information
                    co = str(row[3].value).split(' ')[2:]
                    # co_name = f"{co[-2]} {co[-1]}".upper().replace("C/O ME ",'').replace("C/O ME. ",'')
                    # co_name = f"{co}".upper().replace("C/O ME ", '').replace("C/O ME. ", '')
                    customer_dict.update({
                        row[0].value: {
                            "name": row[2].value,
                            "co": ' '.join(co).upper()
                        }
                    })
                # print(customer_dict)
                json_object = json.dumps(customer_dict, indent=4)

                # Writing to sample.json
                outfile.write(json_object)

                self.import_co()

    def import_co(self):
        if self.sheet is not None:
            co_dict = {}
            with open("co.json", "w") as outfile:
                for row in self.sheet.iter_rows(min_row=2):
                    co_name = str(row[3].value).upper().replace("C/O ME ",'').replace("C/O ME. ",'')
                    co_dict.update({
                        co_name: {
                            "co_name": co_name,
                            "address" : row[6].value,
                            "cp" : row[8].value,
                            "city" : row[9].value
                        }
                    })
                # print(customer_dict)
                json_object = json.dumps(co_dict, indent=4)

                # Writing to sample.json
                outfile.write(json_object)