

def query1():
	query="SELECT artist.name, COUNT(album.albumid) FROM artist JOIN album ON album.artistid = artist.artistid GROUP BY artist.name ORDER BY COUNT(album.albumid) DESC LIMIT 5"
	return query

def query2():
	query = "SELECT genre.name, COUNT(track.genreid) FROM  track JOIN genre ON track.genreid = genre.genreid GROUP BY genre.name ORDER BY COUNT(track.genreid) DESC LIMIT 5"
	return query

def query3():
	query = "SELECT playlist.name, SUM(track.milliseconds) FROM playlisttrack JOIN track ON track.trackid = playlisttrack.trackid JOIN playlist ON playlisttrack.playlistid = playlist.playlistid GROUP BY playlist.name ORDER BY SUM(track.milliseconds) DESC"
	return query 

def query4():
	query = "SELECT track.name, artist.name as artista, track.milliseconds FROM track JOIN album ON track.albumid = album.albumid JOIN artist ON artist.artistid = album.artistid ORDER BY track.milliseconds DESC LIMIT 5"
	return query

def query5():
	query ="SELECT user_client.username, COUNT(track.name) FROM user_client JOIN artist ON artist.customerid = user_client.clientid JOIN album ON artist.artistid = album.artistid JOIN track ON album.albumid = track.albumid GROUP BY user_client.username ORDER BY COUNT(track.name) DESC LIMIT 5"
	return query

def query6():
	query = "SELECT genre.name, AVG(track.milliseconds) FROM track JOIN genre ON genre.genreid = track.genreid GROUP BY genre.name ORDER BY AVG(track.milliseconds) DESC"
	return query

def query7():
	query = "SELECT tabla.nombre, COUNT(tabla.artista) FROM (SELECT DISTINCT playlist.name as nombre, artist.name as artista FROM playlist JOIN playlisttrack ON playlist.playlistid = playlisttrack.playlistid JOIN track ON track.trackid = playlisttrack.trackid JOIN album ON track.albumid = album.albumid JOIN artist ON artist.artistid = album.artistid) as tabla GROUP BY nombre ORDER BY COUNT(artista) DESC "
	return query

def query8():
	query="SELECT tabla.artista, COUNT(tabla.genero) FROM (SELECT DISTINCT artist.name as artista, genre.name as genero FROM artist JOIN album ON artist.artistid = album.artistid JOIN track ON album.albumid = track.albumid JOIN genre ON track.genreid = genre.genreid) as tabla GROUP BY tabla.artista ORDER BY COUNT(tabla.genero) DESC LIMIT 5"
	return query