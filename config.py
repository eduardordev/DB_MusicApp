from configparser import ConfigParser # Esencial para leer archivos .ini

def config(archivo='base_de_datos.ini', seccion='postgresql'):
	parser = ConfigParser()
	parser.read(archivo) #Extrae la informacion ingresada en el .ini
	db={}  
	if parser.has_section(seccion):
		params = parser.items(seccion)
		for param in params:
			db[param[0]] = param[1]
	else:
		raise Exception('Existe un error en el .ini'.format(seccion, archivo))
	return db
