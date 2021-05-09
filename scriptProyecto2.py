import pymongo
import psycopg2 as bd
from pymongo import MongoClient
import pprint

host = '127.0.0.1'
dbname = 'proyectoFinal'
user = 'postgres'
password = '59809690'
port = '5432'


client = MongoClient()
db = client['proyecto2']
collection = db['tracks_compradas']

conn = bd.connect(host=host, dbname=dbname, user=user, password=password, port=port)
cursor = conn.cursor()

anio = input("Ingrese un año:")
mes = input("Ingrese un numero de mes:")
dia = input("Ingrese un numero de dia")

date = anio + "/" + mes + "/" + dia

query = "SELECT firstname, lastname, invoiceline.unitprice, quantity, track.name as cancion, genre.name as genero FROM invoice JOIN customer ON invoice.customerid = customer.customerid JOIN invoiceline ON invoice.invoiceid = invoiceline.invoiceid JOIN track ON invoiceline.trackid = track.trackid JOIN genre ON genre.genreid = track.genreid WHERE invoice.invoicedate = \'"+str(date)+"\'"
cursor.execute(query)
compras = cursor.fetchall()

for compra in compras:
  document = {
    'firstname': str(compra[0]),
    'lastname': str(compra[1]),
    'precio': str(compra[2]),
    'cantidad': str(compra[3]),
    'cancion': str(compra[4]),
    'genero': str(compra[5]),
  }
  collection.insert_one(document)

for doc in collection.find():
  print(doc)