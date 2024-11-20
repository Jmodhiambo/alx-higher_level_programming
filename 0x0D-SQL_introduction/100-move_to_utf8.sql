-- Set the current database context to hbtn_0c_0
USE `hbtn_0c_0`;

-- Alter the first_table to convert its character set and collation
-- Convert all columns in first_table to utf8mb4 character set and utf8mb4_unicode_ci collation
ALTER TABLE `first_table`
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
