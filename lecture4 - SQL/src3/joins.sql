CREATE TABLE passengers (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    flight_id INTEGER REFERENCES flights
);

/*
flight_id is marked as being a foreign key for the table flights with REFERENCES flights.
Since id is the PRIMARY KEY for flights, that is the column that is flights_id will map to by default.
*/

INSERT INTO passengers (name, flight_id) VALUES ('Alice', 1);
INSERT INTO passengers (name, flight_id) VALUES ('Bob', 1);
INSERT INTO passengers (name, flight_id) VALUES ('Charlie', 2);
INSERT INTO passengers (name, flight_id) VALUES ('Dave', 2);
INSERT INTO passengers (name, flight_id) VALUES ('Erin', 4);
INSERT INTO passengers (name, flight_id) VALUES ('Frank', 6);
INSERT INTO passengers (name, flight_id) VALUES ('Grace', 6);


SELECT origin, destination, name FROM flights INNER JOIN passengers ON passengers.flight_id = flights.id;
SELECT origin, destination, name FROM flights JOIN passengers ON passengers.flight_id = flights.id;
SELECT origin, destination, name FROM flights LEFT OUTER JOIN passengers ON passengers.flight_id = flights.id;
SELECT origin, destination, name FROM flights RIGHT OUTER JOIN passengers ON passengers.flight_id = flights.id;


/*
JOIN indicates that tables flights and passengers are being queried together.
JOIN performs an ‘inner join’: only rows where both tables match the query will be returned. In this example, only flights with passengers will be returned.
ON indicates how the two tables are related. In this example, the column flight_id in passengers reflects values in the column id in flights.
As before, queries can be constrained with WHERE.
LEFT JOIN includes rows from the first table listed even if there is no match (e.g. there are no passengers on that flight). RIGHT JOIN is analogous (e.g. passengers with no flights).
*/
