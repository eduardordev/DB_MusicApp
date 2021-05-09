

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.uic import loadUi
from HomeUser import Ui_HomeUser
#import pgdb as db
import psycopg2 as db
from config import config


class Ui_CreateAccount(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 650)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 650))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 650))
        MainWindow.setStyleSheet("background-color: rgb(72,35,60);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(205, 100, 600, 450))
        self.frame.setMinimumSize(QtCore.QSize(600, 450))
        self.frame.setMaximumSize(QtCore.QSize(600, 450))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 12px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(205, 40, 205, 45))
        self.label.setMinimumSize(QtCore.QSize(205, 45))
        self.label.setMaximumSize(QtCore.QSize(205, 45))
        self.label.setStyleSheet("font: 24pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(50, 130, 240, 240))
        self.label_2.setMinimumSize(QtCore.QSize(240, 240))
        self.label_2.setMaximumSize(QtCore.QSize(240, 240))
        self.label_2.setStyleSheet("")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("logo.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(330, 120, 100, 25))
        self.label_3.setMinimumSize(QtCore.QSize(100, 25))
        self.label_3.setMaximumSize(QtCore.QSize(100, 25))
        self.label_3.setStyleSheet("font: 18pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label_3.setObjectName("label_3")
        self.textEdit_Username = QtWidgets.QTextEdit(self.frame)
        self.textEdit_Username.setGeometry(QtCore.QRect(330, 150, 220, 30))
        self.textEdit_Username.setMinimumSize(QtCore.QSize(220, 30))
        self.textEdit_Username.setMaximumSize(QtCore.QSize(220, 30))
        self.textEdit_Username.setStyleSheet("background-color: rgb(150, 172, 183);\n"
"font: 13pt \"Times\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 12px;")
        self.textEdit_Username.setObjectName("textEdit_Username")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(330, 190, 110, 25))
        self.label_4.setMinimumSize(QtCore.QSize(110, 25))
        self.label_4.setMaximumSize(QtCore.QSize(110, 25))
        self.label_4.setStyleSheet("font: 18pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label_4.setObjectName("label_4")
        self.lineEdit_Password = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_Password.setGeometry(QtCore.QRect(330, 220, 220, 30))
        self.lineEdit_Password.setMinimumSize(QtCore.QSize(220, 30))
        self.lineEdit_Password.setMaximumSize(QtCore.QSize(220, 30))
        self.lineEdit_Password.setStyleSheet("background-color: rgb(150, 172, 183);\n"
"color: rgb(255, 255, 255);\n"
"font: 13pt \"Times\";")
        self.lineEdit_Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_Password.setObjectName("lineEdit")
        self.pushButton_CreateAccount = QtWidgets.QPushButton(self.frame)
        self.pushButton_CreateAccount.setGeometry(QtCore.QRect(360, 350, 165, 32))
        self.pushButton_CreateAccount.setMinimumSize(QtCore.QSize(165, 32))
        self.pushButton_CreateAccount.setMaximumSize(QtCore.QSize(165, 32))
        self.pushButton_CreateAccount.setStyleSheet("background-color: rgb(10, 54, 157);\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 12px;")
        self.pushButton_CreateAccount.setObjectName("pushButton_CreateAccount")
        self.pushButton_CreateAccount.clicked.connect(self.createAccount)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(330, 260, 115, 25))
        self.label_5.setMinimumSize(QtCore.QSize(115, 25))
        self.label_5.setMaximumSize(QtCore.QSize(115, 25))
        self.label_5.setStyleSheet("font: 18pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label_5.setObjectName("label_5")
        self.comboBox_Suscripciones = QtWidgets.QComboBox(self.frame)
        self.comboBox_Suscripciones.setGeometry(QtCore.QRect(330, 290, 220, 30))
        self.comboBox_Suscripciones.setStyleSheet("background-color: rgb(150, 172, 183);\n"
"color: rgb(255, 255, 255);\n"
"font: 13pt \"Times\";")
        self.comboBox_Suscripciones.setObjectName("comboBox_Suscripciones")
        self.comboBox_Suscripciones.addItem("")
        self.comboBox_Suscripciones.addItem("")
        self.comboBox_Suscripciones.addItem("")
        self.comboBox_Suscripciones.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Create Account"))
        self.label_3.setText(_translate("MainWindow", "Username"))
        self.textEdit_Username.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.SF NS Text\';\"><br /></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "Contraseña"))
        self.pushButton_CreateAccount.setText(_translate("MainWindow", "Crear cuenta"))
        self.label_5.setText(_translate("MainWindow", "Suscripción"))
        self.comboBox_Suscripciones.setItemText(0, _translate("MainWindow", "Escoge una opción"))
        self.comboBox_Suscripciones.setItemText(1, _translate("MainWindow", "Mensual"))
        self.comboBox_Suscripciones.setItemText(2, _translate("MainWindow", "Semestral"))
        self.comboBox_Suscripciones.setItemText(3, _translate("MainWindow", "Anual"))

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


    def openHomeUser(self):
        self.window = QtWidgets.QMainWindow()
        self.window.close()
        self.ui = Ui_HomeUser()
        self.ui.setupUi(self.window)
        self.window.show()

    def createAccount(self):
        if (self.textEdit_Username.toPlainText()!='' and self.lineEdit_Password.text()!='' and self.comboBox_Suscripciones.currentText()!="Escoge una opción"):
            sus = self.comboBox_Suscripciones.currentText()
            conn = None
            params = config()
            conn = db.connect(**params)
            cursor = conn.cursor()
            cursor.execute("SELECT user_client.username FROM user_client WHERE user_client.username= \'"+self.textEdit_Username.toPlainText()+"\'")
            recordUsers= cursor.fetchall()
            cursor.execute("SELECT artist.name FROM artist WHERE artist.name= \'"+self.textEdit_Username.toPlainText()+"\'")
            recordArtistas= cursor.fetchall()            
            if(len(recordUsers) == 0 and len(recordArtistas)==0):
                cursor.execute("SELECT user_client.clientid FROM user_client ORDER BY user_client.clientid DESC LIMIT 1")
                record = cursor.fetchall()
                id=record[0][0] +1
                sql="INSERT INTO user_client(clientid, username, password, usertype,suscripcion) VALUES (%s,%s,%s,%s,%s)"
                datos=(id,self.textEdit_Username.toPlainText(),self.lineEdit_Password.text(),2,sus)
                cursor.execute(sql,datos)
                conn.commit()
                self.openHomeUser()
            else:
                print("El usuario ya existe o es igual al nombre de un cantante")
                self.openPopUpError("El usuario ya existe o es igual al nombre de un cantante")

        else:
            print("Tiene que ingresar un usuario y contraseña")
            self.openPopUpError("Tiene que ingresar un usuario, contraseña y elegir una opciond de suscripción")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    CreateAccount = QtWidgets.QMainWindow()
    ui = Ui_CreateAccount()
    ui.setupUi(CreateAccount)
    CreateAccount.show()
    sys.exit(app.exec_())







