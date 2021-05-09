# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Simulacion.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!

import sys
import psycopg2 as bd
from PyQt5 import QtCore, QtGui, QtWidgets
from config import config
from datetime import datetime
import random
from HomeAdminReporteria import Ui_HomeAdminReporteria
from PyQt5.QtWidgets import QMessageBox




class Ui_Simulacion(object):
    def __init__(self, id):
        super(Ui_Simulacion, self).__init__()
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
#         self.tableWidget = QtWidgets.QTableWidget(self.frame)
#         self.tableWidget.setGeometry(QtCore.QRect(30, 310, 841, 211))
#         self.tableWidget.setStyleSheet("font: 13pt \"Times\";\n"
# "color: rgb(64, 55, 110);\n"
# "background-color: rgb(212, 228, 188);")
#         self.tableWidget.setObjectName("tableWidget")
#         self.tableWidget.setColumnCount(0)
#         self.tableWidget.setRowCount(0)
        self.pushButton_Buscar = QtWidgets.QPushButton(self.frame)
        self.pushButton_Buscar.setGeometry(QtCore.QRect(180, 220, 75, 31))
        self.pushButton_Buscar.setMinimumSize(QtCore.QSize(75, 31))
        self.pushButton_Buscar.setMaximumSize(QtCore.QSize(75, 31))
        self.pushButton_Buscar.setStyleSheet("background-color: rgb(10, 54, 157);\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_Buscar.setObjectName("pushButton_Buscar")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(30, 120, 210, 50))
        self.label_8.setMinimumSize(QtCore.QSize(210, 50))
        self.label_8.setMaximumSize(QtCore.QSize(210, 50))
        self.label_8.setStyleSheet("font: 22pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label_8.setObjectName("label_8")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.frame)
        self.calendarWidget.setGeometry(QtCore.QRect(559, 120, 312, 173))
        self.calendarWidget.setObjectName("calendarWidget")
        self.calendarWidget.clicked[QtCore.QDate].connect(lambda arg : self.set_date(arg.toString('yyyy-MM-dd')))
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(30, 190, 300, 25))
        self.label_7.setMinimumSize(QtCore.QSize(300, 25))
        self.label_7.setMaximumSize(QtCore.QSize(300, 25))
        self.label_7.setStyleSheet("font: 18pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label_7.setObjectName("label_7")
        self.textEdit_UserBuscar = QtWidgets.QTextEdit(self.frame)
        self.textEdit_UserBuscar.setGeometry(QtCore.QRect(30, 220, 150, 31))
        self.textEdit_UserBuscar.setMinimumSize(QtCore.QSize(150, 31))
        self.textEdit_UserBuscar.setMaximumSize(QtCore.QSize(150, 31))
        self.textEdit_UserBuscar.setStyleSheet("background-color: rgb(150, 172, 183);\n"
"font: 13pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.textEdit_UserBuscar.setObjectName("textEdit_UserBuscar")
        self.pushButton_IrReporteria = QtWidgets.QPushButton(self.frame)
        self.pushButton_IrReporteria.setGeometry(QtCore.QRect(770, 50, 100, 30))
        self.pushButton_IrReporteria.setMinimumSize(QtCore.QSize(100, 30))
        self.pushButton_IrReporteria.setMaximumSize(QtCore.QSize(100, 30))
        self.pushButton_IrReporteria.setStyleSheet("background-color: rgb(10, 54, 157);\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_IrReporteria.setObjectName("pushButton_IrReporteria")
        MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton_IrReporteria.clicked.connect(self.openReporteria)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Sonido Cloud "))
        self.pushButton_Buscar.setText(_translate("MainWindow", "Simular"))
        self.label_8.setText(_translate("MainWindow", "Simulación"))
        self.label_7.setText(_translate("MainWindow", "Número de canciones a simular"))
        self.textEdit_UserBuscar.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_IrReporteria.setText(_translate("MainWindow", "Reportería"))
        self.pushButton_Buscar.clicked.connect(self.simular)

    def set_date (self, newDate) : 
        self.DATE = newDate
        return self.DATE == newDate

    def openReporteria (self):
        self.window = QtWidgets.QMainWindow()
        self.ui= Ui_HomeAdminReporteria()
        self.ui.setupUi(self.window)
        self.window.show()

    def openPopUpError(self, mensaje):
        msgError = QMessageBox()
        msgError.setText(mensaje)
        msgError.setIcon(QMessageBox.Warning)
        x = msgError.exec_()

    def simular(self):
        try:
            print(self.DATE)
            fecha =self.DATE
            cantidad = self.textEdit_UserBuscar.toPlainText()
            cantidad = int(cantidad)

            params = config()
            conn = bd.connect(**params)
            cursor = conn.cursor()

            cursor.execute("SELECT MAX(trackid) FROM track ")
            maxCancionId = cursor.fetchall()[0][0]
            cursor.execute("SELECT MAX(clientid) FROM user_client")
            maxUserId = cursor.fetchall()[0][0]

            cursor.execute("SELECT MAX(invoiceid) from invoice")
            invoiceId = cursor.fetchall()[0][0]+1
            cursor.execute("SELECT MAX(invoicelineid) FROM invoiceline")
            invoicelineId = cursor.fetchall()[0][0]+1

            totalRep=0
            totalComp=0

            for i in range(cantidad):
                user = random.randint(1,maxUserId)
                print(user)
                query="""SELECT track.trackid, track.name FROM track 
                                    JOIN invoiceline on invoiceline.trackid = track.trackid
                                    JOIN invoice on invoice.invoiceid = invoiceline.invoiceid
                                    JOIN user_client on user_client.clientid = invoice.customerid
                                    where invoice.customerid = %(id)s"""
                data= {
                    'id':user
                }
                cursor.execute(query,data)
                record=cursor.fetchall()
                if(len(record)>0):
                    for j in range(random.randint(1,cantidad+1)):
                        cancionKey = random.randint(0,len(record)-1)
                        cancion = record[cancionKey][1]
                        print('rep',cancion,user)
                        query2 = "INSERT INTO reproducciones(clientid, trackname, fecha) VALUES (%s,%s,%s)"
                        datos=(str(user),cancion,fecha)
                        cursor.execute(query2,datos)
                        conn.commit()
                        totalRep+=1

            for i in range(cantidad):
                user = random.randint(1,maxUserId)
                print(user)
                total = cantidad*0.99
                query = "INSERT INTO invoice(invoiceid, customerid, invoicedate, total) VALUES (%s,%s,%s,%s)"
                datos = (invoiceId, user, fecha, total )
                cursor.execute(query, datos)
                print(invoiceId)
                
                for j in range(cantidad):
                    trackId = random.randint(1,maxCancionId)
                    query2= "INSERT INTO invoiceline(invoicelineid, invoiceid, trackid, unitprice, quantity) VALUES (%s,%s,%s,%s,%s)"
                    data = (invoicelineId, invoiceId, trackId, 0.99, 1)
                    cursor.execute(query2, data)
                    print('compra',trackId, invoiceId)
                    invoicelineId +=1
                    totalComp+=1
                invoiceId+=1
            conn.commit()
            self.openPopUpError('Simulacion exitosa:'+str(totalRep)+' reproducciones y '+str(totalComp)+' compras')


        except(Exception) as error:
            print(error)
            self.openPopUpError('Error en la simulacion')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Simulacion = QtWidgets.QMainWindow()
    ui = Ui_Simulacion()
    ui.setupUi(Simulacion)
    Simulacion.show()
    sys.exit(app.exec_())

