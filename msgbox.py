from PySide6.QtWidgets import QMessageBox


def display_msgbox(title, boxtype, msg, button):
    dialog = QMessageBox()
    dialog.setIcon(boxtype)
    dialog.setWindowTitle(title)
    dialog.setText(msg)
    dialog.setStandardButtons(button)
    dialog.exec()
