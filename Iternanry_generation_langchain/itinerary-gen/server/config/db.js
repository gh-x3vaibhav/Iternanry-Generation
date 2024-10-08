const mysql = require('mysql2');

// Set up the database connection
const connection = mysql.createConnection({
    host: 'travalingdatabase.cfu8y0yscmkf.eu-north-1.rds.amazonaws.com',
    user: 'admin',
    password: 'vaibhavsonawane',
    database: 'travalingdatabase',
    port: 3306
});

connection.connect((err) => {
    if (err) {
        console.error('Error connecting to the database:', err);
        return;
    }
    console.log('Connected to the AWS RDS database.');
});

module.exports = connection;
