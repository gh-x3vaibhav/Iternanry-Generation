import pickle
import numpy as np

# Load the trained K-Means model
with open('../models/kmeans_model.pkl', 'rb') as f:
    kmeans = pickle.load(f)

def predict_cluster(expenses, vibe, destinations_count):
    # Assuming 'vibe' is already encoded
    user_data = np.array([[expenses, vibe, destinations_count]])
    cluster = kmeans.predict(user_data)
    return cluster[0]
