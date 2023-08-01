-- Script that creates the database hbtn_0d_2 and the user user_0d_2.
-- Query that creates the databse
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Query that creates the user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';
-- Query that sets password for user. 
SET PASSWORD FOR 'user_0d_2'@'localhost' = 'user_0d_2_pwd';
-- Grant user select privilages on hbtn_0d_2
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';
