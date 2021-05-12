import sys
import psycopg2 as bd
import os
import csv
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from PyQt5.QtGui import QImage, QPainter
from PyQt5.QtCore import QFile, QDir
from HomeUserInactivarEliminar import Ui_HomeUserInactivarEliminar
from HomeUserModificar import Ui_HomeUserModificar
from PT import Ui_PT
from HomeAdminReporteria import Ui_HomeAdminReporteria
from HomeUserRegistrar import Ui_HomeUserRegistrar
from HomeAdminGestionPermisos import Ui_HomeAdminGestionPermisos
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
        MainWindow.setStyleSheet("background-color: #d1d1d5;")


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(50, 50, 900, 550))
        self.frame.setMinimumSize(QtCore.QSize(900, 550))
        self.frame.setMaximumSize(QtCore.QSize(900, 550))
        self.frame.setStyleSheet("background-color: #1c1d32;\n"
        "border-radius: 5px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")


        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(180, 5, 100, 100))
        self.label_2.setMinimumSize(QtCore.QSize(140, 140))
        self.label_2.setMaximumSize(QtCore.QSize(140, 140))
        self.label_2.setStyleSheet("")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("musics.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_2.setObjectName("label_2")

        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(470, 177, 400, 350))
        self.tableWidget.setStyleSheet("font: 14pt \"Times\";\n"
        "color: #1b1c34;\n"
        "background-color: #EDFEFB")
        self.tableWidget.setObjectName("tableWidget")



        self.pushButton_Exit = QtWidgets.QPushButton(self.frame)
        self.pushButton_Exit.setGeometry(QtCore.QRect(750, 30, 15, 15))
        self.pushButton_Exit.setMinimumSize(QtCore.QSize(120, 40))
        self.pushButton_Exit.setMaximumSize(QtCore.QSize(120, 40))
        self.pushButton_Exit.setStyleSheet("background-color: #0ca692;\n"
        "font: 14pt \"Times\";\n"
        "color: rgb(255, 255, 255);\n"
        "border-radius: 5px;")
        self.pushButton_Exit.setObjectName("pushButton_Exit")
        self.pushButton_Exit.clicked.connect(QtCore.QCoreApplication.instance().quit)


        self.textEdit_UserBuscar = QtWidgets.QTextEdit(self.frame)
        self.textEdit_UserBuscar.setGeometry(QtCore.QRect(470, 130, 240, 25))
        self.textEdit_UserBuscar.setMinimumSize(QtCore.QSize(270, 40))
        self.textEdit_UserBuscar.setMaximumSize(QtCore.QSize(270, 40))
        self.textEdit_UserBuscar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "font: 18pt \"Times\";\n"
        "color: rgb(0, 0, 0);\n"
        "border-radius: 5px;")
        self.textEdit_UserBuscar.setObjectName("textEdit_UserBuscar")


        self.pushButton_Registro = QtWidgets.QPushButton(self.frame)
        self.pushButton_Registro.setGeometry(QtCore.QRect(80, 420, 100, 30))
        self.pushButton_Registro.setMinimumSize(QtCore.QSize(350, 50))
        self.pushButton_Registro.setMaximumSize(QtCore.QSize(350, 50))
        self.pushButton_Registro.setStyleSheet("background-color: #0ca692;\n"
        "font: 14pt \"Times\";\n"
        "color: rgb(255, 255, 255);\n"
        "border-radius: 5px;")
        self.pushButton_Registro.setObjectName("pushButton_Registro")
        self.pushButton_Registro.clicked.connect(self.openHomeUserRegistrar)



        self.pushButton_Inactivar = QtWidgets.QPushButton(self.frame)
        self.pushButton_Inactivar.setGeometry(QtCore.QRect(80, 365, 10, 30))
        self.pushButton_Inactivar.setMinimumSize(QtCore.QSize(350, 50))
        self.pushButton_Inactivar.setMaximumSize(QtCore.QSize(350, 50))
        self.pushButton_Inactivar.setStyleSheet("background-color: #0ca692;\n"
        "font: 14pt \"Times\";\n"
        "color: rgb(255, 255, 255);\n"
        "border-radius: 5px;")
        self.pushButton_Inactivar.setObjectName("pushButton_Inactivar")
        self.pushButton_Inactivar.clicked.connect(self.openHomeUserModificar)



        self.pushButton_Modficiar = QtWidgets.QPushButton(self.frame)
        self.pushButton_Modficiar.setGeometry(QtCore.QRect(80, 200, 100, 30))
        self.pushButton_Modficiar.setMinimumSize(QtCore.QSize(350, 50))
        self.pushButton_Modficiar.setMaximumSize(QtCore.QSize(350, 50))
        self.pushButton_Modficiar.setStyleSheet("background-color: #0ca692;\n"
        "font: 14pt \"Times\";\n"
        "color: rgb(255, 255, 255);\n"
        "border-radius: 5px;")
        self.pushButton_Modficiar.setObjectName("pushButton_Modficiar")
        self.pushButton_Modficiar.clicked.connect(self.openHomeUserInactivarEliminar)



        self.pushButton_Reporteria = QtWidgets.QPushButton(self.frame)
        self.pushButton_Reporteria.setGeometry(QtCore.QRect(80, 145, 100, 30))
        self.pushButton_Reporteria.setMinimumSize(QtCore.QSize(350, 50))
        self.pushButton_Reporteria.setMaximumSize(QtCore.QSize(350, 50))
        self.pushButton_Reporteria.setStyleSheet("background-color: #0ca692;\n"
        "font: 14pt \"Times\";\n"
        "color: rgb(255, 255, 255);\n"
        "border-radius: 5px;")
        self.pushButton_Reporteria.setObjectName("pushButton_Reporteria")
        self.pushButton_Reporteria.clicked.connect(self.openHomeAdminReporteria)



        self.comboBox_OpcionesBuscar = QtWidgets.QComboBox(self.frame)
        self.comboBox_OpcionesBuscar.setGeometry(QtCore.QRect(470, 80, 175, 30))
        self.comboBox_OpcionesBuscar.setMinimumSize(QtCore.QSize(400, 40))
        self.comboBox_OpcionesBuscar.setMaximumSize(QtCore.QSize(400, 40))
        self.comboBox_OpcionesBuscar.setStyleSheet("background-color: #d1d1d5;\n"
        "font: 14pt \"Times\";\n"
        "color: rgb(0, 0, 0);\n"
        "border-radius: 5px;")
        self.comboBox_OpcionesBuscar.setObjectName("comboBox_OpcionesBuscar")
        self.comboBox_OpcionesBuscar.addItem("")
        self.comboBox_OpcionesBuscar.addItem("")
        self.comboBox_OpcionesBuscar.addItem("")
        self.comboBox_OpcionesBuscar.addItem("")
        self.comboBox_OpcionesBuscar.addItem("")



        self.pushButton_Buscar = QtWidgets.QPushButton(self.frame)
        self.pushButton_Buscar.setGeometry(QtCore.QRect(750, 130, 110, 25))
        self.pushButton_Buscar.setMinimumSize(QtCore.QSize(120, 40))
        self.pushButton_Buscar.setMaximumSize(QtCore.QSize(120, 40))
        self.pushButton_Buscar.setStyleSheet("background-color: #0ca692;\n"
        "font: 14pt \"Times\";\n"
        "color: rgb(255, 255, 255);\n"
        "border-radius: 5px;")



        self.pushButton_GestionPermisos = QtWidgets.QPushButton(self.frame)
        self.pushButton_GestionPermisos.setGeometry(QtCore.QRect(80, 255, 100, 30))
        self.pushButton_GestionPermisos.setMinimumSize(QtCore.QSize(350, 50))
        self.pushButton_GestionPermisos.setMaximumSize(QtCore.QSize(350, 50))
        self.pushButton_GestionPermisos.setStyleSheet("background-color: #0ca692;\n"
        "font: 14pt \"Times\";\n"
        "color: rgb(255, 255, 255);\n"
        "border-radius: 5px;")
        self.pushButton_GestionPermisos.setObjectName("pushButton_Registro_2")
        self.pushButton_GestionPermisos.clicked.connect(self.openHomeAdminGestionPermisos)



        self.pushButton_Reproductor = QtWidgets.QPushButton(self.frame)
        self.pushButton_Reproductor.setGeometry(QtCore.QRect(610, 30, 114, 32))
        self.pushButton_Reproductor.setMinimumSize(QtCore.QSize(130, 40))
        self.pushButton_Reproductor.setMaximumSize(QtCore.QSize(130, 40))
        self.pushButton_Reproductor.setStyleSheet("background-color: #0ca692;\n"
        "font: 14pt \"Times\";\n"
        "color: rgb(255, 255, 255);")
        self.pushButton_Reproductor.setObjectName("pushButton_Reproductor")





        self.pushButton_Bitacora = QtWidgets.QPushButton(self.frame)
        self.pushButton_Bitacora.setGeometry(QtCore.QRect(80, 310, 100, 30))
        self.pushButton_Bitacora.setMinimumSize(QtCore.QSize(350, 50))
        self.pushButton_Bitacora.setMaximumSize(QtCore.QSize(350, 50))
        self.pushButton_Bitacora.setStyleSheet("background-color: #0ca692;\n"
        "font: 14pt \"Times\";\n"
        "color: rgb(255, 255, 255);\n"
        "border-radius: 5px;")
        self.pushButton_Bitacora.setObjectName("pushButton_Bitacora")




        self.comboBox_OpcionesBuscar.raise_()
        self.label_2.raise_()
        self.tableWidget.raise_()
        self.pushButton_Exit.raise_()
        self.textEdit_UserBuscar.raise_()
        self.pushButton_Registro.raise_()
        self.pushButton_Inactivar.raise_()
        self.pushButton_Modficiar.raise_()
        self.pushButton_Buscar.raise_()
        self.pushButton_GestionPermisos.raise_()
        self.pushButton_Reproductor.raise_()
        self.pushButton_Reproductor.clicked.connect(self.openReproductor)
        self.pushButton_Bitacora.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))




        self.pushButton_Exit.setText(_translate("MainWindow", "Salir"))
        self.textEdit_UserBuscar.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_Registro.setText(_translate("MainWindow", "Registro"))
        self.pushButton_Inactivar.setText(_translate("MainWindow", "Modificación"))
        self.pushButton_Modficiar.setText(_translate("MainWindow", "Inactivación/Eliminación"))
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
        self.pushButton_Reproductor.setText(_translate("MainWindow", "Reproductor"))
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

    def openReproductor(self, id):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_PT(self.id)
        self.ui.setupUi(self.window)
        self.window.show()

    def openBitacora(self, id):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Bitacora(self.id)
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

