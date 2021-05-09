# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HomeUserModificar.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import psycopg2 as bd
from config import config
#import pgdb as bd

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HomeUserModificar(object):
    def __init__(self, id):
        super(Ui_HomeUserModificar, self).__init__()
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
#         self.pushButton_Exit = QtWidgets.QPushButton(self.frame)
#         self.pushButton_Exit.setGeometry(QtCore.QRect(756, 50, 114, 32))
#         self.pushButton_Exit.setMinimumSize(QtCore.QSize(114, 32))
#         self.pushButton_Exit.setMaximumSize(QtCore.QSize(114, 32))
#         self.pushButton_Exit.setStyleSheet("background-color: rgb(10, 54, 157);\n"
# "font: 14pt \"Times\";\n"
# "color: rgb(255, 255, 255);")
#         self.pushButton_Exit.setObjectName("pushButton_Exit")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(30, 190, 100, 25))
        self.label_3.setMinimumSize(QtCore.QSize(100, 25))
        self.label_3.setMaximumSize(QtCore.QSize(100, 25))
        self.label_3.setStyleSheet("font: 18pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label_3.setObjectName("label_3")
        self.textEdit_ArtistaNombre = QtWidgets.QTextEdit(self.frame)
        self.textEdit_ArtistaNombre.setGeometry(QtCore.QRect(30, 220, 220, 30))
        self.textEdit_ArtistaNombre.setMinimumSize(QtCore.QSize(220, 30))
        self.textEdit_ArtistaNombre.setMaximumSize(QtCore.QSize(220, 30))
        self.textEdit_ArtistaNombre.setStyleSheet("background-color: rgb(150, 172, 183);\n"
"color: rgb(255, 255, 255);\n"
"font: 13pt \"Times\";")
        self.textEdit_ArtistaNombre.setObjectName("textEdit_ArtistaNombre")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(506, 190, 100, 25))
        self.label_4.setMinimumSize(QtCore.QSize(100, 25))
        self.label_4.setMaximumSize(QtCore.QSize(100, 25))
        self.label_4.setStyleSheet("font: 18pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label_4.setObjectName("label_4")
        self.textEdit_AlbumNombre = QtWidgets.QTextEdit(self.frame)
        self.textEdit_AlbumNombre.setGeometry(QtCore.QRect(506, 220, 220, 30))
        self.textEdit_AlbumNombre.setMinimumSize(QtCore.QSize(220, 30))
        self.textEdit_AlbumNombre.setMaximumSize(QtCore.QSize(220, 30))
        self.textEdit_AlbumNombre.setStyleSheet("background-color: rgb(150, 172, 183);\n"
"color: rgb(255, 255, 255);\n"
"font: 13pt \"Times\";")
        self.textEdit_AlbumNombre.setObjectName("textEdit_AlbumNombre")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(30, 130, 220, 50))
        self.label_6.setMinimumSize(QtCore.QSize(220, 50))
        self.label_6.setMaximumSize(QtCore.QSize(220, 50))
        self.label_6.setStyleSheet("font: 21pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(506, 130, 220, 50))
        self.label_7.setMinimumSize(QtCore.QSize(220, 50))
        self.label_7.setMaximumSize(QtCore.QSize(220, 50))
        self.label_7.setStyleSheet("font: 21pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(30, 350, 220, 50))
        self.label_9.setMinimumSize(QtCore.QSize(220, 50))
        self.label_9.setMaximumSize(QtCore.QSize(220, 50))
        self.label_9.setStyleSheet("font: 21pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(30, 410, 100, 25))
        self.label_10.setMinimumSize(QtCore.QSize(100, 25))
        self.label_10.setMaximumSize(QtCore.QSize(100, 25))
        self.label_10.setStyleSheet("font: 18pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label_10.setObjectName("label_10")
        self.textEdit_CancionNombre = QtWidgets.QTextEdit(self.frame)
        self.textEdit_CancionNombre.setGeometry(QtCore.QRect(30, 440, 220, 30))
        self.textEdit_CancionNombre.setMinimumSize(QtCore.QSize(220, 30))
        self.textEdit_CancionNombre.setMaximumSize(QtCore.QSize(220, 30))
        self.textEdit_CancionNombre.setStyleSheet("background-color: rgb(150, 172, 183);\n"
"color: rgb(255, 255, 255);\n"
"font: 13pt \"Times\";")
        self.textEdit_CancionNombre.setObjectName("textEdit_CancionNombre")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(340, 410, 114, 25))
        self.label_12.setMinimumSize(QtCore.QSize(114, 25))
        self.label_12.setMaximumSize(QtCore.QSize(114, 25))
        self.label_12.setStyleSheet("font: 18pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label_12.setObjectName("label_12")
        self.label_14 = QtWidgets.QLabel(self.frame)
        self.label_14.setGeometry(QtCore.QRect(650, 410, 350, 25))
        self.label_14.setMinimumSize(QtCore.QSize(350, 25))
        self.label_14.setMaximumSize(QtCore.QSize(350, 25))
        self.label_14.setStyleSheet("font: 18pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label_14.setObjectName("label_14")
        self.textEdit_CambioNuevo = QtWidgets.QTextEdit(self.frame)
        self.textEdit_CambioNuevo.setGeometry(QtCore.QRect(650, 440, 220, 30))
        self.textEdit_CambioNuevo.setMinimumSize(QtCore.QSize(220, 30))
        self.textEdit_CambioNuevo.setMaximumSize(QtCore.QSize(220, 30))
        self.textEdit_CambioNuevo.setStyleSheet("background-color: rgb(150, 172, 183);\n"
"color: rgb(255, 255, 255);\n"
"font: 13pt \"Times\";")
        self.textEdit_CambioNuevo.setObjectName("textEdit_CambioNuevo")
        self.pushButton_MAlbum = QtWidgets.QPushButton(self.frame)
        self.pushButton_MAlbum.setGeometry(QtCore.QRect(756, 258, 114, 32))
        self.pushButton_MAlbum.setMinimumSize(QtCore.QSize(114, 32))
        self.pushButton_MAlbum.setMaximumSize(QtCore.QSize(114, 32))
        self.pushButton_MAlbum.setStyleSheet("background-color: rgb(10, 54, 157);\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_MAlbum.setObjectName("pushButton_MAlbum")
        self.pushButton_MAlbum.clicked.connect(self.modifyAlbum)
        self.pushButton_MArtista = QtWidgets.QPushButton(self.frame)
        self.pushButton_MArtista.setGeometry(QtCore.QRect(280, 258, 114, 32))
        self.pushButton_MArtista.setMinimumSize(QtCore.QSize(114, 32))
        self.pushButton_MArtista.setMaximumSize(QtCore.QSize(114, 32))
        self.pushButton_MArtista.setStyleSheet("background-color: rgb(10, 54, 157);\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_MArtista.setObjectName("pushButton_MArtista")
        self.pushButton_MArtista.clicked.connect(self.modifyArtist)
        self.pushButton_MCancion = QtWidgets.QPushButton(self.frame)
        self.pushButton_MCancion.setGeometry(QtCore.QRect(390, 480, 114, 32))
        self.pushButton_MCancion.setMinimumSize(QtCore.QSize(114, 32))
        self.pushButton_MCancion.setMaximumSize(QtCore.QSize(114, 32))
        self.pushButton_MCancion.setStyleSheet("background-color: rgb(10, 54, 157);\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_MCancion.setObjectName("pushButton_MCancion")
        self.pushButton_MCancion.clicked.connect(self.modifySong)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(30, 260, 150, 25))
        self.label_5.setMinimumSize(QtCore.QSize(150, 25))
        self.label_5.setMaximumSize(QtCore.QSize(150, 25))
        self.label_5.setStyleSheet("font: 18pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label_5.setObjectName("label_5")
        self.textEdit_ArtistaNuevoNombre = QtWidgets.QTextEdit(self.frame)
        self.textEdit_ArtistaNuevoNombre.setGeometry(QtCore.QRect(30, 290, 220, 30))
        self.textEdit_ArtistaNuevoNombre.setMinimumSize(QtCore.QSize(220, 30))
        self.textEdit_ArtistaNuevoNombre.setMaximumSize(QtCore.QSize(220, 30))
        self.textEdit_ArtistaNuevoNombre.setStyleSheet("background-color: rgb(150, 172, 183);\n"
"color: rgb(255, 255, 255);\n"
"font: 13pt \"Times\";")
        self.textEdit_ArtistaNuevoNombre.setObjectName("textEdit_ArtistaNuevoNombre")
        self.label_15 = QtWidgets.QLabel(self.frame)
        self.label_15.setGeometry(QtCore.QRect(506, 260, 150, 25))
        self.label_15.setMinimumSize(QtCore.QSize(150, 25))
        self.label_15.setMaximumSize(QtCore.QSize(150, 25))
        self.label_15.setStyleSheet("font: 18pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label_15.setObjectName("label_15")
        self.textEdit_AlbumNuevoNombre = QtWidgets.QTextEdit(self.frame)
        self.textEdit_AlbumNuevoNombre.setGeometry(QtCore.QRect(506, 290, 220, 30))
        self.textEdit_AlbumNuevoNombre.setMinimumSize(QtCore.QSize(220, 30))
        self.textEdit_AlbumNuevoNombre.setMaximumSize(QtCore.QSize(220, 30))
        self.textEdit_AlbumNuevoNombre.setStyleSheet("background-color: rgb(150, 172, 183);\n"
"color: rgb(255, 255, 255);\n"
"font: 13pt \"Times\";")
        self.textEdit_AlbumNuevoNombre.setObjectName("textEdit_AlbumNuevoNombre")
        self.comboBox_OpcionesCambioCanciones = QtWidgets.QComboBox(self.frame)
        self.comboBox_OpcionesCambioCanciones.setGeometry(QtCore.QRect(340, 440, 220, 30))
        self.comboBox_OpcionesCambioCanciones.setMinimumSize(QtCore.QSize(220, 30))
        self.comboBox_OpcionesCambioCanciones.setMaximumSize(QtCore.QSize(220, 30))
        self.comboBox_OpcionesCambioCanciones.setStyleSheet("background-color: rgb(150, 172, 183);\n"
"color: rgb(255, 255, 255);\n"
"font: 13pt \"Times\";")
        self.comboBox_OpcionesCambioCanciones.setObjectName("comboBox_OpcionesCambioCanciones")
        self.comboBox_OpcionesCambioCanciones.addItem("")
        self.comboBox_OpcionesCambioCanciones.addItem("")
        self.comboBox_OpcionesCambioCanciones.addItem("")
        self.comboBox_OpcionesCambioCanciones.addItem("")
        self.comboBox_OpcionesCambioCanciones.addItem("")
        self.comboBox_OpcionesCambioCanciones.addItem("")
        self.comboBox_OpcionesCambioCanciones.addItem("")
        self.comboBox_OpcionesCambioCanciones.addItem("")
        self.label.raise_()
        self.label_2.raise_()
        # self.pushButton_Exit.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.textEdit_CancionNombre.raise_()
        self.label_12.raise_()
        self.label_14.raise_()
        self.textEdit_CambioNuevo.raise_()
        self.pushButton_MAlbum.raise_()
        self.pushButton_MArtista.raise_()
        self.pushButton_MCancion.raise_()
        self.label_5.raise_()
        self.textEdit_ArtistaNuevoNombre.raise_()
        self.label_3.raise_()
        self.textEdit_ArtistaNombre.raise_()
        self.label_4.raise_()
        self.textEdit_AlbumNombre.raise_()
        self.label_15.raise_()
        self.textEdit_AlbumNuevoNombre.raise_()
        self.comboBox_OpcionesCambioCanciones.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Sonido Cloud "))
        # self.pushButton_Exit.setText(_translate("MainWindow", "Exit"))
        self.label_3.setText(_translate("MainWindow", "Nombre"))
        self.textEdit_ArtistaNombre.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.SF NS Text\';\"><br /></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "Nombre"))
        self.textEdit_AlbumNombre.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.SF NS Text\';\"><br /></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "Modificar Artistas"))
        self.label_7.setText(_translate("MainWindow", "Modificar Álbumes"))
        self.label_9.setText(_translate("MainWindow", "Modificar Canciones"))
        self.label_10.setText(_translate("MainWindow", "Nombre"))
        self.textEdit_CancionNombre.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.SF NS Text\';\"><br /></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "Campo a Cambiar"))
        self.label_14.setText(_translate("MainWindow", "Nuevo Nombre"))
        self.textEdit_CambioNuevo.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.SF NS Text\';\"><br /></p></body></html>"))
        self.pushButton_MAlbum.setText(_translate("MainWindow", "Modificar"))
        self.pushButton_MArtista.setText(_translate("MainWindow", "Modificar"))
        self.pushButton_MCancion.setText(_translate("MainWindow", "Modificar"))
        self.label_5.setText(_translate("MainWindow", "Nuevo Nombre"))
        self.textEdit_ArtistaNuevoNombre.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.SF NS Text\';\"><br /></p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "Nuevo Nombre"))
        self.textEdit_AlbumNuevoNombre.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.SF NS Text\';\"><br /></p></body></html>"))
        self.comboBox_OpcionesCambioCanciones.setItemText(0, _translate("MainWindow", "¿Que deseas cambiar?"))
        self.comboBox_OpcionesCambioCanciones.setItemText(1, _translate("MainWindow", "Nombre"))
        self.comboBox_OpcionesCambioCanciones.setItemText(2, _translate("MainWindow", "Género"))
        self.comboBox_OpcionesCambioCanciones.setItemText(3, _translate("MainWindow", "Álbum"))
        self.comboBox_OpcionesCambioCanciones.setItemText(4, _translate("MainWindow", "UnitPrice"))
        self.comboBox_OpcionesCambioCanciones.setItemText(5, _translate("MainWindow", "Bytes"))
        self.comboBox_OpcionesCambioCanciones.setItemText(6, _translate("MainWindow", "Composer"))
        self.comboBox_OpcionesCambioCanciones.setItemText(7, _translate("MainWindow", "Milisegundos"))

    def modifyArtist (self):
        if(self.textEdit_ArtistaNombre.toPlainText()=="" and self.textEdit_ArtistaNombre.toPlainText()==" " and self.textEdit_ArtistaNuevoNombre.toPlainText() =="" and self.textEdit_ArtistaNuevoNombre.toPlainText() ==" " ):
            print('no voy a hacer nada')
            self.openPopUpError('Tiene que llenar todos los campos')
        else:
            params = config()
            conn = bd.connect(**params)
            cursor = conn.cursor()
            cursor.execute("select username from user_client where clientid = \'"+str(self.id)+"\' ")
            username = cursor.fetchall()[0][0]
            query = """
                UPDATE artist
                SET name = %s, last_modified_by= %s
                WHERE name = %s
                RETURNING artistid, name
            """
            cursor.execute(query,(self.textEdit_ArtistaNuevoNombre.toPlainText(),username,self.textEdit_ArtistaNombre.toPlainText()))
            conn.commit()
            self.openPopUpCheck('Se modifcó con éxito')
            record= cursor.fetchall()
            print(record)


    def modifyAlbum(self):
        if(self.textEdit_AlbumNombre.toPlainText()=="" and self.textEdit_AlbumNombre.toPlainText()==" " and self.textEdit_AlbumNuevoNombre.toPlainText() =="" and self.textEdit_AlbumNuevoNombre.toPlainText() ==" " ):
            print('no voy a hacer nada')
            self.openPopUpError('Tiene que llenar todos los campos')
        else:
            params = config()
            conn = bd.connect(**params)
            cursor = conn.cursor()
            cursor.execute("select username from user_client where clientid = \'"+str(self.id)+"\' ")
            username = cursor.fetchall()[0][0]
            query = """
                UPDATE album
                SET title = %s, last_modified_by= %s
                WHERE title = %s
                RETURNING albumid, title
            """
            cursor.execute(query,(self.textEdit_AlbumNuevoNombre.toPlainText(),username,self.textEdit_AlbumNombre.toPlainText()))
            conn.commit()
            self.openPopUpCheck('Se modifcó con éxito')
            record= cursor.fetchall()
            print(record)

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


    def modifySong(self):
        if(self.textEdit_CancionNombre.toPlainText()!="" and self.textEdit_CambioNuevo.toPlainText()!=""):
            params = config()
            conn = bd.connect(**params)
            cursor = conn.cursor()
            cursor.execute("select username from user_client where clientid = \'"+str(self.id)+"\' ")
            username = cursor.fetchall()[0][0]
            if(self.comboBox_OpcionesCambioCanciones.currentIndex()==0):
                print('no voy a hacer nada')
                self.openPopUpError('Tiene que elegis una opcion')
            elif(self.comboBox_OpcionesCambioCanciones.currentIndex()==1):
                params = config()
                conn = bd.connect(**params)
                cursor = conn.cursor()
                query = """
                    UPDATE track
                    SET name = %s, last_modified_by= %s
                    WHERE name = %s
                    RETURNING track id, name
                """
                cursor.execute(query,(self.textEdit_CambioNuevo.toPlainText(),username,self.textEdit_CancionNombre.toPlainText()))
                conn.commit()
                self.openPopUpCheck('Se modifcó con éxito')
                record= cursor.fetchall()
                print(record)

            elif(self.comboBox_OpcionesCambioCanciones.currentIndex()==2):
                try:
                    params = config()
                    conn = bd.connect(**params)
                    cursor = conn.cursor()
                    query = """
                        UPDATE track
                        SET genreid = %s, last_modified_by= %s
                        WHERE name = %s
                        RETURNING trackid , name 
                    """
                    cursor.execute(query,(int(self.textEdit_CambioNuevo.toPlainText()),username,self.textEdit_CancionNombre.toPlainText()))
                    conn.commit()
                    self.openPopUpCheck('Se modifcó con éxito')
                    record= cursor.fetchall()
                    print(record)    
                except (Exception) as error:
                    print(error)
                

            elif(self.comboBox_OpcionesCambioCanciones.currentIndex()==3):
                try:
                    params = config()
                    conn = bd.connect(**params)
                    cursor = conn.cursor()
                    query = """
                        UPDATE track
                        SET albumid = %s, last_modified_by= %s
                        WHERE name = %s
                        RETURNING trackid , name 
                    """
                    cursor.execute(query,(int(self.textEdit_CambioNuevo.toPlainText()),username,self.textEdit_CancionNombre.toPlainText()))
                    conn.commit()
                    self.openPopUpCheck('Se modifcó con éxito')
                    record= cursor.fetchall()
                    print(record)    
                except (Exception) as error:
                    print(error)

            elif(self.comboBox_OpcionesCambioCanciones.currentIndex()==4):
                params = config()
                conn = bd.connect(**params)
                cursor = conn.cursor()
                query = """
                    UPDATE track
                    SET unitprice = %s, last_modified_by= %s
                    WHERE name = %s
                    RETURNING trackid , name
                """
                cursor.execute(query,(float(self.textEdit_CambioNuevo.toPlainText()),username,self.textEdit_CancionNombre.toPlainText()))
                conn.commit()
                self.openPopUpCheck('Se modifcó con éxito')
                record= cursor.fetchall()
                print(record)

            elif(self.comboBox_OpcionesCambioCanciones.currentIndex()==5):
                params = config()
                conn = bd.connect(**params)
                cursor = conn.cursor()
                query = """
                    UPDATE track
                    SET bytes = %s, last_modified_by= %s
                    WHERE name = %s
                    RETURNING trackid , name
                """
                cursor.execute(query,(int(self.textEdit_CambioNuevo.toPlainText()),username,self.textEdit_CancionNombre.toPlainText()))
                conn.commit()
                self.openPopUpCheck('Se modifcó con éxito')
                record= cursor.fetchall()
                print(record)

            elif(self.comboBox_OpcionesCambioCanciones.currentIndex()==6):
                params = config()
                conn = bd.connect(**params)
                cursor = conn.cursor()
                query = """
                    UPDATE track
                    SET composer = %s, last_modified_by= %s
                    WHERE name = %s
                    RETURNING trackid , name
                """
                cursor.execute(query,(self.textEdit_CambioNuevo.toPlainText(),username,self.textEdit_CancionNombre.toPlainText()))
                conn.commit()
                self.openPopUpCheck('Se modifcó con éxito')
                record= cursor.fetchall()
                print(record)

            elif(self.comboBox_OpcionesCambioCanciones.currentIndex()==7):
                params = config()
                conn = bd.connect(**params)
                cursor = conn.cursor()
                query = """
                    UPDATE track
                    SET milliseconds = %s, last_modified_by= %s
                    WHERE name = %s
                    RETURNING trackid , name
                """
                cursor.execute(query,(int(self.textEdit_CambioNuevo.toPlainText()),username,self.textEdit_CancionNombre.toPlainText()))
                conn.commit()
                self.openPopUpCheck('Se modifcó con éxito')
                record= cursor.fetchall()
                print(record)
        else:
            print("Debe llenar los campos")
            self.openPopUpError('Tiene que llenar todos los campos')

# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     HomeUserModificar = QtWidgets.QMainWindow()
#     ui = Ui_HomeUserModificar()
#     ui.setupUi(HomeUserModificar)
#     HomeUserModificar.show()
#     sys.exit(app.exec_())

                