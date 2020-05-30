-- table query
CREATE TABLE flights (
    id SERIAL PRIMARY KEY,
    origin VARCHAR NOT NULL,
    destination VARCHAR NOT NULL,
    duration INTEGER NOT NULL
    
);

CREATE TABLE passengers(
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    -- FOREIGN key
    flight_id INTEGER REFERENCES flights 
);

-- insert query 
INSERT INTO flights(origin, destination, duration) 
VALUES('New York', 'London', 415);
INSERT INTO flights(origin, destination, duration) 
VALUES('Shanghai', 'Paris', 760);
INSERT INTO flights(origin, destination, duration) 
VALUES('Istanbul', 'Tokyo', 700);
INSERT INTO flights(origin, destination, duration) 
VALUES('New York', 'Paris', 435);
INSERT INTO flights(origin, destination, duration) 
VALUES('Moscow', 'London', 245);
INSERT INTO flights(origin, destination, duration) 
VALUES('Lima', 'New York', 455);

INSERT INTO passengers(name, flight_id) VALUES('Anas', 1);
INSERT INTO passengers(name, flight_id) VALUES('Ali', 1);
INSERT INTO passengers(name, flight_id) VALUES('Rehan', 2);
INSERT INTO passengers(name, flight_id) VALUES('Hamza', 2);
INSERT INTO passengers(name, flight_id) VALUES('Ansar', 4);
INSERT INTO passengers(name, flight_id) VALUES('Asad', 6);
INSERT INTO passengers(name, flight_id) VALUES('Jameel', 6);

-- update query 
UPDATE flights 
SET duration = 430 
WHERE origin = 'New York' AND destination = 'London';

-- delete query
DELETE from flights WHERE id = 3; -- will delete the field
INSERT INTO passengers(name, flight_id) VALUES('Jazib', 3); -- through error because of foreign key   
DELETE from flights WHERE id = 4; -- can't be deleted, it violates foreign key constraints 

-- select query
SELECT * FROM flights;
SELECT origin, destination FROM flights;
SELECT * FROM flights WHERE id = 3;
SELECT * FROM flights WHERE duration > 500;
SELECT * FROM flights WHERE duration > 500 AND destination = 'Paris';
SELECT AVG(duration) FROM flights;
SELECT COUNT(*) FROM flights; 
SELECT MIN(duration) FROM flights; 
SELECT * FROM flights WHERE origin IN('New York', 'Lima');
SELECT * FROM flights WHERE origin LIKE '%a%'; -- character sequence
SELECT * FROM flights LIMIT 2;
SELECT * FROM flights ORDER BY duration ASC;
SELECT origin, COUNT(*) FROM flights GROUP BY origin;
SELECT origin, COUNT(*) FROM flights GROUP BY origin HAVING COUNT(*) > 1;

-- JOIN query
SELECT origin, destination, name FROM flights JOIN passengers ON
    passengers.flight_id = flights.id;

SELECT origin, destination, name FROM flights LEFT JOIN passengers ON
    passengers.flight_id = flights.id;

-- indexing
select * from flights WHERE id IN
(select flight_id from passengers GROUP BY flight_id HAVING COUNT(*) > 1);
