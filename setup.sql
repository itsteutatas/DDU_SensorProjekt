CREATE database senseDB;
USE senseDB;

CREATE TABLE collectors(
    collectorID int NOT NULL AUTO_INCREMENT,
    room_number int,
    PRIMARY KEY(collectorID));
CREATE TABLE data(
    dataID int NOT NULL AUTO_INCREMENT,
    collectorID int,
    humidity int,
    temp float,
    date VARCHAR(10),
    FOREIGN KEY (collectorID) REFERENCES collectors(collectorID),
    PRIMARY KEY(dataID));

INSERT INTO collectors(collectorID, room_number) VALUES (1, 934);
