const express = require('express');
const bodyParser = require('body-parser');
const itineraryRoutes = require('./routes/itineraryRoutes');

const app = express();
app.use(bodyParser.json());

app.use('/itinerary', itineraryRoutes);

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
