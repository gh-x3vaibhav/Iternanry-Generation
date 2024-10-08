const express = require('express');
const bodyParser = require('body-parser');
const itineraryRoutes = require('./routes/itineraryRoutes');

const app = express();
app.use(bodyParser.json());

app.use('/api/itinerary', itineraryRoutes);

app.listen(3000, () => {
    console.log('Server running on port 3000');
});
