CREATE DATABASE calu;
CREATE USER 'calu_user'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON calu.* TO 'calu_user'@'localhost';
FLUSH PRIVILEGES;
