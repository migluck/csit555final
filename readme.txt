-- create database 'csit555final'
mysql -u root -p 
create database csit555final

-- Update file createDatabase.py, Line 6, mysqldatabase connection information
mysql://root:Password1234@localhost/csit555final

-- Create the database
-> python3 createDatabase.py

-- Run script to populate database
-> python3 insertScript.py
