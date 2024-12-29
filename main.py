import sqlite3
import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

from EditDataBase import EditDatabase
from mainWindow import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    window = ""

    def __init__(self):
        super().__init__()
        self.setupUi(self)
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
        con = sqlite3.connect('data/coffee.sqlite')
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
