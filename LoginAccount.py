# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginAccount.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!

import psycopg2 as bd
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.uic import loadUi
from HomeAdmin import Ui_HomeAdmin
from CreateAccount import Ui_CreateAccount
from HomeUserAuto import Ui_HomeUserAuto
from HomeUser import Ui_HomeUser
#import pgdb as bd
from config import config

class Ui_LoginAccount(object):
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
        self.label.setGeometry(QtCore.QRect(210, 60, 195, 45))
        self.label.setMinimumSize(QtCore.QSize(195, 45))
        self.label.setMaximumSize(QtCore.QSize(195, 45))
        self.label.setStyleSheet("font: 24pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(50, 135, 240, 240))
        self.label_2.setMinimumSize(QtCore.QSize(240, 240))
        self.label_2.setMaximumSize(QtCore.QSize(240, 240))
        self.label_2.setStyleSheet("")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("logo.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(330, 135, 100, 25))
        self.label_3.setMinimumSize(QtCore.QSize(100, 25))
        self.label_3.setMaximumSize(QtCore.QSize(100, 25))
        self.label_3.setStyleSheet("font: 18pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label_3.setObjectName("label_3")
        self.textEdit_Username = QtWidgets.QTextEdit(self.frame)
        self.textEdit_Username.setGeometry(QtCore.QRect(330, 160, 220, 30))
        self.textEdit_Username.setMinimumSize(QtCore.QSize(220, 30))
        self.textEdit_Username.setMaximumSize(QtCore.QSize(220, 30))
        self.textEdit_Username.setStyleSheet("background-color: rgb(150, 172, 183);\n"
"color: rgb(255, 255, 255);\n"
"font: 13pt \"Times\";\n"
"border-radius: 12px;")
        self.textEdit_Username.setObjectName("textEdit_Username")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(330, 205, 110, 25))
        self.label_4.setMinimumSize(QtCore.QSize(110, 25))
        self.label_4.setMaximumSize(QtCore.QSize(110, 25))
        self.label_4.setStyleSheet("font: 18pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label_4.setObjectName("label_4")
        self.lineEdit_Password = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_Password.setGeometry(QtCore.QRect(330, 230, 220, 30))
        self.lineEdit_Password.setMinimumSize(QtCore.QSize(220, 0))
        self.lineEdit_Password.setMaximumSize(QtCore.QSize(220, 16777215))
        self.lineEdit_Password.setStyleSheet("background-color: rgb(150, 172, 183);\n"
"color: rgb(255, 255, 255);\n"
"font: 13pt \"Times\";")
        self.lineEdit_Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_Password.setObjectName("lineEdit")
        self.pushButton_Login = QtWidgets.QPushButton(self.frame)
        self.pushButton_Login.setGeometry(QtCore.QRect(385, 283, 114, 32))
        self.pushButton_Login.setMinimumSize(QtCore.QSize(114, 32))
        self.pushButton_Login.setMaximumSize(QtCore.QSize(114, 32))
        self.pushButton_Login.setStyleSheet("background-color: rgb(10, 54, 157);\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 12px;")
        self.pushButton_Login.setObjectName("pushButton_Login")
        self.pushButton_Login.clicked.connect(self.getLogin)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(440, 320, 60, 16))
        self.label_5.setMinimumSize(QtCore.QSize(60, 16))
        self.label_5.setMaximumSize(QtCore.QSize(60, 16))
        self.label_5.setStyleSheet("font: 18pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label_5.setObjectName("label_5")
        self.pushButton_CreateAccount = QtWidgets.QPushButton(self.frame)
        self.pushButton_CreateAccount.setGeometry(QtCore.QRect(360, 340, 165, 32))
        self.pushButton_CreateAccount.setMinimumSize(QtCore.QSize(165, 32))
        self.pushButton_CreateAccount.setMaximumSize(QtCore.QSize(165, 32))
        self.pushButton_CreateAccount.setStyleSheet("background-color: rgb(10, 54, 157);\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 12px;")
        self.pushButton_CreateAccount.setObjectName("pushButton_CreateAccount")
        self.pushButton_CreateAccount.clicked.connect(self.openCreateAccount)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Member Login"))
        self.label_3.setText(_translate("MainWindow", "Username"))
        self.textEdit_Username.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.SF NS Text\';\"><br /></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "Contraseña"))
        self.pushButton_Login.setText(_translate("MainWindow", "Login"))
        self.label_5.setText(_translate("MainWindow", "o"))
        self.pushButton_CreateAccount.setText(_translate("MainWindow", "Crear cuenta"))

    def openPopUpError(self, mensaje):
        msgError = QMessageBox()
        msgError.setText(mensaje)
        msgError.setIcon(QMessageBox.Warning)
        x = msgError.exec_()

    def openPopUpCheck(self,mensaje):
        msgGood = QMessageBox()
        msgGood.setText(mensaje)
        msgGood.setIcon(QMessageBox.Information)
        y = msgGood.exec_()


    def openHomeAdmin(self, id):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_HomeAdmin(id)
        self.ui.setupUi(self.window)
        LoginAccount.hide()
        self.window.show()


    def openCreateAccount(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_CreateAccount()
        self.ui.setupUi(self.window)
        LoginAccount.hide()
        self.window.show()

    def openHomeUserAuto(self, id):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_HomeUserAuto(id)
        self.ui.setupUi(self.window)
        LoginAccount.hide()
        self.window.show()

    def openHomeUser(self, id):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_HomeUser(id)
        self.ui.setupUi(self.window)
        LoginAccount.hide()
        self.window.show()

    def getLogin(self):
        conn=None
        try:
                params = config()
                conn = bd.connect(**params)
                cursor = conn.cursor()
                usuario = self.textEdit_Username.toPlainText()
                contrasena = self.lineEdit_Password.text()
                query = """
                        SELECT usr, pw, type, ide FROM
                                (SELECT username as usr, password as pw, usertype as type , clientid as ide FROM user_client  
                                        UNION 
                                SELECT username as usr, password as pw, usertype as type , employeeid as ide FROM employee )Q 
                                
                        WHERE usr = \'""" + usuario + """\' 
                                AND pw = \'""" + contrasena + """\'
"""
                cursor.execute(query)
                record = cursor.fetchall()
                print(record)
                if(len(record) != 0):
                        if (record[0][2] == 0):
                                self.openHomeAdmin(record[0][3])
                        elif (record[0][2] == 1 ):
                                self.openHomeUserAuto(record[0][3])
                        else:
                                self.openHomeUser(record[0][3])
                else:
                        print("error in loging")
                        self.openPopUpError("Usuario o contraseña incorrecto")
        except (Exception) as error:
                print("Error", error)
        finally:
                if(conn):
                        cursor.close()
                        conn.close()

    


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    LoginAccount = QtWidgets.QMainWindow()
    ui = Ui_LoginAccount()
    ui.setupUi(LoginAccount)
    LoginAccount.show()
    sys.exit(app.exec_())
