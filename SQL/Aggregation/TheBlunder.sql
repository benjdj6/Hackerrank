/*
Enter your query here.
*/
SELECT CEIL(AVG(SALARY - REPLACE(SALARY, '0', ''))) FROM EMPLOYEES;