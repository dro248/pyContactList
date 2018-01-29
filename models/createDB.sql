
CREATE DATABASE contact_list;



CREATE TABLE person (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) not null,
        username VARCHAR(255) UNIQUE not null,
        password VARCHAR(255) not null,
        address VARCHAR(255),
        email VARCHAR(255) not null,
        photo_url VARCHAR(2083),
        UNIQUE (username)
);

