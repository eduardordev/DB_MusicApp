import pymongo
import datetime
from config import config
import psycopg2 as bd


# sudo systemctl start mongod
# sudo systemctl status mongod
# sudo /usr/bin/mongod --config /etc/mongod.conf


# Esta es la configuracion por DEFAULT, cambiar de ser necesario
myClient = pymongo.MongoClient('mongodb://localhost:27017')
mydb = myClient['proyecto']
clientes = mydb['client']
compras = mydb['invoice']
#Limpio mi bd en MONGO
mydb.invoice.delete_many({})  # Esta es para las ventas por fecha
mydb.customers.delete_many({}) # Esta es para todas las compras de todos los clientes
mydb.releases.delete_many({})  # Esta es para los ultimos releases
mydb.usuariosrecomendados.delete_many({}) # En esta coleccion se almacenan los usuarios con sus recomendaciones
# Function to covert string to datetime
def convert(date_time):
    format = '%Y/%m/%d'  # The format
    datetime_str = datetime.datetime.strptime(date_time, format)

    return datetime_str

#Convierte lo que viene del query a lista de diccionarios
def porFechaSerializer(record):
    lista = []
    for i in record:
        lista.append(
            {
                'customerid': i[0],
                'nombre': i[1],
                'pais': i[2],
                'estado': i[3],
                'ciudad': i[4],
                'telefono': i[5],
                'direccion': i[6],
                'fecha' : i[7]
            }
        )
    return lista

#Convierte lo que viene de customer a una lista de diccionarios
def todosClientesSerializer(record):
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

#Convierte los latest releases a una lista de diccionarios
def latestReleasesSerializer(record):
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


#Parametros de POSTGRESQL
params = config()
conn = bd.connect(**params)
cursor = conn.cursor()

DATE = '2009/1/1'

queryPorFecha = """SELECT DISTINCT customer.customerid,CONCAT(customer.firstname,' ', customer.lastname) as nombre,
    invoice.billingcountry as pais, invoice.billingstate as estado, invoice.billingcity as ciudad, customer.phone, customer.address
FROM invoice JOIN invoiceline ON invoice.invoiceid = invoiceline.invoiceid
	JOIN customer ON invoice.customerid = customer.customerid
WHERE invoice.invoicedate = \'{}\'
""".format(DATE)

cursor.execute(queryPorFecha)
record = cursor.fetchall()
# Los seriaizo a un diccionario
lista = porFechaSerializer(record)
#Los agrego a mi coleccion
mydb.invoice.insert_many(lista)

#
#
# Aqui si empiezan las recomendaciones (emoji de fueguitos)
#
#

queryTodosClientes = """SELECT DISTINCT customer.customerid, invoice.invoicedate AS fecha ,
	CONCAT(customer.firstname,' ',customer.lastname) AS nombre, billingcity AS ciudad, 
	billingstate AS estado, billingcountry AS pais, track.name AS cancion, genre.name AS genero , 
	album.title AS album, artist.name AS artista
FROM invoice JOIN invoiceline ON invoice.invoiceid = invoiceline.invoiceid
	JOIN track ON track.trackid = invoiceline.trackid
	JOIN album ON track.albumid = album.albumid
	JOIN artist ON artist.artistid = album.artistid
	JOIN customer ON customer.customerid = invoice.customerid
	JOIN genre ON track.genreid = genre.genreid
--WHERE invoice.invoicedate= \'2009/1/1\'
"""

cursor.execute(queryTodosClientes)
record = cursor.fetchall()
# Los seriaizo a un diccionario
lista = todosClientesSerializer(record)
#Los agrego a mi coleccion
mydb.customers.insert_many(lista)

queryLatestRelases = """SELECT datemodified as releasedate, track.name, album.title, artist.name, genre.name
FROM logbook 
	JOIN track ON logbook.itemmodified = track.trackid
	JOIN album ON album.albumid = track.albumid
	JOIN artist ON artist.artistid = album.artistid
	JOIN genre ON genre.genreid = track.genreid
WHERE tablemodified = 'track' 
ORDER BY releasedate DESC
--LIMIT 20
"""

cursor.execute(queryLatestRelases)
record = cursor.fetchall()
# Los seriaizo a un diccionario
lista = latestReleasesSerializer(record)
#Los agrego a mi coleccion
mydb.releases.insert_many(lista)

############################################################################################
#                                                                                          #
#                       Algoritmo de recomendacion BD                                      #
#                                                                                          #
############################################################################################

# Esta es la configuracion por DEFAULT, cambiar de ser necesario
myClient = pymongo.MongoClient('mongodb://localhost:27017')
mydb = myClient['proyecto']

#El sistema funciona con puntos

canciones = mydb.releases.find({}) #Lista de diccionarios
usuarios = mydb.customers.find({}, {'cid':1} ).distinct('cid') # lista plana (solo de CIDs)
for cancion in canciones:
    for usuario in usuarios:
        esta_cancion = {'cancion': cancion['cancion'], 'genero' : cancion['genero'],'album': cancion['album'], 'artsita' : cancion['artista'], 'puntuacion' : 0}
        artistas = mydb.customers.find({'cid' : usuario}, {'artista': 1}).distinct('artista') # ARRAY
        generos =  mydb.customers.find({'cid' : usuario},{'genero': 1}).distinct('genero')# ARRAY
        albumes =  mydb.customers.find({'cid' : usuario}, {'album': 1}).distinct('album')# ARRAY
        if (cancion['genero'] in generos):
            esta_cancion['puntuacion'] += 10
        if (cancion['album'] in albumes):
            esta_cancion['puntuacion'] += 20
        if (cancion['artista'] in artistas):
            esta_cancion['puntuacion'] += 30
        mydb.customers.update_many({'cid':usuario}, {'$push' : {'sugerencias' : esta_cancion}})

def takeList(sugerencia):
    return sugerencia['puntuacion']

contador = 0
for cid in usuarios:
    customer = mydb.customers.find_one({'cid' : cid })
    mydb.usuariosrecomendados.insert_one({
        'Customer ID': cid,
        'Nombre' : customer['nombre'],
        'Recomendaciones': sorted(customer['sugerencias'], key=takeList)[::-1] #Ordenadas en orden descendente
    })

# x = mybd.usuariosrecomendados.find({})
# for i in x :
#     print (i)