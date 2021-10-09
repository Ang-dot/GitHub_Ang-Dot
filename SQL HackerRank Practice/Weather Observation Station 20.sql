/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
A median is defined as a number separating the higher half of a data set from the lower half. Query the median of the Northern Latitudes (LAT_N) from STATION and round your answer to 4 decimal places.
*/

SELECT DISTINCT
CAST((PERCENTILE_DISC(0.5) WITHIN GROUP(ORDER BY LAT_N ASC)  
    OVER ())
AS DECIMAL(10,4)) FROM STATION;