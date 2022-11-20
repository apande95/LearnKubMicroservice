CREATE USER 'admin'@'localhost' IDENTIFIED BY 'admin';

CREATE DATABASE auth;

GRANT ALL PRIVILEGES ON auth.* TO 'admin'@'localhost';

USE auth;

CREATE TABLE user (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);

INSERT INTO user (email, password) VALUES ('admin','admin');