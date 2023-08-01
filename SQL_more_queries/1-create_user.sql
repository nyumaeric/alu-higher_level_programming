-- Script that creates the MySQL server user user_0d_1 if it does not exist and grants it all privalages on the MySQL server.
-- Query that creates the MySQL server user user_0d_1.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
-- Query that sets password for. (Identify by fails with if not exists)
SET PASSWORD FOR 'user_0d_1'@'localhost' = 'user_0d_1_pwd';
-- Query that grants privilages to the user.
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
