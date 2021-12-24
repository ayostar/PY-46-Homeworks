SELECT name, year FROM album
WHERE year = 2018;

SELECT name, length FROM track
ORDER by length DESC
LIMIT 1;

SELECT name FROM track
WHERE length >= 3.30;

SELECT name, year FROM collection
WHERE year BETWEEN 2018 AND 2020;

SELECT name FROM singer
WHERE name not LIKE '% %';

SELECT name FROM track
WHERE name iLIKE '%My%';