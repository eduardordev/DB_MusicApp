# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HomeAdmin.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!
import sys
import psycopg2 as bd
import os
import csv
#import pgdb as bd
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from PyQt5.QtGui import QImage, QPainter
from PyQt5.QtCore import QFile, QDir
from HomeUserInactivarEliminar import Ui_HomeUserInactivarEliminar
from HomeUserModificar import Ui_HomeUserModificar
from Tienda import Ui_Tienda
from Mongo import Ui_Mongo
from HomeAdminReporteria import Ui_HomeAdminReporteria
from HomeUserRegistrar import Ui_HomeUserRegistrar
from HomeAdminGestionPermisos import Ui_HomeAdminGestionPermisos
from Simulacion import Ui_Simulacion
from MiMusica import Ui_MiMusica
from Bitacora import Ui_Bitacora
from queries import *
from config import config


class Ui_HomeAdmin(object):

    def __init__(self, id=0):
        super(Ui_HomeAdmin, self).__init__()
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
"border-radius: 12px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(130, 40, 205, 50))
        self.label.setMinimumSize(QtCore.QSize(205, 50))
        self.label.setMaximumSize(QtCore.QSize(205, 50))
        self.label.setStyleSheet("font: 24pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 100, 100))
        self.label_2.setMinimumSize(QtCore.QSize(100, 100))
        self.label_2.setMaximumSize(QtCore.QSize(100, 100))
        self.label_2.setStyleSheet("")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("logo.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(30, 110, 210, 25))
        self.label_3.setMinimumSize(QtCore.QSize(210, 25))
        self.label_3.setMaximumSize(QtCore.QSize(210, 25))
        self.label_3.setStyleSheet("font: 18pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label_3.setObjectName("label_3")
#         self.comboBox = QtWidgets.QComboBox(self.frame)
#         self.comboBox.setGeometry(QtCore.QRect(30, 140, 201, 30))
#         self.comboBox.setMinimumSize(QtCore.QSize(400, 30))
#         self.comboBox.setMaximumSize(QtCore.QSize(400, 30))
#         self.comboBox.setStyleSheet("background-color: rgb(150, 172, 183);\n"
# "font: 13pt \"Times\";\n"
# "color: rgb(255, 255, 255);\n"
# "border-radius: 12px;")
#         self.comboBox.setObjectName("comboBox")
#         self.comboBox.addItem("")
#         self.comboBox.addItem("")
#         self.comboBox.addItem("")
#         self.comboBox.addItem("")
#         self.comboBox.addItem("")
#         self.comboBox.addItem("")
#         self.comboBox.addItem("")
#         self.comboBox.addItem("")
#         self.comboBox.addItem("")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(30, 170, 230, 25))
        self.label_7.setMinimumSize(QtCore.QSize(230, 25))
        self.label_7.setMaximumSize(QtCore.QSize(230, 25))
        self.label_7.setStyleSheet("font: 18pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label_7.setObjectName("label_7")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(30, 270, 841, 261))
        self.tableWidget.setStyleSheet("font: 13pt \"Times\";\n"
"color: rgb(64, 55, 110);\n"
"background-color: rgb(212, 228, 188);")
        self.tableWidget.setObjectName("tableWidget")
        # self.tableWidget.setColumnCount(5)
        # self.tableWidget.setRowCount(6)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(1, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(2, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(3, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(4, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(5, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(1, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(2, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(3, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(4, item)
        self.pushButton_Exit = QtWidgets.QPushButton(self.frame)
        self.pushButton_Exit.setGeometry(QtCore.QRect(756, 50, 114, 32))
        self.pushButton_Exit.setMinimumSize(QtCore.QSize(114, 32))
        self.pushButton_Exit.setMaximumSize(QtCore.QSize(114, 32))
        self.pushButton_Exit.setStyleSheet("background-color: rgb(10, 54, 157);\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 12px;")
        self.pushButton_Exit.setObjectName("pushButton_Exit")
        self.pushButton_Exit.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.textEdit_UserBuscar = QtWidgets.QTextEdit(self.frame)
        self.textEdit_UserBuscar.setGeometry(QtCore.QRect(565, 240, 231, 31))
        self.textEdit_UserBuscar.setStyleSheet("background-color: rgb(150, 172, 183);\n"
"font: 13pt \"Times\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 12px;")
        self.textEdit_UserBuscar.setObjectName("textEdit_UserBuscar")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(534, 239, 31, 31))
        self.label_4.setStyleSheet("")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("finder.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.pushButton_Registro = QtWidgets.QPushButton(self.frame)
        self.pushButton_Registro.setGeometry(QtCore.QRect(30, 200, 114, 30))
        self.pushButton_Registro.setMinimumSize(QtCore.QSize(114, 30))
        self.pushButton_Registro.setMaximumSize(QtCore.QSize(114, 30))
        self.pushButton_Registro.setStyleSheet("background-color: rgb(10, 54, 157);\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 12px;")
        self.pushButton_Registro.setObjectName("pushButton_Registro")
        self.pushButton_Registro.clicked.connect(self.openHomeUserRegistrar)
        self.pushButton_Inactivar = QtWidgets.QPushButton(self.frame)
        self.pushButton_Inactivar.setGeometry(QtCore.QRect(272, 200, 114, 30))
        self.pushButton_Inactivar.setMinimumSize(QtCore.QSize(114, 30))
        self.pushButton_Inactivar.setMaximumSize(QtCore.QSize(114, 30))
        self.pushButton_Inactivar.setStyleSheet("background-color: rgb(10, 54, 157);\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 12px;")
        self.pushButton_Inactivar.setObjectName("pushButton_Inactivar")
        self.pushButton_Inactivar.clicked.connect(self.openHomeUserModificar)
        self.pushButton_Modficiar = QtWidgets.QPushButton(self.frame)
        self.pushButton_Modficiar.setGeometry(QtCore.QRect(514, 200, 228, 30))
        self.pushButton_Modficiar.setMinimumSize(QtCore.QSize(228, 30))
        self.pushButton_Modficiar.setMaximumSize(QtCore.QSize(228, 30))
        self.pushButton_Modficiar.setStyleSheet("background-color: rgb(10, 54, 157);\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 12px;")
        self.pushButton_Modficiar.setObjectName("pushButton_Modficiar")
        self.pushButton_Modficiar.clicked.connect(self.openHomeUserInactivarEliminar)
#         self.pushButton_Eliminar = QtWidgets.QPushButton(self.frame)
#         self.pushButton_Eliminar.setGeometry(QtCore.QRect(757, 200, 114, 30))
#         self.pushButton_Eliminar.setMinimumSize(QtCore.QSize(114, 30))
#         self.pushButton_Eliminar.setMaximumSize(QtCore.QSize(114, 30))
#         self.pushButton_Eliminar.setStyleSheet("background-color: rgb(10, 54, 157);\n"
# "font: 14pt \"Times\";\n"
# "color: rgb(255, 255, 255);\n"
# "border-radius: 12px;")
#         self.pushButton_Eliminar.setObjectName("pushButton_Eliminar")
#         self.pushButton_Eliminar.clicked.connect(self.openHomeUserInactivarEliminar)
#         self.pushButton_Op1 = QtWidgets.QPushButton(self.frame)
#         self.pushButton_Op1.setGeometry(QtCore.QRect(440, 140, 75, 30))
#         self.pushButton_Op1.setMinimumSize(QtCore.QSize(75, 30))
#         self.pushButton_Op1.setMaximumSize(QtCore.QSize(75, 30))
#         self.pushButton_Op1.setStyleSheet("background-color: rgb(10, 54, 157);\n"
# "font: 14pt \"Times\";\n"
# "color: rgb(255, 255, 255);\n"
# "border-radius: 12px;")
#         self.pushButton_Op1.setObjectName("pushButton_Op1")

        self.pushButton_Reporteria = QtWidgets.QPushButton(self.frame)
        self.pushButton_Reporteria.setGeometry(QtCore.QRect(30, 140, 100, 30))
        self.pushButton_Reporteria.setMinimumSize(QtCore.QSize(100, 30))
        self.pushButton_Reporteria.setMaximumSize(QtCore.QSize(75, 30))
        self.pushButton_Reporteria.setStyleSheet("background-color: rgb(10, 54, 157);\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_Reporteria.setObjectName("pushButton_Reporteria")
        self.pushButton_Reporteria.clicked.connect(self.openHomeAdminReporteria)
        self.comboBox_OpcionesBuscar = QtWidgets.QComboBox(self.frame)
        self.comboBox_OpcionesBuscar.setGeometry(QtCore.QRect(353, 240, 181, 31))
        self.comboBox_OpcionesBuscar.setMinimumSize(QtCore.QSize(181, 31))
        self.comboBox_OpcionesBuscar.setMaximumSize(QtCore.QSize(181, 31))
        self.comboBox_OpcionesBuscar.setStyleSheet("background-color: rgb(150, 172, 183);\n"
"font: 13pt \"Times\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 12px;")
        self.comboBox_OpcionesBuscar.setObjectName("comboBox_OpcionesBuscar")
        self.comboBox_OpcionesBuscar.addItem("")
        self.comboBox_OpcionesBuscar.addItem("")
        self.comboBox_OpcionesBuscar.addItem("")
        self.comboBox_OpcionesBuscar.addItem("")
        self.comboBox_OpcionesBuscar.addItem("")
        self.pushButton_Buscar = QtWidgets.QPushButton(self.frame)
        self.pushButton_Buscar.setGeometry(QtCore.QRect(796, 240, 75, 31))
        self.pushButton_Buscar.setMinimumSize(QtCore.QSize(75, 31))
        self.pushButton_Buscar.setMaximumSize(QtCore.QSize(75, 31))
        self.pushButton_Buscar.setStyleSheet("background-color: rgb(10, 54, 157);\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 12px;")
        self.pushButton_Buscar.setObjectName("pushButton_Buscar")
        self.pushButton_GestionPermisos = QtWidgets.QPushButton(self.frame)
        self.pushButton_GestionPermisos.setGeometry(QtCore.QRect(30, 240, 200, 30))
        self.pushButton_GestionPermisos.setMinimumSize(QtCore.QSize(200, 30))
        self.pushButton_GestionPermisos.setMaximumSize(QtCore.QSize(200, 30))
        self.pushButton_GestionPermisos.setStyleSheet("background-color: rgb(10, 54, 157);\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:12px;")
        self.pushButton_GestionPermisos.setObjectName("pushButton_Registro_2")
        self.pushButton_GestionPermisos.clicked.connect(self.openHomeAdminGestionPermisos)
        self.pushButton_Tienda = QtWidgets.QPushButton(self.frame)
        self.pushButton_Tienda.setGeometry(QtCore.QRect(630, 50, 114, 32))
        self.pushButton_Tienda.setMinimumSize(QtCore.QSize(114, 32))
        self.pushButton_Tienda.setMaximumSize(QtCore.QSize(114, 32))
        self.pushButton_Tienda.setStyleSheet("background-color: rgb(10, 54, 157);\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_Mongo = QtWidgets.QPushButton(self.frame)
        self.pushButton_Mongo.setGeometry(QtCore.QRect(504, 50, 114, 32))
        self.pushButton_Mongo.setMinimumSize(QtCore.QSize(114, 32))
        self.pushButton_Mongo.setMaximumSize(QtCore.QSize(114, 32))
        self.pushButton_Mongo.setStyleSheet("background-color: rgb(10, 54, 157);\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_Mongo.setObjectName("pushButton_Mongo")
        self.pushButton_Tienda.setObjectName("pushButton_Tienda")
        self.pushButton_MiMusica = QtWidgets.QPushButton(self.frame)
        self.pushButton_MiMusica.setGeometry(QtCore.QRect(378, 50, 114, 32))
        self.pushButton_MiMusica.setMinimumSize(QtCore.QSize(114, 32))
        self.pushButton_MiMusica.setMaximumSize(QtCore.QSize(114, 32))
        self.pushButton_MiMusica.setStyleSheet("background-color: rgb(10, 54, 157);\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_MiMusica.setObjectName("pushButton_Mongo")
        self.pushButton_Simulacion = QtWidgets.QPushButton(self.frame)
        self.pushButton_Simulacion.setGeometry(QtCore.QRect(140, 140, 100, 30))
        self.pushButton_Simulacion.setMinimumSize(QtCore.QSize(100, 30))
        self.pushButton_Simulacion.setMaximumSize(QtCore.QSize(75, 30))
        self.pushButton_Simulacion.setStyleSheet("background-color: rgb(10, 54, 157);\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_Simulacion.setObjectName("pushButton_Simulacion")
        self.pushButton_Bitacora = QtWidgets.QPushButton(self.frame)
        self.pushButton_Bitacora.setGeometry(QtCore.QRect(250, 140, 100, 30))
        self.pushButton_Bitacora.setMinimumSize(QtCore.QSize(100, 30))
        self.pushButton_Bitacora.setMaximumSize(QtCore.QSize(75, 30))
        self.pushButton_Bitacora.setStyleSheet("background-color: rgb(10, 54, 157);\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_Bitacora.setObjectName("pushButton_Bitacora")
        self.comboBox_OpcionesBuscar.raise_()
        self.label_7.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        # self.comboBox.raise_()
        self.tableWidget.raise_()
        self.pushButton_Exit.raise_()
        self.textEdit_UserBuscar.raise_()
        self.label_4.raise_()
        self.pushButton_Registro.raise_()
        self.pushButton_Inactivar.raise_()
        self.pushButton_Modficiar.raise_()
        # self.pushButton_Eliminar.raise_()
        # self.pushButton_Op1.raise_()
        self.pushButton_Buscar.raise_()
        self.pushButton_GestionPermisos.raise_()
        self.pushButton_Tienda.raise_()
        self.pushButton_Mongo.raise_()
        self.pushButton_Tienda.clicked.connect(self.openTienda)
        self.pushButton_Mongo.clicked.connect(self.openMongo)
        self.pushButton_MiMusica.raise_()
        self.pushButton_MiMusica.clicked.connect(self.openMiMusica)
        self.pushButton_Simulacion.raise_()
        self.pushButton_Bitacora.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Sonido Cloud "))
        self.label_3.setText(_translate("MainWindow", "Módulo de reportería"))
        # self.comboBox.setItemText(0, _translate("MainWindow", "Reportería"))
        # self.comboBox.setItemText(1, _translate("MainWindow", "1. Los 5 artistas con más álbumes publicados"))
        # self.comboBox.setItemText(2, _translate("MainWindow", "2. Los 5 géneros con más canciones"))
        # self.comboBox.setItemText(3, _translate("MainWindow", "3. Total de duración de cada playlist"))
        # self.comboBox.setItemText(4, _translate("MainWindow", "4. Las 5 canciones de mayor duración con información del artista"))
        # self.comboBox.setItemText(5, _translate("MainWindow", "5. Los 5 usuarios que han registrado más canciones"))
        # self.comboBox.setItemText(6, _translate("MainWindow", "6. Promedio de duración de canciones por género"))
        # self.comboBox.setItemText(7, _translate("MainWindow", "7. Cantidad de artistas diferentes por playlist"))
        # self.comboBox.setItemText(8, _translate("MainWindow", "8. Los 5 artistas con más diversidad de géneros"))
        self.label_7.setText(_translate("MainWindow", "Módulo de autorización"))
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
        # item.setText(_translate("MainWindow", "aqui"))
        # item = self.tableWidget.horizontalHeaderItem(1)
        # item.setText(_translate("MainWindow", "van"))
        # item = self.tableWidget.horizontalHeaderItem(2)
        # item.setText(_translate("MainWindow", "las"))
        # item = self.tableWidget.horizontalHeaderItem(3)
        # item.setText(_translate("MainWindow", "columnas"))
        # item = self.tableWidget.horizontalHeaderItem(4)
        # item.setText(_translate("MainWindow", "proyecto"))
        self.pushButton_Exit.setText(_translate("MainWindow", "Salir"))
        self.textEdit_UserBuscar.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_Registro.setText(_translate("MainWindow", "Registro"))
        self.pushButton_Inactivar.setText(_translate("MainWindow", "Modificación"))
        self.pushButton_Modficiar.setText(_translate("MainWindow", "Inactivación/Eliminación"))
        # self.pushButton_Eliminar.setText(_translate("MainWindow", "Eliminación"))
        # self.pushButton_Op1.setText(_translate("MainWindow", "Reporte"))
        # self.pushButton_Op1.clicked.connect(self.report)
        self.pushButton_Reporteria.setText(_translate("MainWindow", "Reportería"))
        self.pushButton_Reporteria.clicked.connect(self.openHomeAdminReporteria)
        self.comboBox_OpcionesBuscar.setItemText(0, _translate("MainWindow", "¿Qué deseas buscar?"))
        self.comboBox_OpcionesBuscar.setItemText(1, _translate("MainWindow", "Artista"))
        self.comboBox_OpcionesBuscar.setItemText(2, _translate("MainWindow", "Género"))
        self.comboBox_OpcionesBuscar.setItemText(3, _translate("MainWindow", "Álbum"))
        self.comboBox_OpcionesBuscar.setItemText(4, _translate("MainWindow", "Canción"))
        self.pushButton_Buscar.setText(_translate("MainWindow", "Buscar"))
        self.pushButton_GestionPermisos.setText(_translate("MainWindow", "Gestión de permisos"))
        self.pushButton_Buscar.clicked.connect(self.populateTable)
        self.pushButton_Tienda.setText(_translate("MainWindow", "Tienda"))
        self.pushButton_Mongo.setText(_translate("MainWindow", "Mongo"))
        self.pushButton_Simulacion.setText(_translate("MainWindow", "Simulación"))
        self.pushButton_Simulacion.clicked.connect(self.openSimulacion)
        self.pushButton_MiMusica.setText(_translate("MainWindow", "Mi Música"))
        self.pushButton_Bitacora.setText(_translate("MainWindow", "Bitácora"))
        self.pushButton_Bitacora.clicked.connect(self.openBitacora)

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

    def openTienda(self, id):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Tienda(self.id)
        self.ui.setupUi(self.window)
        self.window.show()

    def openBitacora(self, id):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Bitacora(self.id)
        self.ui.setupUi(self.window)
        self.window.show()

    def openSimulacion(self, id):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Simulacion(self.id)
        self.ui.setupUi(self.window)
        self.window.show()

    def openMongo(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Mongo()
        self.ui.setupUi(self.window)
        self.window.show()

    def openMiMusica(self, id):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MiMusica(self.id)
        self.ui.setupUi(self.window)
        self.window.show()

    def openHomeAdminReporteria(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_HomeAdminReporteria()
        self.ui.setupUi(self.window)
        self.window.show()

    def openHomeUserInactivarEliminar(self, id):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_HomeUserInactivarEliminar(self.id)
        self.ui.setupUi(self.window)
        self.window.show()

    def openHomeUserModificar(self, id):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_HomeUserModificar(self.id)
        self.ui.setupUi(self.window)
        self.window.show()

    def openHomeUserRegistrar(self, id):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_HomeUserRegistrar(self.id)
        self.ui.setupUi(self.window)
        self.window.show()

    def openHomeAdminGestionPermisos(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_HomeAdminGestionPermisos(self.id)
        self.ui.setupUi(self.window)
        self.window.show()

    def populateTable(self):
        #clear the table
        self.tableWidget.setRowCount(0)
        if(self.textEdit_UserBuscar.toPlainText()!='' and self.comboBox_OpcionesBuscar.currentText() != '¿Qué deseas buscar?' ):
            print('Bien')
            print(self.id)
            conn = None
            params =config()
            conn = bd.connect(**params)
            cursor = conn.cursor()
            if(self.comboBox_OpcionesBuscar.currentText() == 'Artista'):
                query = "SELECT track.name, artist.name FROM track JOIN album ON track.albumid = album.albumid JOIN artist ON album.artistid = artist.artistid WHERE artist.name ~* \'" + self.textEdit_UserBuscar.toPlainText() +"'"
                cursor.execute(query)
                record = cursor.fetchall()
                print(record)
                if(len(record)!= 0):
                    self.tableWidget.setColumnCount(len(record[0]))
                    for i in range(len(record)):
                        self.tableWidget.insertRow(i)
                        for j in range(len(record[0])):
                            print(i,j)
                            self.tableWidget.setItem(i,j, QtWidgets.QTableWidgetItem(record[i][j]))


            elif(self.comboBox_OpcionesBuscar.currentText() == 'Género'):
                query = "SELECT track.name, genre.name FROM track INNER JOIN genre ON track.genreid = genre.genreid WHERE genre.name ~* \'" + self.textEdit_UserBuscar.toPlainText() +"'"
                cursor.execute(query)
                record = cursor.fetchall()
                if(len(record)!= 0):
                    self.tableWidget.setColumnCount(len(record[0]))
                    for i in range(len(record)):
                        self.tableWidget.insertRow(i)
                        for j in range(len(record[0])):
                            self.tableWidget.setItem(i,j, QtWidgets.QTableWidgetItem(record[i][j]))

            elif(self.comboBox_OpcionesBuscar.currentText() == 'Álbum'):
                query = "SELECT track.name FROM track INNER JOIN album ON track.albumid = album.albumid WHERE album.title ~* \'" + self.textEdit_UserBuscar.toPlainText() +"'"
                cursor.execute(query)
                record = cursor.fetchall()
                if(len(record)!= 0):
                    self.tableWidget.setColumnCount(len(record[0]))
                    for i in range(len(record)):
                        self.tableWidget.insertRow(i)
                        for j in range(len(record[0])):
                            self.tableWidget.setItem(i,j, QtWidgets.QTableWidgetItem(record[i][j]))

            elif(self.comboBox_OpcionesBuscar.currentText() == 'Canción'):
                query = "SELECT track.name FROM track  WHERE name ~* \'" + self.textEdit_UserBuscar.toPlainText() +"'"
                cursor.execute(query)
                record = cursor.fetchall()
                if(len(record)!= 0):
                    self.tableWidget.setColumnCount(len(record[0]))
                    for i in range(len(record)):
                        self.tableWidget.insertRow(i)
                        for j in range(len(record[0])):
                            self.tableWidget.setItem(i,j, QtWidgets.QTableWidgetItem(str(record[i][j])))
        else:
            print('Mal')

    def populateTableOpcion1(self):
        self.tableWidget.setRowCount(0)
        conn = None
        params =config()
        conn = bd.connect(**params)
        cursor = conn.cursor()
        query = query1()
        cursor.execute(query)
        record = cursor.fetchall()
        if(len(record)!= 0):
            self.tableWidget.setColumnCount(len(record[0]))
            for i in range(len(record)):
                self.tableWidget.insertRow(i)
                for j in range(len(record[0])):
                    self.tableWidget.setItem(i,j, QtWidgets.QTableWidgetItem(str(record[i][j])))
            with open('Opcion1.csv', 'w') as f:
                thewriter = csv.writer(f, delimiter=',')
                thewriter.writerow(['Artista', 'No. Albumés publicados'])
                for row in record:
                    thewriter.writerow(row)
            

    def populateTableOpcion2(self):
        self.tableWidget.setRowCount(0)
        conn = None
        params =config()
        conn = bd.connect(**params)
        cursor = conn.cursor()
        query = query2()
        cursor.execute(query)
        record = cursor.fetchall()
        if(len(record)!= 0):
            self.tableWidget.setColumnCount(len(record[0]))
            for i in range(len(record)):
                self.tableWidget.insertRow(i)
                for j in range(len(record[0])):
                    self.tableWidget.setItem(i,j, QtWidgets.QTableWidgetItem(str(record[i][j])))
            with open('Opcion2.csv', 'w', newline='') as f:
                thewriter = csv.writer(f, delimiter=',')
                thewriter.writerow(['Genero', 'No. Canciones'])
                for row in record:
                    thewriter.writerow(row)


    def populateTableOpcion3(self):
        self.tableWidget.setRowCount(0)
        conn = None
        params =config()
        conn = bd.connect(**params)
        cursor = conn.cursor()
        query = query3()
        cursor.execute(query)
        record = cursor.fetchall()
        if(len(record)!= 0):
            self.tableWidget.setColumnCount(len(record[0]))
            for i in range(len(record)):
                self.tableWidget.insertRow(i)
                for j in range(len(record[0])):
                    self.tableWidget.setItem(i,j, QtWidgets.QTableWidgetItem(str(record[i][j])))
            with open('Opcion3.csv', 'w', newline='') as f:
                thewriter = csv.writer(f, delimiter=',')
                thewriter.writerow(['Playlist', 'Duración (milisegundos)'])
                for row in record:
                    thewriter.writerow(row)


    def populateTableOpcion4(self):
        self.tableWidget.setRowCount(0)
        conn = None
        params =config()
        conn = bd.connect(**params)
        cursor = conn.cursor()
        query = query4()
        cursor.execute(query)
        record = cursor.fetchall()
        if(len(record)!= 0):
            self.tableWidget.setColumnCount(len(record[0]))
            for i in range(len(record)):
                self.tableWidget.insertRow(i)
                for j in range(len(record[0])):
                    self.tableWidget.setItem(i,j, QtWidgets.QTableWidgetItem(str(record[i][j])))
            with open('Opcion4.csv', 'w', newline='') as f:
                thewriter = csv.writer(f, delimiter=',')
                thewriter.writerow(['Canción','Artista', 'Duración (milisegundos)'])
                for row in record:
                    thewriter.writerow(row)


    def populateTableOpcion5(self):
        self.tableWidget.setRowCount(0)
        conn = None
        params =config()
        conn = bd.connect(**params)
        cursor = conn.cursor()
        query = query5()
        cursor.execute(query)
        record = cursor.fetchall()
        if(len(record)!= 0):
            self.tableWidget.setColumnCount(len(record[0]))
            for i in range(len(record)):
                self.tableWidget.insertRow(i)
                for j in range(len(record[0])):
                    self.tableWidget.setItem(i,j, QtWidgets.QTableWidgetItem(str(record[i][j])))
            with open('Opcion5.csv', 'w', newline='') as f:
                thewriter = csv.writer(f, delimiter=',')
                thewriter.writerow(['Nombre', 'No. Canciones Subidas'])
                for row in record:
                    thewriter.writerow(row)


    def populateTableOpcion6(self):
        self.tableWidget.setRowCount(0)
        conn = None
        params =config()
        conn = bd.connect(**params)
        cursor = conn.cursor()
        query = query6()
        cursor.execute(query)
        record = cursor.fetchall()
        if(len(record)!= 0):
            self.tableWidget.setColumnCount(len(record[0]))
            for i in range(len(record)):
                self.tableWidget.insertRow(i)
                for j in range(len(record[0])):
                    self.tableWidget.setItem(i,j, QtWidgets.QTableWidgetItem(str(record[i][j])))
            with open('Opcion6.csv', 'w', newline='') as f:
                thewriter = csv.writer(f, delimiter=',')
                thewriter.writerow(['Canción', 'Promedio de duración (milisegundos)'])
                for row in record:
                    thewriter.writerow(row)


    def populateTableOpcion7(self):
        self.tableWidget.setRowCount(0)
        conn = None
        params =config()
        conn = bd.connect(**params)
        cursor = conn.cursor()
        query = query7()
        cursor.execute(query)
        record = cursor.fetchall()
        if(len(record)!= 0):
            self.tableWidget.setColumnCount(len(record[0]))
            for i in range(len(record)):
                self.tableWidget.insertRow(i)
                for j in range(len(record[0])):
                    self.tableWidget.setItem(i,j, QtWidgets.QTableWidgetItem(str(record[i][j])))
            with open('Opcion7.csv', 'w', newline='') as f:
                thewriter = csv.writer(f, delimiter=',')
                thewriter.writerow(['Playlist', 'No. Artistas diferentes'])
                for row in record:
                    thewriter.writerow(row)



    def populateTableOpcion8(self):
        self.tableWidget.setRowCount(0)
        conn = None
        params =config()
        conn = bd.connect(**params)
        cursor = conn.cursor()
        query = query8()
        cursor.execute(query)
        record = cursor.fetchall()
        if(len(record)!= 0):
            self.tableWidget.setColumnCount(len(record[0]))
            for i in range(len(record)):
                self.tableWidget.insertRow(i)
                for j in range(len(record[0])):
                    self.tableWidget.setItem(i,j, QtWidgets.QTableWidgetItem(str(record[i][j])))
            with open('Opcion8.csv', 'w') as f:
                thewriter = csv.writer(f, delimiter=',')
                thewriter.writerow(['Artista', 'No. Generos'])
                for row in record:
                    thewriter.writerow(row)
        


    def report(self):
        if(self.comboBox.currentText()=="Reportería"):
            print("Eliga una opcion")
        elif(self.comboBox.currentText()=="1. Los 5 artistas con más álbumes publicados"):
            self.populateTableOpcion1()
        elif(self.comboBox.currentText()=="2. Los 5 géneros con más canciones"):
            self.populateTableOpcion2()
        elif(self.comboBox.currentText()=="3. Total de duración de cada playlist"):
            self.populateTableOpcion3()
        elif(self.comboBox.currentText()=="4. Las 5 canciones de mayor duración con información del artista"):
            self.populateTableOpcion4()
        elif(self.comboBox.currentText()=="5. Los 5 usuarios que han registrado más canciones"):
            self.populateTableOpcion5()
        elif(self.comboBox.currentText()=="6. Promedio de duración de canciones por género"):
            self.populateTableOpcion6()
        elif(self.comboBox.currentText()=="7. Cantidad de artistas diferentes por playlist"):
            self.populateTableOpcion7()
        elif(self.comboBox.currentText()=="8. Los 5 artistas con más diversidad de géneros"):
            self.populateTableOpcion8()

    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    HomeAdmin = QtWidgets.QMainWindow()
    ui = Ui_HomeAdmin()
    ui.setupUi(HomeAdmin)
    HomeAdmin.show()
    sys.exit(app.exec_())

