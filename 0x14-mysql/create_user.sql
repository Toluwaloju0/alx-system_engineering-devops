-- A script to create a user and add values to the table
CREATE DATABASE IF NOT EXISTS tyrell_corp;
GRANT SELECT ON tyrell_corp.* TO 'holberton_user'@'localhost';
USE tyrell_corp;
CREATE TABLE IF NOT EXISTS nexus6 (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(256) NOT NULL
  );

INSERT INTO nexus6 (name) VALUES
  ('John'),
  ('Ahmed'),
  ('Claire');
