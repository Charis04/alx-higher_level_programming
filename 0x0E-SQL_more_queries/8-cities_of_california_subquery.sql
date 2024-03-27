-- list cities in carlifonia
SELECT id, name FROM cities
	WHERE state_id = (SELECT id FROM states WHERE name = 'Carlifonia')
	ORDER BY id ASC;
