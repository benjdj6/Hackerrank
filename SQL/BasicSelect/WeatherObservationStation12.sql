/*
Enter your query here.
*/
SELECT DISTINCT CITY FROM STATION WHERE CITY NOT REGEXP "^[a,e,i,o,u]|[a,e,i,o,u]$";