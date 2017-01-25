/*
Enter your query here.
*/
SELECT CITY FROM STATION WHERE CITY REGEXP "[a,e,i,o,u]$" GROUP BY CITY;