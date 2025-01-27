-- Module for creating database and users


DROP DATABASE IF EXISTS hbnb_dev_db;

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;


CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

ALTER USER 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
ALTER USER 'root'@'localhost' IDENTIFIED BY 'root'

GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

FLUSH PRIVILEGES;

USE hbnb_dev_db;
