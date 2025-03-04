import os
import numpy as np
import librosa
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split

# 1. Function to extract MFCC features from audio files
def extract_features(file_path, max_pad_len=50):
    audio, sample_rate = librosa.load(file_path, res_type='kaiser_fast')
    mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
    pad_width = max_pad_len - mfccs.shape[1]
    if pad_width > 0:
        mfccs = np.pad(mfccs, pad_width=((0, 0), (0, pad_width)), mode='constant')
    else:
        mfccs = mfccs[:, :max_pad_len]
    return mfccs

# 2. Prepare the dataset
def prepare_dataset(data_dir="dataset/"):
    labels = []
    features = []
    
    for label, category in enumerate(["normal", "slurred"]):  # Categories: normal or slurred
        folder = os.path.join(data_dir, category)
        for file in os.listdir(folder):
            if file.endswith(".wav"):  # Only process .wav files
                file_path = os.path.join(folder, file)
                mfccs = extract_features(file_path)
                features.append(mfccs)
                labels.append(label)

    # Convert to numpy arrays
    X = np.array(features)
    y = np.array(labels)

    # Reshape X for LSTM input (samples, timesteps, features)
    X = X.reshape(X.shape[0], X.shape[1], X.shape[2])

    # One-hot encoding for labels
    y = to_categorical(y, num_classes=2)

    return X, y

# 3. Build the LSTM model
def build_model(input_shape):
    model = Sequential([
        LSTM(128, return_sequences=True, input_shape=input_shape),
        Dropout(0.3),
        LSTM(64, return_sequences=False),
        Dropout(0.3),
        Dense(32, activation='relu'),
        Dense(2, activation='softmax')  # 2 output classes: normal, slurred
    ])

    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

# 4. Train the model
def train_model(X_train, y_train, X_test, y_test):
    model = build_model(input_shape=(X_train.shape[1], X_train.shape[2]))
    model.fit(X_train, y_train, epochs=30, batch_size=16, validation_data=(X_test, y_test))
    model.save("slurred_speech_model.h5")
    print("Model saved successfully as 'slurred_speech_model.h5'")
    return model

# 5. Predict function for new audio samples
def predict_speech(file_path, model):
    mfccs = extract_features(file_path)
    mfccs = np.expand_dims(mfccs, axis=0)  # Reshape for LSTM model input
    prediction = model.predict(mfccs)
    label = np.argmax(prediction)

    if label == 0:
        return "Normal Speech"
    else:
        return "Slurred Speech"

# Main function to train or predict
if __name__ == "__main__":
    # 1. Prepare the dataset
    X, y = prepare_dataset(data_dir="dataset/")  # Replace with the actual path of your dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 2. Train the model
    model = train_model(X_train, y_train, X_test, y_test)

    # 3. Use the model to predict on a new audio file
    file_path = "test_audio.wav"  # Replace with your test file path
    print(predict_speech(file_path, model))
