-- This script creates the database hbtn_0d_2 and the user user_0d_2 with password user_0d_2_pwd.
-- user_0d_2 should have only SELECT privilege in the database hbtn_0d_2
-- if the database or user exists the script should not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
