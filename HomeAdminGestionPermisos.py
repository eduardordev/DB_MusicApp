import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
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
        MainWindow.setStyleSheet("background-color:  #d1d1d5;")


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(50, 50, 900, 550))
        self.frame.setMinimumSize(QtCore.QSize(900, 550))
        self.frame.setMaximumSize(QtCore.QSize(900, 550))
        self.frame.setStyleSheet("background-color:  #1c1d32;\n"
"border-radius:5px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")


        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(100, 20, 100, 100))
        self.label_2.setMinimumSize(QtCore.QSize(225, 205))
        self.label_2.setMaximumSize(QtCore.QSize(225, 205))
        self.label_2.setStyleSheet("")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("musics.PNG"))
        self.label_2.setScaledContents(True)
        self.label_2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_2.setObjectName("label_2")


        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(440, 60, 410, 460))
        self.tableWidget.setStyleSheet("font: 14pt \"Times\";\n"
        "color: #1b1c34;\n"
        "background-color: #EDFEFB")
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
     


        self.textEdit_UserBuscar = QtWidgets.QTextEdit(self.frame)
        self.textEdit_UserBuscar.setGeometry(QtCore.QRect(40, 300, 280, 31))
        self.textEdit_UserBuscar.setStyleSheet("background-color: #ffffff;\n"
"font: 13pt \"Times\";\n"
"color: #000000;")
        self.textEdit_UserBuscar.setObjectName("textEdit_UserBuscar")


        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(120, 220, 210, 25))
        self.label_8.setMinimumSize(QtCore.QSize(210, 25))
        self.label_8.setMaximumSize(QtCore.QSize(210, 25))
        self.label_8.setStyleSheet("font: 16pt \"Times\";\n"
"color: #ffffff;\n"
"")
        self.label_8.setObjectName("label_8")


        self.comboBox_OpcionesBuscar = QtWidgets.QComboBox(self.frame)
        self.comboBox_OpcionesBuscar.setGeometry(QtCore.QRect(40, 260, 280, 31))
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
        self.comboBox_OpcionesBuscar.addItem("")


        self.pushButton_Buscar = QtWidgets.QPushButton(self.frame)
        self.pushButton_Buscar.setGeometry(QtCore.QRect(330, 300, 80, 31))
        self.pushButton_Buscar.setMinimumSize(QtCore.QSize(80, 30))
        self.pushButton_Buscar.setMaximumSize(QtCore.QSize(80, 30))
        self.pushButton_Buscar.setStyleSheet("background-color: #0ca692;\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_Buscar.setObjectName("pushButton_Buscar")
        self.pushButton_Buscar.clicked.connect(self.populateTable)


        self.pushButton_Cambiar = QtWidgets.QPushButton(self.frame)
        self.pushButton_Cambiar.setGeometry(QtCore.QRect(330, 260, 80, 31))
        self.pushButton_Cambiar.setMinimumSize(QtCore.QSize(80, 30))
        self.pushButton_Cambiar.setMaximumSize(QtCore.QSize(80, 30))
        self.pushButton_Cambiar.setStyleSheet("background-color: #0ca692;\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_Cambiar.setObjectName("pushButton_Cambiar")
        self.pushButton_Cambiar.clicked.connect(self.changePermision)


        self.label_8.raise_()
        self.label_2.raise_()
        self.tableWidget.raise_()
        #self.pushButton_Exit.raise_()
        self.textEdit_UserBuscar.raise_()
        self.comboBox_OpcionesBuscar.raise_()
        self.pushButton_Buscar.raise_()
        self.pushButton_Cambiar.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Usuario"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nivel de permiso"))
        item = self.tableWidget.verticalHeaderItem(2)
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
        self.comboBox_OpcionesBuscar.setItemText(4, _translate("MainWindow", "3"))
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
