--Animes en emisión
SELECT count(id) as "Animes en emisión" FROM emission WHERE state like "En emisión"

SELECT id, name, season, chapters, year, next_chapter FROM emission WHERE state like "en emisión"
ORDER BY next_chapter, name

SELECT emission.id, name, genero, season, chapters, year, next_chapter FROM emission, generos 
WHERE state like "En emisión" AND emission.id = generos.id
ORDER BY next_chapter, name

SELECT emission.id, name, generos.genero, season, chapters, year, next_chapter 
FROM emission, generos 
WHERE state like "en emisión" AND emission.id = generos.id
ORDER BY next_chapter, name

SELECT name, season, chapters, genero FROM Finalizado, generos WHERE generos.id = Finalizado.id

--Animes vistos del año 2023
SELECT count(id) as "Animes vistos en 2023" 
FROM emission WHERE last_chapter like "2023%" AND state like "Finalizado"

SELECT id, name, season, chapters, year, last_chapter
FROM emission WHERE state like "finalizado" AND last_chapter like "2023%"
order by last_chapter, name

--Animes vistos del año 2024
SELECT count(id) as "Animes vistos en 2024" 
FROM emission WHERE last_chapter like "2024%" AND state like "Finalizado"

SELECT id, name as 'Título', season as 'Temporada', chapters as 'Capítulos', year as 'Emitido', last_chapter as 'Ultimo capítulo'
FROM emission WHERE state like "finalizado" AND last_chapter like "2024%"
order by last_chapter, name

--Animes vistos del año 2025
SELECT count(id) as "Animes vistos en 2025" 
FROM emission WHERE last_chapter like "2025%" AND state like "Finalizado"

SELECT id, name as 'Título', season as 'Temporada', chapters as 'Capítulos', year as 'Emitido', last_chapter as 'Ultimo capítulo'
FROM emission WHERE state like "finalizado" AND last_chapter like "2025%"
order by last_chapter, name

--UPDATE emission SET author="Akutami Gege" WHERE id=3836

SELECT name, author FROM emission WHERE author != "" AND author != "An author"

--Openings and Endings
SELECT ost.id, emission.name, ost.tipo, ost.nombre, ost.interprete
FROM emission, ost
WHERE emission.id = ost.id
ORDER BY name

--Listing by genrers
SELECT generos.genero, count(name) as "animes" 
from emission, generos 
WHERE state like "En emisión" AND emission.id = generos.id
GROUP BY genero
ORDER BY "animes" ASC

--Agregar nuevo anime
INSERT INTO emission (id, name, season, chapters, state, year, next_chapter)
VALUES(4054, "Dungeon ni Deai wo Motomeru no wa Machigatteiru Darou ka V: Houjou no Megami-hen", 5, 15, "En emisión", "2024-10-03", "2025-03-05")

INSERT INTO emission (id, name, season, chapters, state, year, last_chapter)
VALUES(4054, "Dungeon ni Deai wo Motomeru no wa Machigatteiru Darou ka V: Houjou no Megami-hen", 5, 15, "Finalizado", "2024-10-05", "2024-12-21")

--Nuevo anime con ID por defecto de la base de datos
INSERT INTO emission (name, season, chapters, state, year, next_chapter)
VALUES("Kanchigai no Atelier Meister: Eiyuu Party no Moto Zatsuyougakari ga, Jitsu wa Sentou Igai ga SSS Rank Datta to Iu Yoku Aru Hanashi, Kensei ni Naru", 1, 3, "En emisión", "2025-04-05", "2025-04-13")

INSERT INTO emission (name, season, chapters, state, year, last_chapter)
VALUES("Ore wa Subete wo «Parry» suru", 1, 12, "Finalizado", "2025-04-16", "2025-04-17")

INSERT INTO Finalizado (id, name, season, chapters, emited, last_chapter)
VALUES(3909, "Kusuriya no Hitorigoto", 1, 24, "2023-10-06", "2024-03-23")

INSERT INTO Finalizado (name, season, chapters, emited, last_chapter)
VALUES("Parasyte", 1, 12, "2025-04-19", "2025-04-21")

INSERT INTO generos (id, genero) 
VALUES (1635, "Acción"), (1635, "Sci-Fi"), (1635, "Drama"), (1635, "Psicológico"), (1635, "Seinen"), (1635, "Terror")

INSERT INTO generos (id, genero) 
VALUES (4088, "Acción"), (4088, "Aventura"), (4088, "Fantasia")

INSERT INTO generos (id, genero) 
VALUES (3955, "Isekai"), (3955, "Fantasía"), (3955, "Aventura"), (3955, "Acción")

INSERT INTO generos (id, genero) 
VALUES (3956, "Aventura"), (3956, "Fantasía")

--Actualizar lista de animes
UPDATE emission SET state="En emisión", next_chapter="2024-05-03", last_chapter="" WHERE id=3968
UPDATE emission SET next_chapter="2025-01-17" WHERE id=4079
UPDATE emission SET chapters=6, next_chapter="2024-05-14" WHERE id=3982
UPDATE emission SET chapters=79 WHERE id=3773
UPDATE emission SET name="Rurouni Kenshin: Meiji Kenkaku Romantan (2023)" WHERE id=3973
UPDATE emission SET season=1 WHERE id=4075
UPDATE emission SET next_chapter="2025-04-11" WHERE id=3773
UPDATE emission SET state="Finalizado" WHERE id=4005
UPDATE emission SET state="Finalizado",next_chapter="", last_chapter="2025-04-03" WHERE id=4081
UPDATE emission SET state="Finalizado", chapters=11, next_chapter="", last_chapter="2024-06-19" WHERE id=3988
UPDATE emission SET id=3930 WHERE id=3970
UPDATE emission SET year="2023-07-06", last_chapter="2023-12-14" WHERE id=3838
UPDATE emission SET year="2024-05-12", next_chapter="2024-05-12" WHERE id=3976