import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.feature_extraction.text import TfidfVectorizer

def preprocess_data(file_path):
    df = pd.read_csv("file_path")

    # Scale expenses
    scaler = StandardScaler()
    df['expenses'] = scaler.fit_transform(df[['expenses']])
    
    # One-hot encode vibe and favorite activities
    encoder = OneHotEncoder()
    vibe_encoded = encoder.fit_transform(df[['vibe']]).toarray()
    activities_encoded = encoder.fit_transform(df[['favorite_activities']]).toarray()

    # TF-IDF vectorize reviews
    tfidf = TfidfVectorizer(max_features=100)
    review_vectors = tfidf.fit_transform(df['reviews']).toarray()

    # Concatenate all features
    features = pd.concat([df[['expenses']], pd.DataFrame(vibe_encoded), pd.DataFrame(activities_encoded), pd.DataFrame(review_vectors)], axis=1)
    
    return features
