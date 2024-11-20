-- This script Lists all databases in MySQL server.
-- The SCHEMA_NAME column in INFORMATION_SCHEMA.SCHEMATA contains the names of all databases.
SELECT SCHEMA_NAME
FROM INFORMATION_SCHEMA.SCHEMATA 
ORDER BY SCHEMA_NAME;
