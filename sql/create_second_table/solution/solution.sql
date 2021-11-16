CREATE TABLE STORES
(
    NAME   VARCHAR(20),
    NUMBER INTEGER,
    CITY   VARCHAR(20)
);
-- Query OK, 0 rows affected

INSERT INTO STORES
VALUES ('headquarters', 4, 'new york'),
       ('midwest', 5, 'chicago'),
       ('west coast', 6, 'san francisco');
-- Query OK, 3 rows affected
-- Records: 3  Duplicates: 0  Warnings: 0

SELECT *
FROM STORES;
-- +--------------+--------+----------------+
-- | name         | number | city           |
-- +--------------+--------+----------------+
-- | headquarters |  	4   | new york  	|
-- | midwest      |  	5   | chicago   	|
-- | west coast   |  	6   | san francisco |
-- +--------------+--------+----------------+
-- 3 rows in set (0,00 sec)
