# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HomeUserInactivarEliminar.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
import psycopg2 as bd
#import pgdb as bd
from config import config

class Ui_HomeUserInactivarEliminar(object):
    def __init__(self, id):
        super(Ui_HomeUserInactivarEliminar, self).__init__()
        self.id = id

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 650)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 650))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 650))
        MainWindow.setStyleSheet("background-color: rgb(72,35,60);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(50, 50, 900, 550))
        self.frame.setMinimumSize(QtCore.QSize(900, 550))
        self.frame.setMaximumSize(QtCore.QSize(900, 550))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:12px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(130, 50, 205, 50))
        self.label.setMinimumSize(QtCore.QSize(205, 50))
        self.label.setMaximumSize(QtCore.QSize(205, 50))
        self.label.setStyleSheet("font: 24pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 100, 100))
        self.label_2.setMinimumSize(QtCore.QSize(100, 100))
        self.label_2.setMaximumSize(QtCore.QSize(100, 100))
        self.label_2.setStyleSheet("")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("logo.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_2.setObjectName("label_2")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(609, 130, 230, 50))
        self.label_7.setMinimumSize(QtCore.QSize(220, 50))
        self.label_7.setMaximumSize(QtCore.QSize(230, 25))
        self.label_7.setStyleSheet("font: 19pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label_7.setObjectName("label_7")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(609, 230, 262, 231))
        self.tableWidget.setMinimumSize(QtCore.QSize(262, 231))
        self.tableWidget.setMaximumSize(QtCore.QSize(262, 231))
        self.tableWidget.setStyleSheet("font: 13pt \"Times\";\n"
"color: rgb(64, 55, 110);\n"
"background-color: rgb(212, 228, 188);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
#         self.pushButton_Login = QtWidgets.QPushButton(self.frame)
#         self.pushButton_Login.setGeometry(QtCore.QRect(756, 50, 114, 32))
#         self.pushButton_Login.setMinimumSize(QtCore.QSize(114, 32))
#         self.pushButton_Login.setMaximumSize(QtCore.QSize(114, 32))
#         self.pushButton_Login.setStyleSheet("background-color: rgb(10, 54, 157);\n"
# "font: 14pt \"Times\";\n"
# "color: rgb(255, 255, 255);\n"
# "border-radius:12px;")
#         self.pushButton_Login.setObjectName("pushButton_Login")
        self.textEdit_UserBuscar = QtWidgets.QTextEdit(self.frame)
        self.textEdit_UserBuscar.setGeometry(QtCore.QRect(640, 200, 156, 31))
        self.textEdit_UserBuscar.setMinimumSize(QtCore.QSize(156, 0))
        self.textEdit_UserBuscar.setMaximumSize(QtCore.QSize(156, 16777215))
        self.textEdit_UserBuscar.setStyleSheet("background-color: rgb(150, 172, 183);\n"
"font: 13pt \"Times\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:12px;")
        self.textEdit_UserBuscar.setObjectName("textEdit_UserBuscar")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(609, 199, 31, 31))
        self.label_4.setStyleSheet("")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("finder.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(30, 130, 280, 50))
        self.label_8.setMinimumSize(QtCore.QSize(280, 50))
        self.label_8.setMaximumSize(QtCore.QSize(210, 25))
        self.label_8.setStyleSheet("font: 19pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label_8.setObjectName("label_8")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(30, 199, 31, 31))
        self.label_5.setStyleSheet("")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("finder.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.textEdit_UserBuscar_2 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_UserBuscar_2.setGeometry(QtCore.QRect(61, 200, 156, 31))
        self.textEdit_UserBuscar_2.setMinimumSize(QtCore.QSize(156, 0))
        self.textEdit_UserBuscar_2.setMaximumSize(QtCore.QSize(156, 16777215))
        self.textEdit_UserBuscar_2.setStyleSheet("background-color: rgb(150, 172, 183);\n"
"font: 13pt \"Times\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:12px;")
        self.textEdit_UserBuscar_2.setObjectName("textEdit_UserBuscar_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.frame)
        self.tableWidget_2.setGeometry(QtCore.QRect(30, 230, 262, 231))
        self.tableWidget_2.setMinimumSize(QtCore.QSize(262, 231))
        self.tableWidget_2.setMaximumSize(QtCore.QSize(262, 231))
        self.tableWidget_2.setStyleSheet("font: 13pt \"Times\";\n"
"color: rgb(64, 55, 110);\n"
"background-color: rgb(212, 228, 188);")
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(1)
        self.tableWidget_2.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        self.pushButton_EliminarCancion = QtWidgets.QPushButton(self.frame)
        self.pushButton_EliminarCancion.setGeometry(QtCore.QRect(30, 480, 114, 32))
        self.pushButton_EliminarCancion.setMinimumSize(QtCore.QSize(114, 32))
        self.pushButton_EliminarCancion.setMaximumSize(QtCore.QSize(114, 32))
        self.pushButton_EliminarCancion.setStyleSheet("background-color: rgb(10, 54, 157);\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:12px;")
        self.pushButton_EliminarCancion.setObjectName("pushButton_EliminarCancion")
        self.pushButton_EliminarAlbum = QtWidgets.QPushButton(self.frame)
        self.pushButton_EliminarAlbum.setGeometry(QtCore.QRect(690, 480, 114, 32))
        self.pushButton_EliminarAlbum.setMinimumSize(QtCore.QSize(114, 32))
        self.pushButton_EliminarAlbum.setMaximumSize(QtCore.QSize(114, 32))
        self.pushButton_EliminarAlbum.setStyleSheet("background-color: rgb(10, 54, 157);\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:12px;")
        self.pushButton_EliminarAlbum.setObjectName("pushButton_EliminarAlbum")
        self.pushButton_EliminarAlbum.clicked.connect(self.eliminarAlbum)
        self.pushButton_BuscarEliminarInactivarCancion = QtWidgets.QPushButton(self.frame)
        self.pushButton_BuscarEliminarInactivarCancion.setGeometry(QtCore.QRect(217, 200, 75, 31))
        self.pushButton_BuscarEliminarInactivarCancion.setMinimumSize(QtCore.QSize(75, 31))
        self.pushButton_BuscarEliminarInactivarCancion.setMaximumSize(QtCore.QSize(75, 31))
        self.pushButton_BuscarEliminarInactivarCancion.setStyleSheet("background-color: rgb(10, 54, 157);\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:12px;")
        self.pushButton_BuscarEliminarInactivarCancion.setObjectName("pushButton_BuscarEliminarInactivarCancion")
        self.pushButton_BuscarEliminarAlbum = QtWidgets.QPushButton(self.frame)
        self.pushButton_BuscarEliminarAlbum.setGeometry(QtCore.QRect(796, 200, 75, 31))
        self.pushButton_BuscarEliminarAlbum.setMinimumSize(QtCore.QSize(75, 31))
        self.pushButton_BuscarEliminarAlbum.setMaximumSize(QtCore.QSize(75, 31))
        self.pushButton_BuscarEliminarAlbum.setStyleSheet("background-color: rgb(10, 54, 157);\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:12px;")
        self.pushButton_BuscarEliminarAlbum.setObjectName("pushButton_BuscarEliminarAlbum")
        self.pushButton_BuscarEliminarInactivarCancion.clicked.connect(self.llenarTablaCanciones)
        self.pushButton_BuscarEliminarAlbum.clicked.connect(self.buscarAlbum)
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(320, 200, 31, 31))
        self.label_6.setStyleSheet("")
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("finder.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.textEdit_UserBuscar_3 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_UserBuscar_3.setGeometry(QtCore.QRect(351, 200, 156, 31))
        self.textEdit_UserBuscar_3.setMinimumSize(QtCore.QSize(156, 0))
        self.textEdit_UserBuscar_3.setMaximumSize(QtCore.QSize(156, 16777215))
        self.textEdit_UserBuscar_3.setStyleSheet("background-color: rgb(150, 172, 183);\n"
"font: 13pt \"Times\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:12px;")
        self.textEdit_UserBuscar_3.setObjectName("textEdit_UserBuscar_3")
        self.pushButton_BuscarEliminarArtista = QtWidgets.QPushButton(self.frame)
        self.pushButton_BuscarEliminarArtista.setGeometry(QtCore.QRect(507, 200, 75, 31))
        self.pushButton_BuscarEliminarArtista.setMinimumSize(QtCore.QSize(75, 31))
        self.pushButton_BuscarEliminarArtista.setMaximumSize(QtCore.QSize(75, 31))
        self.pushButton_BuscarEliminarArtista.setStyleSheet("background-color: rgb(10, 54, 157);\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:12px;")
        self.pushButton_BuscarEliminarArtista.setObjectName("pushButton_BuscarEliminarArtista")
        self.pushButton_BuscarEliminarArtista.clicked.connect(self.buscarArtista)
        self.tableWidget_3 = QtWidgets.QTableWidget(self.frame)
        self.tableWidget_3.setGeometry(QtCore.QRect(320, 230, 262, 231))
        self.tableWidget_3.setMinimumSize(QtCore.QSize(262, 231))
        self.tableWidget_3.setMaximumSize(QtCore.QSize(262, 231))
        self.tableWidget_3.setStyleSheet("font: 13pt \"Times\";\n"
"color: rgb(64, 55, 110);\n"
"background-color: rgb(212, 228, 188);")
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(1)
        self.tableWidget_3.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        self.pushButton_EliminarArtista = QtWidgets.QPushButton(self.frame)
        self.pushButton_EliminarArtista.setGeometry(QtCore.QRect(394, 480, 114, 32))
        self.pushButton_EliminarArtista.setMinimumSize(QtCore.QSize(114, 32))
        self.pushButton_EliminarArtista.setMaximumSize(QtCore.QSize(114, 32))
        self.pushButton_EliminarArtista.setStyleSheet("background-color: rgb(10, 54, 157);\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:12px;")
        self.pushButton_EliminarArtista.setObjectName("pushButton_EliminarArtista")
        self.pushButton_EliminarArtista.clicked.connect(self.eliminarArtista)
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(320, 130, 280, 50))
        self.label_9.setMinimumSize(QtCore.QSize(280, 50))
        self.label_9.setMaximumSize(QtCore.QSize(210, 25))
        self.label_9.setStyleSheet("font: 19pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label_9.setObjectName("label_9")
        self.pushButton_InactivarCancion = QtWidgets.QPushButton(self.frame)
        self.pushButton_InactivarCancion.setGeometry(QtCore.QRect(178, 480, 114, 32))
        self.pushButton_InactivarCancion.setMinimumSize(QtCore.QSize(114, 32))
        self.pushButton_InactivarCancion.setMaximumSize(QtCore.QSize(114, 32))
        self.pushButton_InactivarCancion.setStyleSheet("background-color: rgb(10, 54, 157);\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:12px;")
        self.pushButton_InactivarCancion.setObjectName("pushButton_InactivarCancion")
        self.label_8.raise_()
        self.label_7.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.tableWidget.raise_()
        # self.pushButton_Login.raise_()
        self.textEdit_UserBuscar.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.textEdit_UserBuscar_2.raise_()
        self.tableWidget_2.raise_()
        self.pushButton_EliminarCancion.raise_()
        self.pushButton_EliminarAlbum.raise_()
        self.pushButton_BuscarEliminarInactivarCancion.raise_()
        self.pushButton_BuscarEliminarAlbum.raise_()
        self.label_6.raise_()
        self.textEdit_UserBuscar_3.raise_()
        self.pushButton_BuscarEliminarArtista.raise_()
        self.tableWidget_3.raise_()
        self.pushButton_EliminarArtista.raise_()
        self.label_9.raise_()
        self.pushButton_InactivarCancion.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton_EliminarCancion.clicked.connect(self.eliminarCancion)
        self.pushButton_InactivarCancion.clicked.connect(self.inactivarCancion)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Sonido Cloud "))
        self.label_7.setText(_translate("MainWindow", "Eliminar Álbum"))
        # item = self.tableWidget.verticalHeaderItem(0)
        # item.setText(_translate("MainWindow", "aqui"))
        # item = self.tableWidget.verticalHeaderItem(1)
        # item.setText(_translate("MainWindow", "van"))
        # item = self.tableWidget.verticalHeaderItem(2)
        # item.setText(_translate("MainWindow", "New Row"))
        # item = self.tableWidget.verticalHeaderItem(3)
        # item.setText(_translate("MainWindow", "las"))
        # item = self.tableWidget.verticalHeaderItem(4)
        # item.setText(_translate("MainWindow", "filas"))
        # item = self.tableWidget.verticalHeaderItem(5)
        # item.setText(_translate("MainWindow", "proyecto"))
        # item = self.tableWidget.horizontalHeaderItem(0)
        # item.setText(_translate("MainWindow", "canciones"))
        # self.pushButton_Login.setText(_translate("MainWindow", "Salir"))
        self.textEdit_UserBuscar.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "Eliminar/Inactivar Canción"))
        self.textEdit_UserBuscar_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        # item = self.tableWidget_2.verticalHeaderItem(0)
        # item.setText(_translate("MainWindow", "aqui"))
        # item = self.tableWidget_2.verticalHeaderItem(1)
        # item.setText(_translate("MainWindow", "van"))
        # item = self.tableWidget_2.verticalHeaderItem(2)
        # item.setText(_translate("MainWindow", "New Row"))
        # item = self.tableWidget_2.verticalHeaderItem(3)
        # item.setText(_translate("MainWindow", "las"))
        # item = self.tableWidget_2.verticalHeaderItem(4)
        # item.setText(_translate("MainWindow", "filas"))
        # item = self.tableWidget_2.verticalHeaderItem(5)
        # item.setText(_translate("MainWindow", "proyecto"))
        # item = self.tableWidget_2.horizontalHeaderItem(0)
        # item.setText(_translate("MainWindow", "canciones"))
        self.pushButton_EliminarCancion.setText(_translate("MainWindow", "Eliminar"))
        self.pushButton_EliminarAlbum.setText(_translate("MainWindow", "Eliminar"))
        self.pushButton_BuscarEliminarInactivarCancion.setText(_translate("MainWindow", "Buscar"))
        self.pushButton_BuscarEliminarAlbum.setText(_translate("MainWindow", "Buscar"))
        self.textEdit_UserBuscar_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_BuscarEliminarArtista.setText(_translate("MainWindow", "Buscar"))
        # item = self.tableWidget_3.verticalHeaderItem(0)
        # item.setText(_translate("MainWindow", "aqui"))
        # item = self.tableWidget_3.verticalHeaderItem(1)
        # item.setText(_translate("MainWindow", "van"))
        # item = self.tableWidget_3.verticalHeaderItem(2)
        # item.setText(_translate("MainWindow", "New Row"))
        # item = self.tableWidget_3.verticalHeaderItem(3)
        # item.setText(_translate("MainWindow", "las"))
        # item = self.tableWidget_3.verticalHeaderItem(4)
        # item.setText(_translate("MainWindow", "filas"))
        # item = self.tableWidget_3.verticalHeaderItem(5)
        # item.setText(_translate("MainWindow", "proyecto"))
        # item = self.tableWidget_3.horizontalHeaderItem(0)
        # item.setText(_translate("MainWindow", "canciones"))
        self.pushButton_EliminarArtista.setText(_translate("MainWindow", "Eliminar"))
        self.label_9.setText(_translate("MainWindow", "Eliminar Artista"))
        self.pushButton_InactivarCancion.setText(_translate("MainWindow", "Inactivar"))

    def llenarTablaCanciones(self):
        #clear the table
        self.tableWidget_2.setRowCount(0)
        if(self.textEdit_UserBuscar_2.toPlainText() != ''):
            try:
                print('Bien')
                conn = None
                params = config()
                conn = bd.connect(**params)
                cursor = conn.cursor()
                texto = self.textEdit_UserBuscar_2.toPlainText()
                query = "SELECT track.trackid, track.name, album.title, artist.name FROM track JOIN album ON album.albumid = track.albumid JOIN artist ON album.artistid = artist.artistid WHERE UPPER(track.name) LIKE UPPER(\'%" + \
                    texto+"%\') AND track.isactive = \'t\'"
                cursor.execute(query)
                record = cursor.fetchall()
                if(len(record) != 0 and len(record[0]) != 0):
                    self.tableWidget_2.setColumnCount(len(record[0]))
                    self.tableWidget_2.setHorizontalHeaderItem(
                        0, QtWidgets.QTableWidgetItem("Id"))
                    self.tableWidget_2.setHorizontalHeaderItem(
                        1, QtWidgets.QTableWidgetItem("Cancion"))
                    self.tableWidget_2.setHorizontalHeaderItem(
                        2, QtWidgets.QTableWidgetItem("Album"))
                    self.tableWidget_2.setHorizontalHeaderItem(
                        3, QtWidgets.QTableWidgetItem("Artista"))
                    # print(len(record[0]))
                    for i in range(len(record)):
                        self.tableWidget_2.insertRow(i)
                        for j in range(len(record[0])):
                            # print(i, j)
                            self.tableWidget_2.setItem(
                                i, j, QtWidgets.QTableWidgetItem(str(record[i][j])))
            except(Exception) as error:
                print("Error", error)
            finally:
                if(conn):
                   cursor.close()
                   conn.close()

        else:
            print('Mal')

    def eliminarCancion(self):
        if (self.tableWidget_2.item(self.tableWidget_2.currentRow(), 0)):
            trackid = self.tableWidget_2.item(self.tableWidget_2.currentRow(), 0).text()
            query2 = "DELETE FROM track WHERE track.trackid = \'"+ trackid +"\'"
            try:
                conn = None
                params=config()
                conn = bd.connect(**params)
                cursor = conn.cursor()
                cursor.execute("select username from user_client where clientid = \'"+str(self.id)+"\' ")
                username = cursor.fetchall()[0][0]
                query = "UPDATE track SET deleted_by=%s WHERE trackid = %s"
                data=(username, trackid)
                cursor.execute(query,data)
                cursor.execute(query2)
                conn.commit()
                self.openPopUpCheck('Se borró con éxito')
            except(Exception) as error:
                print("EROOOR", error)
                self.openPopUpError('Error')
            finally:
                if(conn):
                    cursor.close()
                    conn.close()
                    self.llenarTablaCanciones()

    def openPopUpError(self, mensaje):
        msgError = QMessageBox()
        msgError.setText(mensaje)
        msgError.setIcon(QMessageBox.Warning)
        x = msgError.exec_()

    def openPopUpCheck(self, mensaje):
        msgGood = QMessageBox()
        msgGood.setText(mensaje)
        msgGood.setIcon(QMessageBox.Information)
        y = msgGood.exec_()


    def inactivarCancion(self):
        if (self.tableWidget_2.item(self.tableWidget_2.currentRow(), 0)):
            print(str(self.tableWidget_2.item(self.tableWidget_2.currentRow(), 0).text()))
            query1 = "UPDATE track SET isactive = FALSE WHERE trackid = \'" +str(self.tableWidget_2.item(self.tableWidget_2.currentRow(), 0).text())+"\'"
            try:
               conn = None
               params=config()
               conn = bd.connect(**params)
               cursor = conn.cursor()
               cursor.execute(query1)
               conn.commit()
               self.openPopUpCheck('Se borró con éxito')
            except(Exception) as error:
               print("Error", error)
               self.openPopUpError('Error')
            finally:
               if(conn):
                  cursor.close()
                  conn.close()
                  self.llenarTablaCanciones()

    def buscarArtista(self):
        #clear the table
        self.tableWidget_3.setRowCount(0)
        if(self.textEdit_UserBuscar_3.toPlainText() != ''):
            try:
                print('Bien')
                conn = None
                params = config()
                conn = bd.connect(**params)
                cursor = conn.cursor()
                texto = self.textEdit_UserBuscar_3.toPlainText()
                query = "SELECT artist.artistid, artist.name FROM artist  WHERE UPPER(artist.name) LIKE UPPER(\'%" + \
                    texto+"%\')"
                cursor.execute(query)
                record = cursor.fetchall()
                if(len(record) != 0 and len(record[0]) != 0):
                    self.tableWidget_3.setColumnCount(len(record[0]))
                    self.tableWidget_3.setHorizontalHeaderItem(
                        0, QtWidgets.QTableWidgetItem("Id"))
                    self.tableWidget_3.setHorizontalHeaderItem(
                        1, QtWidgets.QTableWidgetItem("Artista"))
                    
                    for i in range(len(record)):
                        self.tableWidget_3.insertRow(i)
                        for j in range(len(record[0])):
                            # print(i, j)
                            self.tableWidget_3.setItem(
                                i, j, QtWidgets.QTableWidgetItem(str(record[i][j])))
            except(Exception) as error:
                print("Error", error)
            finally:
                if(conn):
                   cursor.close()
                   conn.close()

        else:
            print('Mal')

    def buscarAlbum(self):
        #clear the table
        self.tableWidget.setRowCount(0)
        if(self.textEdit_UserBuscar.toPlainText() != ''):
            try:
                print('Bien')
                conn = None
                params = config()
                conn = bd.connect(**params)
                cursor = conn.cursor()
                texto = self.textEdit_UserBuscar.toPlainText()
                query = "SELECT album.albumid, album.title, artist.name FROM album JOIN artist ON album.artistid = artist.artistid WHERE UPPER(album.title) LIKE UPPER(\'%" + \
                    texto+"%\')"
                cursor.execute(query)
                record = cursor.fetchall()
                if(len(record) != 0 and len(record[0]) != 0):
                    self.tableWidget.setColumnCount(len(record[0]))
                    self.tableWidget.setHorizontalHeaderItem(
                        0, QtWidgets.QTableWidgetItem("Id"))
                    self.tableWidget.setHorizontalHeaderItem(
                        1, QtWidgets.QTableWidgetItem("Album"))
                    self.tableWidget.setHorizontalHeaderItem(
                        2, QtWidgets.QTableWidgetItem("Artista"))
                    # print(len(record[0]))
                    for i in range(len(record)):
                        self.tableWidget.insertRow(i)
                        for j in range(len(record[0])):
                            # print(i, j)
                            self.tableWidget.setItem(
                                i, j, QtWidgets.QTableWidgetItem(str(record[i][j])))
            except(Exception) as error:
                print("Error", error)
            finally:
                if(conn):
                   cursor.close()
                   conn.close()

        else:
            print('Mal')

    def eliminarArtista(self):
        if (self.tableWidget_3.item(self.tableWidget_3.currentRow(), 0)):
            artistId = self.tableWidget_3.item(self.tableWidget_3.currentRow(), 0).text()
            query2 = "DELETE FROM artist WHERE artist.artistid = \'"+ artistId +"\'"
            print(artistId)
            try:
                conn = None
                params=config()
                conn = bd.connect(**params)
                cursor = conn.cursor()
                cursor.execute("select username from user_client where clientid = \'"+str(self.id)+"\' ")
                username = cursor.fetchall()[0][0]
                query = "UPDATE artist SET deleted_by=%s WHERE artistid = %s"
                data=(username, artistId)
                cursor.execute(query,data)
                cursor.execute(query2)
                conn.commit() 
                self.openPopUpCheck('Se borró con éxito')
            except(Exception) as error:
                print("EROOOR", error)
                self.openPopUpError('Error')
            finally:
                if(conn):
                    cursor.close()
                    conn.close()
                    self.buscarArtista()

    def eliminarAlbum(self):
        if (self.tableWidget.item(self.tableWidget.currentRow(), 0)):
            albumid = self.tableWidget.item(self.tableWidget.currentRow(), 0).text()
            query2 = "DELETE FROM album WHERE album.albumid = \'"+ albumid +"\'"
            print(albumid)
            try:
                conn = None
                params=config()
                conn = bd.connect(**params)
                cursor = conn.cursor()
                cursor.execute("select username from user_client where clientid = \'"+str(self.id)+"\' ")
                username = cursor.fetchall()[0][0]
                query = "UPDATE album SET deleted_by=%s WHERE albumid = %s"
                data=(username, albumid)
                cursor.execute(query,data)
                cursor.execute(query2)
                conn.commit() 
                self.openPopUpCheck('Se borró con éxito')
            except(Exception) as error:
                print("EROOOR", error)
                self.openPopUpError('Error')                
            finally:
                if(conn):
                    cursor.close()
                    conn.close()
                    self.buscarAlbum()

# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     HomeUserActivarEliminar = QtWidgets.QMainWindow()
#     ui = Ui_HomeUserInactivarEliminar()
#     ui.setupUi(HomeUserActivarEliminar)
#     HomeUserActivarEliminar.show()
#     sys.exit(app.exec_())
