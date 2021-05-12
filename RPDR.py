import sys
import psycopg2 as bd
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.uic import loadUi
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from config import config
from fpdf import FPDF

class Ui_RPDR(object):
    def __init__(self, id):
        super(Ui_RPDR, self).__init__()
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
        self.label_2.setGeometry(QtCore.QRect(100, 10, 100, 100))
        self.label_2.setMinimumSize(QtCore.QSize(225, 205))
        self.label_2.setMaximumSize(QtCore.QSize(225, 205))
        self.label_2.setStyleSheet("")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("musics.PNG"))
        self.label_2.setScaledContents(True)
        self.label_2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_2.setObjectName("label_2")


        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(460, 30, 400, 420))
        self.tableWidget.setStyleSheet("font: 18pt \"Times\";\n"
"color: #1b1c34;\n"
"background-color: #EDFEFB")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)


        self.textEdit_UserBuscar = QtWidgets.QTextEdit(self.frame)
        self.textEdit_UserBuscar.setGeometry(QtCore.QRect(20, 260, 231, 31))
        self.textEdit_UserBuscar.setMinimumSize(QtCore.QSize(410, 50))
        self.textEdit_UserBuscar.setMaximumSize(QtCore.QSize(410, 50))
        self.textEdit_UserBuscar.setStyleSheet("background-color: #ffffff;\n"
"font: 18pt \"Times\";\n"
"color: #000000;")
        self.textEdit_UserBuscar.setObjectName("textEdit_UserBuscar")
        

        self.pushButton_Buscar = QtWidgets.QPushButton(self.frame)
        self.pushButton_Buscar.setGeometry(QtCore.QRect(20, 330, 75, 31))
        self.pushButton_Buscar.setMinimumSize(QtCore.QSize(410, 50))
        self.pushButton_Buscar.setMaximumSize(QtCore.QSize(410, 50))
        self.pushButton_Buscar.setStyleSheet("background-color: #0ca692;\n"
"font: 18pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_Buscar.setObjectName("pushButton_Buscar")


        self.pushButton_Checkout = QtWidgets.QPushButton(self.frame)
        self.pushButton_Checkout.setGeometry(QtCore.QRect(460, 470, 150, 31))
        self.pushButton_Checkout.setMinimumSize(QtCore.QSize(400, 50))
        self.pushButton_Checkout.setMaximumSize(QtCore.QSize(400, 50))
        self.pushButton_Checkout.setStyleSheet("background-color: #0ca692;\n"
"font: 18pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_Checkout.setObjectName("pushButton_Checkout")


        self.pushButton_BorrarTodo = QtWidgets.QPushButton(self.frame)
        self.pushButton_BorrarTodo.setGeometry(QtCore.QRect(20, 470, 150, 31))
        self.pushButton_BorrarTodo.setMinimumSize(QtCore.QSize(410, 50))
        self.pushButton_BorrarTodo.setMaximumSize(QtCore.QSize(410, 50))
        self.pushButton_BorrarTodo.setStyleSheet("background-color: #0ca692;\n"
"font: 18pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_BorrarTodo.setObjectName("pushButton_BorrarTodo")


        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(120, 190, 210, 50))
        self.label_8.setMinimumSize(QtCore.QSize(300, 50))
        self.label_8.setMaximumSize(QtCore.QSize(300, 50))
        self.label_8.setStyleSheet("font: 18pt \"Times\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_8.setObjectName("label_8")


        self.pushButton_BorrarCancion = QtWidgets.QPushButton(self.frame)
        self.pushButton_BorrarCancion.setGeometry(QtCore.QRect(20, 400, 150, 31))
        self.pushButton_BorrarCancion.setMinimumSize(QtCore.QSize(410, 50))
        self.pushButton_BorrarCancion.setMaximumSize(QtCore.QSize(410, 50))
        self.pushButton_BorrarCancion.setStyleSheet("background-color: #0ca692;\n"
"font: 18pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_BorrarCancion.setObjectName("pushButton_BorrarCancion")
        self.pushButton_BorrarCancion.clicked.connect(self.deleteSong)


        self.pushButton_Checkout.clicked.connect(self.comprar)
        self.pushButton_BorrarTodo.clicked.connect(self.deleteAll)
        MainWindow.setCentralWidget(self.centralwidget)

        self.tableWidget.setRowCount(0)
        userId = self.id
        params = config()
        conn = bd.connect(**params)
        cursor = conn.cursor()
        query = "SELECT trackname FROM carrito WHERE comprado = false and clientid = \'"+str(userId)+"\'"
        cursor.execute(query)
        record = cursor.fetchall()
        if(len(record)!=0):
            self.tableWidget.setColumnCount(len(record[0]))
            for i in range(len(record)):
                self.tableWidget.insertRow(i)
                for j in range(len(record[0])):
                    self.tableWidget.setItem(i,j, QtWidgets.QTableWidgetItem(record[i][j]))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        
        self.textEdit_UserBuscar.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_Buscar.setText(_translate("MainWindow", "Buscar"))
        self.pushButton_Checkout.setText(_translate("MainWindow", "Reproducir"))
        self.pushButton_BorrarTodo.setText(_translate("MainWindow", "Borrar todo"))
        self.label_8.setText(_translate("MainWindow", "REPRODUCTOR 3.0"))
        self.pushButton_BorrarCancion.setText(_translate("MainWindow", "Borrar Canción"))

    
    def openPopUpError(self, mensaje):
        msgError = QMessageBox()
        msgError.setText(mensaje)
        msgError.setIcon(QMessageBox.Warning)
        x = msgError.exec_()
    
    def populateTable(self):
        self.tableWidget.setRowCount(0)
        userId = self.id
        params = config()
        conn = bd.connect(**params)
        cursor = conn.cursor()
        query = "SELECT trackname FROM carrito WHERE comprado = false and clientid = \'"+str(userId)+"\'"
        cursor.execute(query)
        record = cursor.fetchall()
        if(len(record)!=0):
            self.tableWidget.setColumnCount(len(record[0]))
            for i in range(len(record)):
                self.tableWidget.insertRow(i)
                for j in range(len(record[0])):
                    self.tableWidget.setItem(i,j, QtWidgets.QTableWidgetItem(record[i][j]))


    def deleteSong(self):
        if(self.tableWidget.item(self.tableWidget.currentRow(),0)):
            userId = self.id
            originalName = self.tableWidget.item(self.tableWidget.currentRow(),0).text()
            try:
                params = config()
                conn = bd.connect(**params)
                cursor = conn.cursor()

                index = originalName.find("'")
                if(index > -1):
                    trackName = originalName[:index] + "'" + originalName[index:]
                else:
                    trackName=originalName

                query = "DELETE FROM carrito WHERE trackname = \'"+str(trackName)+"\' and clientid = \'"+str(userId)+"\' and comprado = false"
                cursor.execute(query)
                conn.commit()
                self.populateTable()
                self.openPopUpError('Se borró la canción con éxito')
            except(Exception) as error:
                self.openPopUpError('No se pudo borrar la cancion')
        else:
            self.openPopUpError('No ha seleccionado ninguna cancion')

    
    def deleteAll(self):
        userId= self.id
        params = config()
        conn = bd.connect(**params)
        cursor = conn.cursor()

        cursor.execute("SELECT trackname FROM carrito WHERE comprado = false and clientid = \'"+str(userId)+"\'")
        record = cursor.fetchall()
        if(len(record)>0):
            try:
                query= "DELETE FROM carrito WHERE clientid = \'"+str(userId)+"\' and comprado = false"
                cursor.execute(query)
                conn.commit()
                self.populateTable()
            except(Exception) as error:
                self.openPopUpError('No se pudo borrar todo')
        else:
            self.openPopUpError('No tiene canciones en su playlist')

    def comprar(self):
        userId = self.id
        params = config()
        conn = bd.connect(**params)
        cursor = conn.cursor()

        cursor.execute("SELECT trackid, trackname FROM carrito WHERE comprado = false and clientid = \'"+str(userId)+"\'")
        canciones = cursor.fetchall()
        cursor.execute("SELECT MAX(invoiceid) from invoice")
        invoiceId = cursor.fetchall()[0][0]+1
        cursor.execute("SELECT MAX(invoicelineid) FROM invoiceline")
        invoicelineId = cursor.fetchall()[0][0]+1

        total = len(canciones) * 0.99
        if(len(canciones)>0):
            try:

                query = "INSERT INTO invoice(invoiceid, customerid, invoicedate, total) VALUES (%s,%s,%s,%s)"
                datos = (invoiceId, userId, datetime.date(datetime.now()), total )
                cursor.execute(query, datos)
                for i in range(len(canciones)):
                    trackId = canciones[i][0]
                    query2= "INSERT INTO invoiceline(invoicelineid, invoiceid, trackid, unitprice, quantity) VALUES (%s,%s,%s,%s,%s)"
                    data = (invoicelineId, invoiceId, trackId, 0.99, 1)
                    cursor.execute(query2, data)
                    invoicelineId +=1
                conn.commit()
                self.deleteAll()
                self.openPopUpError('Reproduciendo')
            except(Exception) as error:
                print(error)
                self.openPopUpError('No se pudo reproducir')
        else:
            self.openPopUpError('No tiene canciones en su playlist')



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    RPDR = QtWidgets.QMainWindow()
    ui = Ui_RPDR()
    ui.setupUi(RPDR)
    RPDR.show()
    sys.exit(app.exec_())

