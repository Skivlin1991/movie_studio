DROP TABLE IF EXISTS movie;
CREATE TABLE movie (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    rating VARCHAR(255),
);