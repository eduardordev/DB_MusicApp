import psycopg2 as bd
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.uic import loadUi
#import pgdb as bd
from config import config

#for playing music
import urllib
import urllib.request
import urllib.parse
import re
import webbrowser

class Ui_MiMusica(object):
    def __init__(self, id):
        super(Ui_MiMusica, self).__init__()
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
        self.label_2.setGeometry(QtCore.QRect(100, 100, 100, 100))
        self.label_2.setMinimumSize(QtCore.QSize(225, 205))
        self.label_2.setMaximumSize(QtCore.QSize(225, 205))
        self.label_2.setStyleSheet("")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("musics.PNG"))
        self.label_2.setScaledContents(True)
        self.label_2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_2.setObjectName("label_2")
        
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(60, 350, 280, 25))
        self.label_7.setMinimumSize(QtCore.QSize(350, 25))
        self.label_7.setMaximumSize(QtCore.QSize(350, 25))
        self.label_7.setStyleSheet("font: 14pt \"Times\";\n"
"color: #ffffff;\n"
"")
        self.label_7.setObjectName("label_7")


        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(460, 30, 400, 490))
        self.tableWidget.setStyleSheet("font: 18pt \"Times\";\n"
"color: #1b1c34;\n"
"background-color: #EDFEFB;")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)


        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(150, 290, 210, 50))
        self.label_8.setMinimumSize(QtCore.QSize(210, 50))
        self.label_8.setMaximumSize(QtCore.QSize(210, 50))
        self.label_8.setStyleSheet("font: 22pt \"Times\";\n"
"color: #FFFFFF;\n"
"")
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #for music playing
        self.tableWidget.itemDoubleClicked.connect(self.playMusicOnClick)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_8.setText(_translate("MainWindow", "Mi Música"))
        self.label_7.setText(_translate("MainWindow", "Para reproducir doble click en la canción"))
        self.populateTable()

    def populateTable(self):
        #clear the table
        self.tableWidget.setRowCount(0)
        userId = self.id
        conn = None
        params =config()
        conn = bd.connect(**params)
        cursor = conn.cursor()
        query = """  SELECT t.name
                            FROM invoice i 
                            INNER JOIN invoiceline il on il.invoiceid = i.invoiceid 
                            INNER JOIN user_client u on u.clientid = i.customerid
                            INNER JOIN track t on t.trackid = il.trackid WHERE u.clientid = %(id)s 
                            
                            UNION

                            SELECT t.name
                            FROM track t 
                            INNER JOIN album a on a.albumid = t.trackid
                            INNER JOIN artist at on at.artistid = a.artistid
                            INNER JOIN user_client c on at.customerid = c.clientid
                            WHERE c.clientid =%(id2)s"""
        query_data = {
            'id': userId,
            'id2':userId
        }
        cursor.execute(query, query_data)
        record = cursor.fetchall()
        if(len(record)!= 0):
            self.tableWidget.setColumnCount(len(record[0]))
            for i in range(len(record)):
                self.tableWidget.insertRow(i)
                for j in range(len(record[0])):
                    self.tableWidget.setItem(i,j, QtWidgets.QTableWidgetItem(record[i][j]))
    
    def playMusicOnClick(self, item):
        query_string = urllib.parse.urlencode({"search_query" : item.data(0)})
        html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
        search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
        url ="http://www.youtube.com/watch?v=" + search_results[0]
        webbrowser.open(url)
        userId = self.id
        conn = None
        params =config()
        conn = bd.connect(**params)
        cursor = conn.cursor()
        query = """  INSERT INTO reproducciones VALUES( %(id)s, %(track)s) """
        query_data = {
            'id': userId,
            'track': item.data(0)
        }
        cursor.execute(query, query_data)
        conn.commit()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MiMusica = QtWidgets.QMainWindow()
    ui = Ui_MiMusica(id)
    ui.setupUi(MiMusica)
    MiMusica.show()
    sys.exit(app.exec_())
