import pandas as pd
from sklearn.cluster import KMeans
import joblib
from preprocess import preprocess_data  # Make sure you have preprocess.py in the same directory

def train_kmeans(file_path, n_clusters=5, model_output='models/kmeans_model.pkl'):
    # Preprocess the data
    features = preprocess_data(file_path)

    # Train the K-Means model
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(features)

    # Save the model
    joblib.dump(kmeans, model_output)
    print(f"K-Means model trained and saved to {model_output}")

def predict_cluster(model_input, new_data):
    # Load the trained K-Means model
    kmeans = joblib.load(model_input)

    # Predict the cluster for the new data
    predictions = kmeans.predict(new_data)
    return predictions

if __name__ == "__main__":
    # Define the file path to the CSV file
    file_path = 'data/user_profiles.csv'  # Update this path if necessary
    
    # Train the K-Means model
    train_kmeans(file_path, n_clusters=5)

    # Example of predicting a cluster for new data
    # new_data = ... (Load or define your new data for prediction here)
    # predicted_clusters = predict_cluster('models/kmeans_model.pkl', new_data)
    # print(predicted_clusters)
