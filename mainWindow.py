# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(710, 320)
        MainWindow.setMinimumSize(QtCore.QSize(640, 320))
        MainWindow.setMaximumSize(QtCore.QSize(800, 320))
        self.centralWidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.editPushButton = QtWidgets.QPushButton(parent=self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.editPushButton.setFont(font)
        self.editPushButton.setObjectName("editPushButton")
        self.gridLayout.addWidget(self.editPushButton, 3, 1, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 4, 0, 1, 2)
        self.label = QtWidgets.QLabel(parent=self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)
        self.addPushButton = QtWidgets.QPushButton(parent=self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.addPushButton.setFont(font)
        self.addPushButton.setObjectName("addPushButton")
        self.gridLayout.addWidget(self.addPushButton, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 710, 26))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(parent=MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.editPushButton.setText(_translate("MainWindow", "изменить запись"))
        self.label.setText(_translate("MainWindow", "Информация о кофе"))
        self.addPushButton.setText(_translate("MainWindow", "добавить запись"))
