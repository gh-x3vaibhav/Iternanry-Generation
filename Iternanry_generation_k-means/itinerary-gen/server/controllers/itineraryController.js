const { spawn } = require('child_process');
const db = require('../config/db');

exports.generateItinerary = (req, res) => {
    const { user_id } = req.body;

    // Fetch user data from AWS RDS
    db.query('SELECT * FROM user_profiles WHERE user_id = ?', [user_id], (err, result) => {
        if (err) {
            return res.status(500).send('Database error');
        }

        const user = result[0];
        if (!user) {
            return res.status(404).send('User not found');
        }

        // Call Python K-Means prediction
        const pythonProcess = spawn('python', ['server/kmeans_prediction.py', user.expenses, user.vibe, user.previous_destinations.split(',').length]);

        pythonProcess.stdout.on('data', (data) => {
            const cluster = data.toString();
            // Based on the predicted cluster, generate a personalized itinerary
            res.json({
                user_id: user.user_id,
                destination: 'Switzerland',  // Example destination
                itinerary: [
                    { day: 1, activities: ['Visit Zurich', 'Explore Swiss Alps'], cost: 150 },
                    { day: 2, activities: ['Hiking in Interlaken'], cost: 120 }
                ]
            });
        });
    });
};
