CREATE DATABASE proyecto;

CREATE TABLE usuarios(
	nombre text,
	apellido text,
	username text,
	contraseña text,
);
CREATE TABLE musica(
	id int,
	genero text,
	album text,
	cancion text,
	artista text,
	f_publi text
);
CREATE TABLE artista(
	nombre_artistico text,
	genero text,
	manager text
);
CREATE TABLE manager(
	nombre text,
	artista text
);

INSERT INTO public.musica(
	id, genero, album, cancion, artista, f_publi)
	VALUES ('1', 'Pop Rock', 'Hollywood’s Bleeding', 'Wow', 'Post Malone', '2019');
	
INSERT INTO public.musica(
	id, genero, album, cancion, artista, f_publi)
	VALUES ('2', 'Pop Rock', 'Hollywood’s Bleeding', 'Hollywood’s Bleeding', 'Post Malone', '2019');
	
INSERT INTO public.musica(
	id, genero, album, cancion, artista, f_publi)
	VALUES ('3', 'Pop Rock', 'Hollywood’s Bleeding', 'Circles', 'Post Malone', '2019');
	
INSERT INTO public.musica(
	id, genero, album, cancion, artista, f_publi)
	VALUES ('4', 'Pop Rock', 'Hollywood’s Bleeding', 'Sunflower', 'Post Malone', '2019');
	
	
	
	
	
INSERT INTO public.musica(
	id, genero, album, cancion, artista, f_publi)
	VALUES ('5', 'Reguetón', 'YHLQMDLG', 'A tu merced', 'Bad Bunny', '2020');
	
INSERT INTO public.musica(
	id, genero, album, cancion, artista, f_publi)
	VALUES ('6', 'Reguetón', 'YHLQMDLG', 'Safaera', 'Bad Bunny', '2020');
	
INSERT INTO public.musica(
	id, genero, album, cancion, artista, f_publi)
	VALUES ('7', 'Reguetón', 'YHLQMDLG', 'Si veo a tu mamá', 'Bad Bunny', '2020');
	
INSERT INTO public.musica(
	id, genero, album, cancion, artista, f_publi)
	VALUES ('8', 'Reguetón', 'YHLQMDLG', 'Hablamos mañana', 'Bad Bunny', '2020');
	
INSERT INTO public.musica(
	id, genero, album, cancion, artista, f_publi)
	VALUES ('9', 'Reguetón', 'YHLQMDLG', 'Está cabrón ser yo', 'Bad Bunny', '2020');
	
	
INSERT INTO public.musica(
	id, genero, album, cancion, artista, f_publi)
	VALUES ('10', 'Hip hop', 'Scorpion', 'Gods Plan', 'Drake', '2018');
	
INSERT INTO public.musica(
	id, genero, album, cancion, artista, f_publi)
	VALUES ('11', 'Hip hop', 'Scorpion', 'Nice for What', 'Drake', '2018');
	
INSERT INTO public.musica(
	id, genero, album, cancion, artista, f_publi)
	VALUES ('12', 'Hip hop', 'Scorpion', 'Im Upset', 'Drake', '2018');
	
INSERT INTO public.musica(
	id, genero, album, cancion, artista, f_publi)
	VALUES ('13', 'Hip hop', 'Scorpion', 'Don’t Matter To Me', 'Drake', '2018');
	
INSERT INTO public.musica(
	id, genero, album, cancion, artista, f_publi)
	VALUES ('13', 'Hip hop', 'Scorpion', 'In My Feelings', 'Drake', '2018');
	
	
	
	
INSERT INTO public.musica(
	id, genero, album, cancion, artista, f_publi)
	VALUES ('14', 'Pop', 'When We All Fall Asleep, Where Do We Go?', 'You Should See Me in a Crown', 'Billie Eilish', '2019');
	
INSERT INTO public.musica(
	id, genero, album, cancion, artista, f_publi)
	VALUES ('15', 'Pop', 'When We All Fall Asleep, Where Do We Go?', 'Bury a Friend', 'Billie Eilish', '2019');
	
INSERT INTO public.musica(
	id, genero, album, cancion, artista, f_publi)
	VALUES ('16', 'Pop', 'When We All Fall Asleep, Where Do We Go?', 'When the Partys Over', 'Billie Eilish', '2019');
	
INSERT INTO public.musica(
	id, genero, album, cancion, artista, f_publi)
	VALUES ('17', 'Pop', 'When We All Fall Asleep, Where Do We Go?', 'Bad Guy', 'Billie Eilish', '2019');
	
INSERT INTO public.musica(
	id, genero, album, cancion, artista, f_publi)
	VALUES ('18', 'Pop', 'When We All Fall Asleep, Where Do We Go?', 'All the Good Girls Go to Hell', 'Billie Eilish', '2019');
	
	
INSERT INTO public.musica(
	id, genero, album, cancion, artista, f_publi)
	VALUES ('19', '	Dance-pop', 'Future Nostalgia', 'Future Nostalgia', 'Dua Lipa', '2020');
	
INSERT INTO public.musica(
	id, genero, album, cancion, artista, f_publi)
	VALUES ('20', '	Dance-pop', 'Future Nostalgia', 'Dont Start Now', 'Dua Lipa', '2020');
	
INSERT INTO public.musica(
	id, genero, album, cancion, artista, f_publi)
	VALUES ('21', '	Dance-pop', 'Future Nostalgia', 'Cool', 'Dua Lipa', '2020');
	
INSERT INTO public.musica(
	id, genero, album, cancion, artista, f_publi)
	VALUES ('22', '	Dance-pop', 'Future Nostalgia', 'Break My Heart', 'Dua Lipa', '2020');
	
INSERT INTO public.musica(
	id, genero, album, cancion, artista, f_publi)
	VALUES ('23', '	Dance-pop', 'Future Nostalgia', 'Pretty Pleas', 'Dua Lipa', '2020');
	
	
INSERT INTO public.musica(
	id, genero, album, cancion, artista, f_publi)
	VALUES ('24', '	Disco', 'Random Access Memories', 'Get Lucky', ' Daft Punk', '2013');
	
INSERT INTO public.musica(
	id, genero, album, cancion, artista, f_publi)
	VALUES ('25', '	Disco', 'Random Access Memories', 'Lose Yourself to Dance', ' Daft Punk', '2013');
	
INSERT INTO public.musica(
	id, genero, album, cancion, artista, f_publi)
	VALUES ('26', '	Disco', 'Random Access Memories', 'Doin It Right', ' Daft Punk', '2013');
	
INSERT INTO public.musica(
	id, genero, album, cancion, artista, f_publi)
	VALUES ('27', '	Disco', 'Random Access Memories', 'Instant Crush', ' Daft Punk', '2013');
	
INSERT INTO public.musica(
	id, genero, album, cancion, artista, f_publi)
	VALUES ('28', '	Disco', 'Random Access Memories', 'Give Life Back to Music', ' Daft Punk', '2013');
	

INSERT INTO public.musica(
	id, genero, album, cancion, artista, f_publi)
	VALUES ('29', 'Hip hop', 'The Marshall Mathers LP', 'The Real Slim Shady', 'Eminem', '2000');
	
INSERT INTO public.musica(
	id, genero, album, cancion, artista, f_publi)
	VALUES ('30', 'Hip hop', 'The Marshall Mathers LP', 'The Way I Am', 'Eminem', '2000');
	
INSERT INTO public.musica(
	id, genero, album, cancion, artista, f_publi)
	VALUES ('31', 'Hip hop', 'The Marshall Mathers LP', 'Bitch Please II', 'Eminem', '2000');
	
INSERT INTO public.musica(
	id, genero, album, cancion, artista, f_publi)
	VALUES ('32', 'Hip hop', 'Music to Be Murdered By', 'Darkness', 'Eminem', '2020');
	
INSERT INTO public.musica(
	id, genero, album, cancion, artista, f_publi)
	VALUES ('33', 'Hip hop', 'Music to Be Murdered By', 'Godzilla', 'Eminem', '2020');
	
	
INSERT INTO public.musica(
	id, genero, album, cancion, artista, f_publi)
	VALUES ('34', 'R&B', 'Thank U, Next', '7 Rings', 'Ariana Grande', '2018');
	
INSERT INTO public.musica(
	id, genero, album, cancion, artista, f_publi)
	VALUES ('35', '	Pop', 'Thank U, Next', 'Thank U, Next', 'Ariana Grande', '2018');
	
INSERT INTO public.musica(
	id, genero, album, cancion, artista, f_publi)
	VALUES ('36', '	Pop', 'Thank U, Next', 'Break Up with Your Girlfriend, Im Bored', 'Ariana Grande', '2018');
	
INSERT INTO public.musica(
	id, genero, album, cancion, artista, f_publi)
	VALUES ('37', '	Pop', 'Positions', 'Positions', 'Ariana Grande', '2020');
	
INSERT INTO public.musica(
	id, genero, album, cancion, artista, f_publi)
	VALUES ('38', 'R&B', 'Positions', '34+35', 'Ariana Grande', '2020');
	
	
INSERT INTO public.musica(
	id, genero, album, cancion, artista, f_publi)
	VALUES ('39', 'música urbana,', 'Colores', 'Rojo', 'J Balvin', '2020');
	
INSERT INTO public.musica(
	id, genero, album, cancion, artista, f_publi)
	VALUES ('40', 'música urbana,', 'Colores', 'Blanco', 'J Balvin', '2020');
	
INSERT INTO public.musica(
	id, genero, album, cancion, artista, f_publi)
	VALUES ( '41', 'R&B', 'Changes', 'Yummy', 'Justin Bieber', '2020');
	
INSERT INTO public.musica(
	id, genero, album, cancion, artista, f_publi)
	VALUES ( '42','	Pop', 'Justice', 'Anyone', 'Justin Bierber', '2021');
	
INSERT INTO public.musica(
	id, genero, album, cancion, artista, f_publi)
	VALUES ( '43','	House', 'Skin Companion EP 2', 'Hyperreal', 'Flume', '2017');
	
INSERT INTO public.musica(
	id, genero, album, cancion, artista, f_publi)
	VALUES ( '44','Hip-Hop', 'Astroworld', 'Sicko Mode', 'Travis Scott', '2019');
	
INSERT INTO public.musica(
	id, genero, album, cancion, artista, f_publi)
	VALUES ( '45','Norteña', 'Jefe de Jefes', 'Jefe de Jefes', 'Los Tigres del Norte', '1997');
	
INSERT INTO public.musica(
	id, genero, album, cancion, artista, f_publi)
	VALUES ( '46','Pop Rock', 'Happiness Begins', 'Sucker', 'Jonas Brothers', '2019');
	
	
INSERT INTO public.musica(
	id, genero, album, cancion, artista, f_publi)
	VALUES ( '47', 'hip-Hop', 'Championships', 'Going Bad', ' Meek Mill', '2020');
	
	
INSERT INTO public.musica(
	id, genero, album, cancion, artista, f_publi)
	VALUES ( '48', 'Reggaeton', 'El último tour del mundo', 'Dakiti', 'Bad Bunny', '2020');
	
	
INSERT INTO public.musica(
	id, genero, album, cancion, artista, f_publi)
	VALUES ( '49','Rap', ' I Am > I Was', 'A Lot', '21 Savage featuring J. Cole', '2019');
	

INSERT INTO public.musica(
	id, genero, album, cancion, artista, f_publi)
	VALUES ( '50','Reggaeton', 'X 100pre', 'Mia', 'Bad Bunny', '2018');
	
	

	

	
