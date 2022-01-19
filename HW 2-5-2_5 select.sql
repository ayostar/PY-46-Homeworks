'1'

SELECT style_id, count(singer_id) FROM singer_style
GROUP BY style_id;

'2'

SELECT count(*) FROM track
JOIN album a ON a.id = track.album 
WHERE year BETWEEN 2019 AND 2020;

'3'

SELECT album, avg(length) FROM track
GROUP BY album
ORDER BY album;

'4'

SELECT s.id, s.name FROM singer s 
WHERE s.id NOT IN (
	SELECT sa.singer_id FROM singer_album sa 
	JOIN album a ON a.id = sa.album_id 
	WHERE a.year = 2020);

'5'

SELECT DISTINCT c.name FROM collection c 
JOIN track_collection tc ON c.id = tc.collection_id 
JOIN track t ON tc.track_id = t.id
JOIN album a ON t.album = a.id 
JOIN singer_album sa ON a.id = sa.album_id 
WHERE sa.singer_id = 7;

'6'

SELECT a.name FROM album a
JOIN singer_album sa ON a.id = sa.album_id
JOIN singer_style ss ON sa.singer_id = ss.singer_id
GROUP BY a.name
HAVING count(ss.singer_id) > 1;
	
'7'

SELECT t.name FROM track t 
LEFT JOIN track_collection tc ON t.id = tc.track_id
WHERE tc.track_id IS NULL;

'8'

SELECT s.name FROM singer s
JOIN singer_album sa ON s.id = sa.singer_id
JOIN track t on sa.album_id = t.album 
	WHERE t.length IN (
 	SELECT MIN(t.length) FROM track t);

'9'

select distinct a.name from album a
left join track as t on t.album = a.id
where t.album in (
    select album
    from track
    group by album
    having count(id) = (
        select count(id)
        from track
        group by album
        order by count
        limit 1
    )
)
order by a.name



