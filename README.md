# Proyecto de base de datos 
# Parte 1 y parte 2

## Instalaciones

Para que funcione el programa, se debe realizar una instalacion mediante ```pip```:

```bash
$ pip install pyqt5
```
```bash
$ pip install fpdf
```
```bash
$ pip install pymongo
```
```bash
$ pip install psycopg2
```
En el remoto caso que psicogp2 no funcione, instalar:
```bash
$ pip install psycopg2-binary
```

Luego, en una nueva base de POSTGRES,  se debe de copiar el archivo ```Proyecto1.sql```.

### PostgreSQL

Para que el sistema se concecte correctamente con la base de datos, es importante que el usuario agregue sus credenciales en el archivo ```base_de_datos.ini``` ubicado en el directorio principal. En este archivo se deben ingresar las credenciales indicadas (host, database, user, password, port) **sin el uso de comillas**. Ejemplo:
``` bash
host = 127.0.0.1
database= testdb
user= postgres
password= 12345678
port= 5432
```
se conectará a la base de datos ```testdb``` en el host ```127.0.01```, puerto ```5432``` como el usuario ```postgres``` y la contraseña ```12345678```.

### Importante - Mongodb

Es necesario que previo a la ejecución de la aplicación se cuente con un servicio de mongo activo.

La aplicacion se buscará por defecto conectarse con Mongo en  ```mongodb://localhost:27017```. En caso sea necesario, cambiar el valor de la variable ```MONGO_PORT``` en el archivo ```Mongo.py``` (linea 17).

### Finalmente

Para ejecutar la aplicación, correr el acrchivo ```Loginaccount.py```:
