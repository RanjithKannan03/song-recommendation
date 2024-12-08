# Song Recommendation System

Welcome to the Song Recommendation System! This project uses advanced machine learning techniques and Spotify song features to recommend songs similar to the one you input. The system leverages an autoencoder model and a Flask API to efficiently find and serve recommendations.

---

## Features

- **Input-Based Recommendations:** Provide a song name, and the system will return 50 similar songs.
- **Spotify Integration:** Fetch song details and features using Spotify's Web API.
- **Efficient Machine Learning:** Built with a custom-trained autoencoder model to encode and compare song features.
- **Fast API Responses:** Flask serves as the backend, ensuring low-latency responses.
- **Scalable and Robust:** Handles large datasets with over 1.2 million songs.

---

## Technologies Used

### Backend
- **Flask**: Backend API for handling requests and providing song recommendations.
- **Spotipy**: Python wrapper for the Spotify Web API.
- **TensorFlow**: For the custom autoencoder model.

### Dataset
- Spotify dataset with the following features:
  - `danceability`, `energy`, `key`, `loudness`, `acousticness`, `instrumentalness`, `liveness`, `valence`, `tempo`, `genre`, and more.


