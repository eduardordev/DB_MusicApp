import psycopg2 as bd
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.uic import loadUi
from RPDR import Ui_RPDR
#import pgdb as bd
from config import config


class Ui_PT(object):
    def __init__(self, id):
        super(Ui_PT, self).__init__()
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
        self.tableWidget.setGeometry(QtCore.QRect(460, 30, 400, 490))
        self.tableWidget.setStyleSheet("font: 18pt \"Times\";\n"
"color: #1b1c34;\n"
"background-color: #EDFEFB")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        
        self.textEdit_UserBuscar = QtWidgets.QTextEdit(self.frame)
        self.textEdit_UserBuscar.setGeometry(QtCore.QRect(20, 290, 231, 31))
        self.textEdit_UserBuscar.setMinimumSize(QtCore.QSize(410, 50))
        self.textEdit_UserBuscar.setMaximumSize(QtCore.QSize(410, 50))
        self.textEdit_UserBuscar.setStyleSheet("background-color: #FFFFFF;\n"
"font: 18pt \"Times\";\n"
"color: #000000;")
        self.textEdit_UserBuscar.setObjectName("textEdit_UserBuscar")
        

        self.pushButton_Buscar = QtWidgets.QPushButton(self.frame)
        self.pushButton_Buscar.setGeometry(QtCore.QRect(20, 350, 75, 31))
        self.pushButton_Buscar.setMinimumSize(QtCore.QSize(410, 50))
        self.pushButton_Buscar.setMaximumSize(QtCore.QSize(410, 50))
        self.pushButton_Buscar.setStyleSheet("background-color: #0ca692;\n"
"font: 20pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_Buscar.setObjectName("pushButton_Buscar")
        self.pushButton_Buscar.clicked.connect(self.populateTable)

        self.pushButton_AgregaCarrito = QtWidgets.QPushButton(self.frame)
        self.pushButton_AgregaCarrito.setGeometry(QtCore.QRect(20, 410, 150, 31))
        self.pushButton_AgregaCarrito.setMinimumSize(QtCore.QSize(410, 50))
        self.pushButton_AgregaCarrito.setMaximumSize(QtCore.QSize(410, 50))
        self.pushButton_AgregaCarrito.setStyleSheet("background-color: #0ca692;\n"
"font: 20pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_AgregaCarrito.setObjectName("pushButton_AgregaCarrito")
        self.pushButton_VerCarrito = QtWidgets.QPushButton(self.frame)
        self.pushButton_VerCarrito.setGeometry(QtCore.QRect(20, 470, 150, 31))
        self.pushButton_VerCarrito.setMinimumSize(QtCore.QSize(410, 50))
        self.pushButton_VerCarrito.setMaximumSize(QtCore.QSize(410, 50))
        self.pushButton_VerCarrito.setStyleSheet("background-color: #0ca692;\n"
"font: 20pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_VerCarrito.setObjectName("pushButton_VerCarrito")
        self.pushButton_VerCarrito.clicked.connect(self.openCarrito)
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(180, 180, 210, 50))
        self.label_8.setMinimumSize(QtCore.QSize(210, 50))
        self.label_8.setMaximumSize(QtCore.QSize(210, 50))
        self.label_8.setStyleSheet("font: 18pt \"Times\";\n"
"color: #FFFFFF;\n"
"")
        self.label_8.setObjectName("label_8")
        self.comboBox_OpcionesBuscar = QtWidgets.QComboBox(self.frame)
        self.comboBox_OpcionesBuscar.setGeometry(QtCore.QRect(20, 230, 220, 31))
        self.comboBox_OpcionesBuscar.setMinimumSize(QtCore.QSize(410, 50))
        self.comboBox_OpcionesBuscar.setMaximumSize(QtCore.QSize(410, 50))
        self.comboBox_OpcionesBuscar.setStyleSheet("background-color: #d1d1d5;\n"
"font: 14pt \"Times\";\n"
"color: rgb(0, 0, 0);")
        self.comboBox_OpcionesBuscar.setObjectName("comboBox_OpcionesBuscar")
        self.comboBox_OpcionesBuscar.addItem("")
        self.comboBox_OpcionesBuscar.addItem("")
        self.comboBox_OpcionesBuscar.addItem("")
        self.comboBox_OpcionesBuscar.addItem("")
        self.comboBox_OpcionesBuscar.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)

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
        self.pushButton_AgregaCarrito.setText(_translate("MainWindow", "Añadir a su playlist"))
        self.pushButton_AgregaCarrito.clicked.connect(self.addCarrito)
        self.pushButton_VerCarrito.setText(_translate("MainWindow", "Ver playlist"))
        self.label_8.setText(_translate("MainWindow", "Reproductor"))
        self.comboBox_OpcionesBuscar.setItemText(0, _translate("MainWindow", "¿Qué deseas buscar?"))
        self.comboBox_OpcionesBuscar.setItemText(1, _translate("MainWindow", "Artista"))
        self.comboBox_OpcionesBuscar.setItemText(2, _translate("MainWindow", "Género"))
        self.comboBox_OpcionesBuscar.setItemText(3, _translate("MainWindow", "Álbum"))
        self.comboBox_OpcionesBuscar.setItemText(4, _translate("MainWindow", "Canción"))

    def openPopUpError(self, mensaje):
        msgError = QMessageBox()
        msgError.setText(mensaje)
        msgError.setIcon(QMessageBox.Warning)
        x = msgError.exec_()

    def openCarrito(self, id):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_RPDR(self.id)
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

    def addCarrito(self):
        if(self.tableWidget.item(self.tableWidget.currentRow(),0)):
            userId = self.id
            originalName = self.tableWidget.item(self.tableWidget.currentRow(),0).text()
            try:
                params = config()
                conn = bd.connect(**params)
                cursor=conn.cursor()
                
                index = originalName.find("'")
                if(index > -1):
                    trackName = originalName[:index] + "'" + originalName[index:]
                else:
                    trackName=originalName

                cursor.execute("SELECT track.trackid, track.name FROM track WHERE track.name = \'"+str(trackName)+"\' and track.name NOT IN ( SELECT DISTINCT track.name FROM user_client JOIN invoice ON invoice.customerid = user_client.clientid JOIN invoiceline ON invoiceline.invoiceid = invoice.invoiceid JOIN track ON track.trackid = invoiceline.trackid WHERE user_client.clientid = \'"+str(userId)+"\')")
                record = cursor.fetchall()
                print(record)
                if(len(record)>0):
                    cursor.execute("SELECT trackid FROM track WHERE name = \'"+trackName+"\'")
                    trackId = cursor.fetchall()[0][0]
                    query= "INSERT INTO carrito(clientid, trackid,trackname, comprado) VALUES (%s,%s,%s,%s)"
                    datos = (userId,trackId,originalName,False)
                    cursor.execute(query,datos)
                    conn.commit()
                    self.openPopUpError("Se agregó la canción a su playlist")
                else:
                    self.openPopUpError('Ya agregó esta canción')
                    
            except(Exception) as error:
                print('Error:', error)
                self.openPopUpError('Ya agregó esta canción a su playlist')
        else:
            self.openPopUpError("No ha seleccionado ninguna canción")
            



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    PT = QtWidgets.QMainWindow()
    ui = Ui_PT()
    ui.setupUi(PT)
    PT.show()
    sys.exit(app.exec_())

