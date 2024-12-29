import sqlite3
import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class EditDatabase(QMainWindow):
    def __init__(self, parent=None, item=None):
        super().__init__(parent)
        uic.loadUi("addEditCoffeeForm.ui", self)
        self.setWindowTitle("Редактирование БД")
        self.item = item
        self.con = sqlite3.connect('coffee.sqlite')

        self.cur = self.con.cursor()
        if self.item:
            current_text = self.cur.execute(f"""SELECT * FROM coffee WHERE grade == ?""", (self.item,)).fetchall()
            print(current_text)
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


class MyWidget(QMainWindow):
    window = ""

    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.editPushButton.clicked.connect(self.add_info)
        self.addPushButton.clicked.connect(self.add_info)
        self.setWindowTitle('Кофе')
        self.load_table()

    def add_info(self):
        selected_row = self.tableWidget.currentRow()
        if self.sender().text() == "изменить запись" and selected_row != -1:
            item = self.tableWidget.item(selected_row, 0).text()
            self.window = EditDatabase(self, item=item)
        else:
            self.window = EditDatabase(self)
        self.window.show()

    def load_table(self):
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        data = cur.execute(f"""SELECT * FROM coffee""").fetchall()
        self.tableWidget.setColumnCount(len(data[0]) - 1)
        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setHorizontalHeaderLabels(
            ["название сорта", "степень обжарки", "молотый/в зернах", "описание вкуса", "цена", "объем упаковки"])
        for i, elem in enumerate(data):
            for j, val in enumerate(elem[1:]):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        self.tableWidget.resizeColumnsToContents()
        con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
