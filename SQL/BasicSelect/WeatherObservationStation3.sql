/*
Enter your query here.
*/
SELECT CITY FROM STATION WHERE ID % 2 = 0 GROUP BY CITY;