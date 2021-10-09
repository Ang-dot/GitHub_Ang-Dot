/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths (i.e.: number of characters in the name). If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.
Note
You can write two separate queries to get the desired output. It need not be a single query.
*/
SELECT TOP 1 CITY , LEN(CITY) as 'number of characters in the name'
FROM STATION
ORDER BY LEN(CITY), CITY ASC;

SELECT TOP 1 CITY , LEN(CITY) as 'number of characters in the name'
FROM STATION
ORDER BY LEN(CITY) DESC, CITY ASC;