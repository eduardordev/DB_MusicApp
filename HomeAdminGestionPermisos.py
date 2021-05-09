# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HomeAdminGestionPermisos.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
#import pgdb as bd
import psycopg2 as bd
from config import config

class Ui_HomeAdminGestionPermisos(object):
    def __init__(self, id):
        super(Ui_HomeAdminGestionPermisos, self).__init__()
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
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(30, 230, 841, 281))
        self.tableWidget.setStyleSheet("font: 13pt \"Times\";\n"
"color: rgb(64, 55, 110);\n"
"background-color: rgb(212, 228, 188);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
#         self.pushButton_Exit = QtWidgets.QPushButton(self.frame)
#         self.pushButton_Exit.setGeometry(QtCore.QRect(756, 50, 114, 32))
#         self.pushButton_Exit.setMinimumSize(QtCore.QSize(114, 32))
#         self.pushButton_Exit.setMaximumSize(QtCore.QSize(114, 32))
#         self.pushButton_Exit.setStyleSheet("background-color: rgb(10, 54, 157);\n"
# "font: 14pt \"Times\";\n"
# "color: rgb(255, 255, 255);")
#         self.pushButton_Exit.setObjectName("pushButton_Exit")
        self.textEdit_UserBuscar = QtWidgets.QTextEdit(self.frame)
        self.textEdit_UserBuscar.setGeometry(QtCore.QRect(560, 200, 231, 31))
        self.textEdit_UserBuscar.setStyleSheet("background-color: rgb(150, 172, 183);\n"
"font: 13pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.textEdit_UserBuscar.setObjectName("textEdit_UserBuscar")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(529, 199, 31, 31))
        self.label_4.setStyleSheet("")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("finder.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(30, 130, 210, 25))
        self.label_8.setMinimumSize(QtCore.QSize(210, 25))
        self.label_8.setMaximumSize(QtCore.QSize(210, 25))
        self.label_8.setStyleSheet("font: 18pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label_8.setObjectName("label_8")
        self.comboBox_OpcionesBuscar = QtWidgets.QComboBox(self.frame)
        self.comboBox_OpcionesBuscar.setGeometry(QtCore.QRect(30, 160, 280, 31))
        self.comboBox_OpcionesBuscar.setMinimumSize(QtCore.QSize(280, 31))
        self.comboBox_OpcionesBuscar.setMaximumSize(QtCore.QSize(181, 31))
        self.comboBox_OpcionesBuscar.setStyleSheet("background-color: rgb(150, 172, 183);\n"
"font: 13pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.comboBox_OpcionesBuscar.setObjectName("comboBox_OpcionesBuscar")
        self.comboBox_OpcionesBuscar.addItem("")
        self.comboBox_OpcionesBuscar.addItem("")
        self.comboBox_OpcionesBuscar.addItem("")
        self.comboBox_OpcionesBuscar.addItem("")
        self.pushButton_Buscar = QtWidgets.QPushButton(self.frame)
        self.pushButton_Buscar.setGeometry(QtCore.QRect(791, 200, 80, 31))
        self.pushButton_Buscar.setMinimumSize(QtCore.QSize(80, 31))
        self.pushButton_Buscar.setMaximumSize(QtCore.QSize(80, 31))
        self.pushButton_Buscar.setStyleSheet("background-color: rgb(10, 54, 157);\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_Buscar.setObjectName("pushButton_Buscar")
        self.pushButton_Buscar.clicked.connect(self.populateTable)
        self.pushButton_Cambiar = QtWidgets.QPushButton(self.frame)
        self.pushButton_Cambiar.setGeometry(QtCore.QRect(310, 160, 80, 31))
        self.pushButton_Cambiar.setMinimumSize(QtCore.QSize(80, 31))
        self.pushButton_Cambiar.setMaximumSize(QtCore.QSize(80, 31))
        self.pushButton_Cambiar.setStyleSheet("background-color: rgb(10, 54, 157);\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_Cambiar.setObjectName("pushButton_Cambiar")
        self.pushButton_Cambiar.clicked.connect(self.changePermision)
        self.label_8.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.tableWidget.raise_()
        #self.pushButton_Exit.raise_()
        self.textEdit_UserBuscar.raise_()
        self.label_4.raise_()
        self.comboBox_OpcionesBuscar.raise_()
        self.pushButton_Buscar.raise_()
        self.pushButton_Cambiar.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Sonido Cloud "))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Usuario"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nivel de permiso"))
        item = self.tableWidget.verticalHeaderItem(2)
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
        # #self.pushButton_Exit.setText(_translate("MainWindow", "Salir"))
        self.textEdit_UserBuscar.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "Gestión de Permisos"))
        self.comboBox_OpcionesBuscar.setItemText(0, _translate("MainWindow", "¿Qué número de permiso deseas autorizar?"))
        self.comboBox_OpcionesBuscar.setItemText(1, _translate("MainWindow", "0"))
        self.comboBox_OpcionesBuscar.setItemText(2, _translate("MainWindow", "1"))
        self.comboBox_OpcionesBuscar.setItemText(3, _translate("MainWindow", "2"))
        self.pushButton_Buscar.setText(_translate("MainWindow", "Buscar"))
        self.pushButton_Cambiar.setText(_translate("MainWindow", "Cambiar"))

    def openPopUpError(self, mensaje):
        msgError = QMessageBox()
        msgError.setText(mensaje)
        msgError.setIcon(QMessageBox.Warning)
        x = msgError.exec_()

    def openPopUpCheck(self):
        msgGood = QMessageBox()
        msgGood.setText("Aqui va una variable")
        msgGood.setIcon(QMessageBox.Information)
        y = msgGood.exec_()


    def populateTable(self):
        self.tableWidget.setRowCount(0)
        if(self.textEdit_UserBuscar.toPlainText()!=''):
            print('Bien')
            conn = None
            params =config()
            conn = bd.connect(**params)
            cursor = conn.cursor()
            query = "SELECT user_client.username, user_client.usertype FROM user_client WHERE user_client.username ~* \'" + self.textEdit_UserBuscar.toPlainText() +"'"
            cursor.execute(query)
            record = cursor.fetchall()
            print(record)
            if(len(record)!= 0):
                self.tableWidget.setColumnCount(len(record[0]))
                for i in range(len(record)):
                    self.tableWidget.insertRow(i)
                    for j in range(len(record[0])):
                        print(i,j)
                        self.tableWidget.setItem(i,j, QtWidgets.QTableWidgetItem(str(record[i][j])))

    def changePermision(self):
        permiso = self.comboBox_OpcionesBuscar.currentText()
        if(permiso != "¿Qué número de permiso deseas autorizar?"):
            try:
                usuario = self.tableWidget.item(self.tableWidget.currentRow(),0).text()
                print(usuario)
                params = config()
                conn = bd.connect(**params)
                cursor = conn.cursor()
                query = "UPDATE user_client SET usertype = \'"+permiso+"\' WHERE username = \'"+usuario+"\'"
                cursor.execute(query)
                conn.commit()
                if(permiso=="1"):
                    cursor.execute("SELECT artist.name FROM artist WHERE artist.name= \'"+usuario+"\'")
                    if(len(cursor.fetchall()) == 0):
                        cursor.execute("select username from user_client where clientid=\'"+str(self.id)+"\'")
                        username = cursor.fetchall()[0][0]
                        cursor.execute("SELECT artist.artistid FROM artist ORDER BY artist.artistid DESC LIMIT 1")
                        record = cursor.fetchall()
                        id=record[0][0] +1
                        cursor.execute("SELECT user_client.clientid FROM user_client WHERE user_client.username = \'"+usuario+"\'")
                        recordCustomerid = cursor.fetchall()
                        customerid = recordCustomerid[0][0]
                        sql="INSERT INTO artist(artistid, name, customerid, last_modified_by) VALUES (%s,%s,%s,%s)"
                        datos=(id,usuario,customerid,username)
                        cursor.execute(sql,datos)
                        conn.commit()
                    else:
                        print("Ya existe este artista")

            except(Exception) as error:
                print("Error",error)
        else:
            self.openPopUpError("Seleccione el permiso nuevo")
            print("Seleccione el permiso nuevo")


# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     HomeAdminGestionPermisos = QtWidgets.QMainWindow()
#     ui = Ui_HomeAdminGestionPermisos()
#     ui.setupUi(HomeAdminGestionPermisos)
#     HomeAdminGestionPermisos.show()
#     sys.exit(app.exec_())

