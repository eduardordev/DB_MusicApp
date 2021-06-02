import psycopg2 as bd
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.uic import loadUi
#import pgdb as bd
from config import config
import pymongo
import datetime
MONGO_PORT = 'mongodb://localhost:27017'


class Ui_Mongo(object):
    # Esta es la confi basica, si quieren la pueden cambiar
    myClient = pymongo.MongoClient(MONGO_PORT)
    mydb = myClient['Instancia_Proyecto']
    clientes = mydb['client']
    compras = mydb['invoice']
    #BD vacia en mongo
    mydb.invoice.delete_many({})  # Esta es para las fechas
    mydb.customers.delete_many({})# Esta es para todos los clientes
    mydb.releases.delete_many({})  # Esta es para los ultimos releases
    mydb.usuariosrecomendados.delete_many({}) # En esta coleccion se almacenan las recomendaciones
    
    DEFAULT_FECHA = '2000/1/1'
    def convert(self, date_time):
        format = '%Y-%m-%d'
        datetime_str = datetime.datetime.strftime(date_time, format)
        return datetime_str

    def porFechaSerializer(self,record):
        lista = []
        for i in record:
                lista.append(
                {
                    'customerid': i[0],
                    'nombre': i[1],
                    'fecha' : self.convert(i[2])
                }
        )
        return lista

    def todosClientesSerializer( record):
        lista = []
        for i in record:
            lista.append(
                {
                    'cid': i[0],
                    'fecha': i[1],
                    'nombre': i[2],
                    'ciudad': i[3],
                    'estado': i[4],
                    'pais': i[5],
                    'cancion': i[6],
                    'genero': i[7],
                    'album': i[8],
                    'artista': i[9],
                    'sugerencias': []
                }
            )
        return lista

    def latestReleasesSerializer ( record):
        lista = []
        for i in record:
            lista.append({
                'fecha': str(i[0]),
                'cancion': i[1],
                'album': i[2],
                'artista': i[3],
                'genero': i[4],
            })
        return lista

    #Lo de PGAdmin
    params = config()
    conn = bd.connect(**params)
    cursor = conn.cursor()

    DATE = '2009-01-01'

    #Comienza los traslados a Mongo

    queryTodosClientes = """SELECT DISTINCT user_client.clientid, invoice.invoicedate AS fecha ,
	user_client.username AS nombre, billingcity AS ciudad, 
	billingstate AS estado, billingcountry AS pais, track.name AS cancion, genre.name AS genero , 
	album.title AS album, artist.name AS artista
FROM invoice JOIN invoiceline ON invoice.invoiceid = invoiceline.invoiceid
	JOIN track ON track.trackid = invoiceline.trackid
	JOIN album ON track.albumid = album.albumid
	JOIN artist ON artist.artistid = album.artistid
	JOIN user_client ON user_client.clientid = invoice.customerid
	JOIN genre ON track.genreid = genre.genreid
"""


    cursor.execute(queryTodosClientes)
    record = cursor.fetchall()
    
    lista = todosClientesSerializer(record)
    
    if (len(lista) !=0):
        mydb.customers.insert_many(lista)

    queryLatestRelases = """SELECT datemodified as releasedate, track.name, album.title, artist.name, genre.name
    FROM logbook 
        JOIN track ON logbook.itemmodified = track.trackid
        JOIN album ON album.albumid = track.albumid
        JOIN artist ON artist.artistid = album.artistid
        JOIN genre ON genre.genreid = track.genreid
    WHERE tablemodified = 'track' 
    ORDER BY releasedate DESC
    
    """

    cursor.execute(queryLatestRelases)
    record = cursor.fetchall()
    
    lista = latestReleasesSerializer(record)
    
    if (len(lista) != 0):
        mydb.releases.insert_many(lista)

    


    canciones = mydb.releases.find({})  
    usuarios = mydb.customers.find({}, {'cid': 1}).distinct(
        'cid')  
    for cancion in canciones:
        for usuario in usuarios:
            esta_cancion = {'cancion': cancion['cancion'], 'genero': cancion['genero'],
                            'album': cancion['album'], 'artista': cancion['artista'], 'puntuacion': 0}
            artistas = mydb.customers.find(
                {'cid': usuario}, {'artista': 1}).distinct('artista')  # ARRAY
            generos = mydb.customers.find(
                {'cid': usuario}, {'genero': 1}).distinct('genero')  # ARRAY
            albumes = mydb.customers.find(
                {'cid': usuario}, {'album': 1}).distinct('album')  # ARRAY
            if (cancion['genero'] in generos):
                esta_cancion['puntuacion'] += 10
            if (cancion['album'] in albumes):
                esta_cancion['puntuacion'] += 20
            if (cancion['artista'] in artistas):
                esta_cancion['puntuacion'] += 30
            mydb.customers.update_many(
                {'cid': usuario}, {'$push': {'sugerencias': esta_cancion}})


    def takeList(sugerencia):
        return sugerencia['puntuacion']


    contador = 0
    for cid in usuarios:
        customer = mydb.customers.find_one({'cid': cid})
        mydb.usuariosrecomendados.insert_one({
            'Customer ID': cid,
            'Nombre': customer['nombre'],
            'sugerencias': sorted(customer['sugerencias'], key=takeList)[::-1]
        })


    def set_date (self, newDate) : 
        self.DATE = newDate
        return self.DATE == newDate

    #Esta es la parte visual, no tiene relevancia
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
        self.label_2.setGeometry(QtCore.QRect(170, 30, 100, 100))
        self.label_2.setMinimumSize(QtCore.QSize(150, 150))
        self.label_2.setMaximumSize(QtCore.QSize(150, 150))
        self.label_2.setStyleSheet("")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("musics.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_2.setObjectName("label_2")



        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(470, 30, 400, 490))
        self.tableWidget.setStyleSheet("font: 14pt \"Times\";\n"
        "color: #1b1c34;\n"
        "background-color: #EDFEFB")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)



        self.pushButton_Buscar = QtWidgets.QPushButton(self.frame)
        self.pushButton_Buscar.setGeometry(QtCore.QRect(80, 440, 100, 30))
        self.pushButton_Buscar.setMinimumSize(QtCore.QSize(330, 50))
        self.pushButton_Buscar.setMaximumSize(QtCore.QSize(330, 50))
        self.pushButton_Buscar.setStyleSheet("background-color: #0ca692;\n"
        "font: 14pt \"Times\";\n"
        "color: rgb(255, 255, 255);\n"
        "border-radius: 5px;")
        self.pushButton_Buscar.setObjectName("pushButton_Buscar")


        self.comboBox_OpcionesBuscar = QtWidgets.QComboBox(self.frame)
        self.comboBox_OpcionesBuscar.setGeometry(QtCore.QRect(80, 180, 220, 31))
        self.comboBox_OpcionesBuscar.setMinimumSize(QtCore.QSize(330, 50))
        self.comboBox_OpcionesBuscar.setMaximumSize(QtCore.QSize(330, 50))
        self.comboBox_OpcionesBuscar.setStyleSheet("background-color: rgb(150, 172, 183);\n"
        "font: 13pt \"Times\";\n"
        "color: rgb(255, 255, 255);")
        self.comboBox_OpcionesBuscar.setObjectName("comboBox_OpcionesBuscar")
        self.comboBox_OpcionesBuscar.addItem("")
        self.comboBox_OpcionesBuscar.addItem("")
        self.comboBox_OpcionesBuscar.addItem("")


        
        self.calendarWidget = QtWidgets.QCalendarWidget(self.frame)
        self.calendarWidget.setGeometry(QtCore.QRect(80, 250, 330, 173))
        self.calendarWidget.setObjectName("calendarWidget")
        self.calendarWidget.setStyleSheet("background-color: #FFFFFF;")
        self.calendarWidget.clicked[QtCore.QDate].connect(lambda arg : self.set_date(arg.toString('yyyy-MM-dd')))




        self.pushButton_Buscar.clicked.connect(self.populateTable)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #segunda parte de la codificacion 

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_Buscar.setText(_translate("MainWindow", "Aplicar"))
        self.comboBox_OpcionesBuscar.setItemText(0, _translate("MainWindow", "¿Qué deseas ver?"))
        self.comboBox_OpcionesBuscar.setItemText(1, _translate("MainWindow", "Clientes por fecha"))
        self.comboBox_OpcionesBuscar.setItemText(2, _translate("MainWindow", "Sugerencias"))
    
    def useFirstRec(self, item) : 
        return item['sugerencias'][0]['puntuacion']
    
    def populateTable(self):
        fecha = self.DATE
        self.tableWidget.setRowCount(0)
        if (self.comboBox_OpcionesBuscar.currentText() == "Clientes por fecha"):
            self.mydb.invoice.delete_many({})
            print('SI FUNCIONAAAAA :))))   ')
            queryPorFecha = """SELECT DISTINCT user_client.clientid, user_client.username as nombre,
                invoice.invoicedate
                FROM invoice JOIN invoiceline ON invoice.invoiceid = invoiceline.invoiceid
                JOIN user_client ON invoice.customerid = user_client.clientid
                WHERE invoice.invoicedate = \'{}\'
                """.format(fecha)
            params = config()
            conn = bd.connect(**params)
            cursor = conn.cursor()
            cursor.execute(queryPorFecha)
            record = cursor.fetchall()
            # Los seriaizo a un diccionario
            lista = self.porFechaSerializer(record)
            #Los agrego a mi coleccion
            if len(lista) > 0 :
                self.mydb.invoice.insert_many(lista)
            porFecha = list(self.mydb.invoice.find({'fecha' : fecha}))
            
            self.tableWidget.setColumnCount(3)
            for item in porFecha: 
                rowposition = self.tableWidget.rowCount()
                self.tableWidget.insertRow(rowposition)
                self.tableWidget.setItem(rowposition, 0, QtWidgets.QTableWidgetItem(item['nombre']))
                self.tableWidget.setItem(rowposition, 1, QtWidgets.QTableWidgetItem(item['fecha']))
        if (self.comboBox_OpcionesBuscar.currentText() == "Sugerencias"):
            recomendaciones = list(self.mydb.usuariosrecomendados.find({}))
            usuariosRec = sorted(recomendaciones, key = self.useFirstRec)[::-1]
            if len(usuariosRec) > 10: 
                self.tableWidget.setColumnCount(4)
                for i in range(10):
                    rowposition = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(rowposition)
                    self.tableWidget.setItem(rowposition, 0, QtWidgets.QTableWidgetItem(usuariosRec[i]['Nombre']))
                    self.tableWidget.setItem(rowposition, 1, QtWidgets.QTableWidgetItem(usuariosRec[i]['sugerencias'][0]['cancion'] + ' de ' + usuariosRec[i]['sugerencias'][0]['artista']))
                    self.tableWidget.setItem(rowposition, 2, QtWidgets.QTableWidgetItem(usuariosRec[i]['sugerencias'][1]['cancion'] + ' de ' + usuariosRec[i]['sugerencias'][1]['artista']))
                    self.tableWidget.setItem(rowposition, 3, QtWidgets.QTableWidgetItem(usuariosRec[i]['sugerencias'][2]['cancion'] + ' de ' + usuariosRec[i]['sugerencias'][2]['artista']))
                    
            else:
                self.tableWidget.setColumnCount(4)
                for i in usuariosRec:
                    rowposition = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(rowposition)
                    self.tableWidget.setItem(rowposition, 0, QtWidgets.QTableWidgetItem(i['nombre']))
                    self.tableWidget.setItem(rowposition, 1, QtWidgets.QTableWidgetItem(i['sugerencias'][0]))
                    self.tableWidget.setItem(rowposition, 2, QtWidgets.QTableWidgetItem(i['sugerencias'][1]))
                    self.tableWidget.setItem(rowposition, 3, QtWidgets.QTableWidgetItem(i['sugerencias'][2]))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Mongo = QtWidgets.QMainWindow()
    ui = Ui_Mongo()
    ui.setupUi(Mongo)
    Mongo.show()
    sys.exit(app.exec_())


