CREATE TABLE PEOPLE (
    NAME CHAR(10),
    HIRED DATE,
    STORE INTEGER,
    HOURLY BOOL DEFAULT 1
);

INSERT INTO PEOPLE
VALUES ('topsy', '2012/11/01', 4, 0),
       ('max', '2012/02/14', 4, 0),
       ('zach', '2009/03/24', 6, 0),
       ('sam', '2008/01/28', 6, 1);

INSERT INTO PEOPLE(NAME, STORE)
VALUES ('percy', 2),
       ('bailey', 2);

DELETE
FROM PEOPLE
WHERE NAME = 'bailey'
   OR NAME = 'percy';

UPDATE PEOPLE
SET HOURLY = TRUE
WHERE NAME = 'sam'
   OR NAME = 'topsy';
