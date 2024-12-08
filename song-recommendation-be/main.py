from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf
from sklearn.metrics.pairwise import cosine_similarity
from keras.src.legacy.saving import legacy_h5_format
from keras.src import models
from spotify import get_song_features,create_playlist
import pandas as pd
from tensorflow.keras import losses
from sklearn.neighbors import NearestNeighbors
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

class AdvancedParametricTanh(tf.keras.layers.Layer):
    def __init__(self, input_dim, alpha_init=1.5, beta_init=0.5, **kwargs):
        super(AdvancedParametricTanh, self).__init__(**kwargs)
        self.input_dim = input_dim
        self.alpha_init = alpha_init
        self.beta_init = beta_init

    def build(self, input_shape):
        self.alpha = self.add_weight(name='alpha', shape=(self.input_dim,),
                                     initializer=tf.keras.initializers.Constant(value=self.alpha_init), trainable=True)
        self.beta = self.add_weight(name='beta', shape=(self.input_dim,),
                                    initializer=tf.keras.initializers.Constant(value=self.beta_init), trainable=True)
        super(AdvancedParametricTanh, self).build(input_shape)

    def call(self, x):
        return self.alpha * tf.math.tanh(self.beta * x)


encoder = legacy_h5_format.load_model_from_hdf5('model_v1.h5',
                                              custom_objects={'AdvancedParametricTanh': AdvancedParametricTanh,
                                                              'mse': losses.MeanSquaredError()})
# encoder = models.Model(inputs=autoencoder.input, outputs=autoencoder.layers[0].output)


# autoencoder = legacy_h5_format.load_model_from_hdf5('model_v1_gradual.h5',
#                                               custom_objects={'mse': losses.MeanSquaredError()})
# encoder = models.Model(inputs=autoencoder.input, outputs=autoencoder.layers[2].output)

encoded_data = np.load('encoded_song_data.npy')
# encoded_data = np.load('encoded_song_data_gradual.npy')
song_data = pd.read_csv('spotify_data.csv')
knn = NearestNeighbors(n_neighbors=50, metric='cosine')
knn.fit(encoded_data)


@app.route('/', methods=['GET'])
def home():
    print(encoder.summary())
    return jsonify({"text": "Hello World!!!"})


@app.route('/find_similar_songs', methods=['POST'])
def find_similar_songs():
    print('hello')
    data = request.json
    song_name = data.get('song_name')

    song_features = np.array(get_song_features(song_name))
    if song_features is None:
        return jsonify({"error": "Song not found on Spotify"}), 404

    song_features = song_features.reshape(1, -1)
    print(encoded_data.shape)
    encoded_song = encoder.predict(song_features)
    print(encoded_song.shape)
    similarities = cosine_similarity(encoded_song, encoded_data)
    print(similarities[0].shape)
    similar_indices = np.argsort(similarities[0])[::-1][:100]
    # distances, indices = knn.kneighbors(encoded_song)


    similar_songs = []
    for index in similar_indices:
        song_info = {
            'id': song_data.iloc[index]['track_id'],
            'track_name': song_data.iloc[index]['track_name'],
            'artist_name': song_data.iloc[index]['artist_name'],
            'genre': song_data.iloc[index]['genre'],
            'similarity': float(similarities[0][index])  # Cast float32 to standard Python float
        }
        similar_songs.append(song_info)

    # for i, index in enumerate(indices[0]):
    #     song_info = {
    #         'id': song_data.iloc[index]['track_id'],
    #         'track_name': song_data.iloc[index]['track_name'],
    #         'artist_name': song_data.iloc[index]['artist_name'],
    #         'genre': song_data.iloc[index]['genre'],
    #         'similarity': float(1 - distances[0][i])  # Convert distance to similarity score
    #     }
    #     similar_songs.append(song_info)

    playlist_url=create_playlist(similar_songs,song_name)

    return jsonify({"similar_songs": similar_songs,"playlist_url":playlist_url})


if __name__ == '__main__':
    app.run(debug=True,port=8000)
