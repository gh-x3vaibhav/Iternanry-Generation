const express = require('express');
const router = express.Router();
const itineraryController = require('../controllers/itineraryController');

router.get('/generate', itineraryController.generateItinerary);

module.exports = router;
