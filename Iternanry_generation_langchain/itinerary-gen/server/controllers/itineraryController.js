const connection = require('../config/db');
const { spawn } = require('child_process');

exports.generateItinerary = (req, res) => {
    // Fetch user data from AWS RDS
    connection.query('SELECT * FROM users WHERE user_id = ?', [req.query.user_id], (error, results) => {
        if (error) {
            console.error('Error fetching data:', error);
            return res.status(500).send('Error fetching data from database.');
        }

        // Call LangChain script with user data
        const pythonProcess = spawn('python', ['langchain/generate_itinerary.py']);

        // Send user data to LangChain Python process
        pythonProcess.stdin.write(JSON.stringify(results));
        pythonProcess.stdin.end();

        // Capture itinerary output from LangChain
        pythonProcess.stdout.on('data', (data) => {
            const itinerary = data.toString();
            res.json({ itinerary });
        });

        pythonProcess.stderr.on('data', (data) => {
            console.error('Error from LangChain:', data.toString());
        });
    });
};
