/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
Find the difference between the total number of CITY entries in the table and the number of distinct CITY entries in the table.
*/
SELECT (COUNT (CITY) - COUNT (DISTINCT CITY)) AS DIFF
FROM STATION;