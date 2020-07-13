-- script that displays the average temperature
-- by city ordered by temperature (descending).
-- command import table in database mysql -u root -p hbtn_0c_0 < temperatures.sql
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
