
# Personalized Itinerary Generation using LangChain, Node.js, and AWS

This project generates personalized travel itineraries using LangChain and K-means clustering, integrated with AWS RDS for data storage and Node.js for backend operations.

## Overview

This system takes user preferences, past trip history, and additional data to provide personalized itineraries. The itinerary generation leverages LangChain to interface with language models and K-means clustering to group users based on their travel patterns.

The backend is powered by Node.js, and data is stored in an AWS RDS MySQL database. The Python scripts handle the preprocessing and LangChain interactions.

## Features

- **Personalized Itinerary Generation:** Generates recommendations based on user history and preferences.
- **Data Integration with AWS RDS:** Stores user data in AWS RDS and fetches real-time updates.
- **K-Means Clustering:** Segments users based on their travel preferences and history to enhance recommendations.
- **LangChain Integration:** Uses language models to provide rich, personalized responses and itineraries.

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/itinerary-gen.git
    cd itinerary-gen
    ```

2. Install the required dependencies for the Node.js backend:

    ```bash
    npm install
    ```

3. Set up Python dependencies for the LangChain and clustering scripts:

    ```bash
    pip install -r requirements.txt
    ```

4. Configure your AWS RDS instance and update the credentials in `server/config/db.js`.

5. Ensure you have an OpenAI API key and add it to `langchain/openai_config.py`.

## Running the Application

1. Start the Node.js server:

    ```bash
    node server/app.js
    ```

2. Use the provided routes to request personalized itineraries.

3. Train the K-Means clustering model:

    ```bash
    python scripts/train_model.py
    ```

4. To generate an itinerary using LangChain:

    ```bash
    python langchain/generate_itinerary.py --user_id=<USER_ID>
    ```

## Example

To generate a personalized itinerary for user `101`, you can call the LangChain script as follows:

```bash
python langchain/generate_itinerary.py --user_id=101
```

This will generate a detailed itinerary based on the user's preferences and past trips.

---

### Note

Make sure your database contains the required user profiles and that the AWS RDS instance is accessible.
