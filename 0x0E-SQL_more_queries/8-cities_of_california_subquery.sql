-- list cities in carlifonia
SELECT name FROM cities
	WHERE state_id = (SELECT id FROM states WHERE name = 'carlifonia')
	ORDER BY id ASC;
