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

--Animes vistos del año 2023
SELECT count(id) as "Animes vistos en 2023" 
FROM emission WHERE last_chapter like "2023%" AND state like "Finalizado"

SELECT id, name, season, chapters, year, last_chapter
FROM emission WHERE state like "finalizado" AND last_chapter like "2023%"
order by last_chapter, name

--Animes vistos del año 2024
SELECT count(id) as "Animes vistos en 2024" 
FROM emission WHERE last_chapter like "2024%" AND state like "Finalizado"

SELECT id, name, season, chapters, year, last_chapter
FROM emission WHERE state like "finalizado" AND last_chapter like "2024%"
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
VALUES(3993, "The New Gate", 1, 3, "En emisión", "2024-04-14", "2024-04-28")

INSERT INTO emission (id, name, season, chapters, state, year, last_chapter)
VALUES(2887, "Death March kara Hajimaru Isekai Kyousoukyoku", 1, 12, "Finalizado", "2024-04-27", "2024-04-27")

INSERT INTO Finalizado (id, name, season, chapters, emited, last_chapter)
VALUES(3909, "Kusuriya no Hitorigoto", 1, 24, "2023-10-22", "2024-03-23")

INSERT INTO generos (id, genero) 
VALUES (3909, "Histórico"), (3909, "Drama"), (3909, "Misterio")

INSERT INTO generos (id, genero) 
VALUES (3975, "Acción"), (3975, "Colegial"), (3975, "Shounen")

INSERT INTO generos (id, genero) 
VALUES (3955, "Isekai"), (3955, "Fantasía"), (3955, "Aventura"), (3955, "Acción")

INSERT INTO generos (id, genero) 
VALUES (3956, "Aventura"), (3956, "Fantasía")

--Actualizar lista de animes
UPDATE emission SET state="En emisión", next_chapter="2024-05-03", last_chapter="" WHERE id=3968
UPDATE emission SET chapters=4, next_chapter="2024-05-04" WHERE id=3993
UPDATE emission SET chapters=12 WHERE id=3929
UPDATE emission SET name="Rurouni Kenshin: Meiji Kenkaku Romantan (2023)" WHERE id=3973
UPDATE emission SET season=3 WHERE id=3929
UPDATE emission SET id=3917, next_chapter="2024-01-17" WHERE id=3971
UPDATE emission SET state="Finalizado" WHERE id=3972
UPDATE emission SET id=3930 WHERE id=3970
UPDATE emission SET year="2023-07-06", last_chapter="2023-12-14" WHERE id=3838
UPDATE emission SET year="2024-05-12", next_chapter="2024-05-12" WHERE id=3976