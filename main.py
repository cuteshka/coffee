import sqlite3
import sys


from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class MyWidget(QMainWindow):
    def __init__(self):
        super(MyWidget, self).__init__()
        uic.loadUi("main.ui", self)
        self.table()

    def table(self) -> None:
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
