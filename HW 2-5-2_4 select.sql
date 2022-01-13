'1'

SELECT style_id, count(singer_id) FROM singer_style
GROUP BY style_id;

'2'

SELECT count(*) FROM track
INNER JOIN album a ON a.id = track.album 
WHERE year BETWEEN 2019 AND 2020;

'3'

SELECT album, avg(length) FROM track
GROUP BY album
ORDER BY album;

'4'

SELECT s.id, s.name FROM singer s 
WHERE s.id NOT IN (
	SELECT sa.singer_id FROM singer_album sa 
	INNER JOIN album a ON a.id = sa.album_id 
	WHERE a.year = 2020);

'5'

SELECT DISTINCT c.name FROM collection c 
INNER JOIN track_collection tc ON c.id = tc.collection_id 
INNER JOIN track t ON tc.track_id = t.id
INNER JOIN album a ON t.album = a.id 
INNER JOIN singer_album sa ON a.id = sa.album_id 
WHERE sa.singer_id = 7;

'6'

SELECT a.name FROM album a
INNER JOIN singer_album sa ON a.id = sa.album_id
INNER JOIN singer_style ss ON sa.singer_id = ss.singer_id
GROUP BY a.name
HAVING count(ss.singer_id) > 1;
	
'7'

SELECT t.name FROM track t 
LEFT JOIN track_collection tc ON t.id = tc.track_id
WHERE tc.track_id IS NULL;

'8'

SELECT s.name FROM singer s
INNER JOIN singer_album sa ON s.id = sa.singer_id
INNER JOIN track t on sa.album_id = t.album 
	WHERE t.length IN (
 	SELECT MIN(t.length) FROM track t);

'9'

SELECT a.name FROM album a
INNER JOIN track t ON t.album = a.id
GROUP BY a.name
HAVING count(t.id) = (SELECT min(t.id) FROM track t)


