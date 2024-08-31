-- A script to createa new user and grant some privileges to them
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';
CREATE USER IF NOT EXISTS 'replica_user'@'%' IDENTIFIED BY 'Toluwaloju2002';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%'
