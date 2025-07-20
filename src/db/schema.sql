-- mysql -p
CREATE DATABASE IF NOT EXISTS countriesdb;
USE countriesdb;

-- Create tables
CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    country VARCHAR(200) NOT NULL,
    c_population INTEGER,
    gdp FLOAT,
    debt FLOAT
);

-- Insert data
INSERT INTO 
    countries 
        (id, country, c_population, gdp, debt) 
VALUES
    (1, 'US', 331002651, 21137518, 28141300000000),
    (2, 'Europe', 747636026, 15546200000000, 13000000000000),
    (3, 'China', 1439323776, 14342903, 9800000000000);
