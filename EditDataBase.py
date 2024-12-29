import sqlite3

from PyQt6.QtWidgets import QMainWindow

from addEditCoffeeForm import Ui_MainWindow


class EditDatabase(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None, item=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Редактирование БД")
        self.item = item
        self.con = sqlite3.connect('data/coffee.sqlite')

        self.cur = self.con.cursor()
        if self.item:
            current_text = self.cur.execute(f"""SELECT * FROM coffee WHERE grade == ?""", (self.item,)).fetchall()
            self.id = current_text[0][0]
            self.gradeLineEdit.setText(current_text[0][1])
            self.roastingLineEdit.setText(current_text[0][2])
            self.typeLineEdit.setText(current_text[0][3])
            self.tasteLineEdit.setText(current_text[0][4])
            self.priceLineEdit.setText(str(current_text[0][5]))
            self.weightLineEdit.setText(str(current_text[0][6]))
        self.pushButton.clicked.connect(self.save_changes)

    def save_changes(self):
        if self.get_verdict():
            self.parent().load_table()
            self.close()

    def get_verdict(self):
        try:
            if not self.item:
                self.cur.execute(
                    """INSERT INTO coffee(grade, roasting, type, taste, price, weight) VALUES (?,?,?,?,?,?)""",
                    [self.gradeLineEdit.text(), self.roastingLineEdit.text(), self.typeLineEdit.text(),
                     self.tasteLineEdit.text(), float(self.priceLineEdit.text()), int(self.weightLineEdit.text())])
            else:
                self.cur.execute(
                    """UPDATE coffee SET grade = ?, roasting = ?, type = ?, taste = ?, price = ?, weight = ? WHERE id = ?""",
                    (self.gradeLineEdit.text(), self.roastingLineEdit.text(), self.typeLineEdit.text(),
                     self.tasteLineEdit.text(), float(self.priceLineEdit.text()), int(self.weightLineEdit.text()),
                     int(self.id)))
            self.con.commit()
            return True
        except Exception as ex:
            print(ex)
            return False
