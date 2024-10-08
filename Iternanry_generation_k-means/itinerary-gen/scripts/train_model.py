import pandas as pd
from sklearn.cluster import KMeans
import joblib
from preprocess import preprocess_data

# Load and preprocess data
file_path = 'data/user_profiles.csv'
X = preprocess_data(file_path)

# Train K-Means model
kmeans = KMeans(n_clusters=5, random_state=0)
kmeans.fit(X)

# Save the model
joblib.dump(kmeans, 'models/kmeans_model.pkl')
