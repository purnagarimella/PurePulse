import librosa
import numpy as np
from keras.models import load_model

# Function to extract MFCC features from an audio file
def extract_mfcc(audio_file):
    """
    Extracts MFCC features from an audio file.
    :param audio_file: Path to the audio file.
    :return: MFCC features extracted from the audio file.
    """
    y, sr = librosa.load(audio_file, sr=None)  # Load the audio file
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)  # Extract MFCC features
    mfcc = np.mean(mfcc.T, axis=0)  # Average over time (for each feature)
    return mfcc

# Load the trained model
model = load_model('slurred_speech_model.h5')

# Example audio file to test (replace with your actual file path)
audio_file = 'path/to/your/audio/file.wav'

# Extract MFCC features from the audio file
mfcc_features = extract_mfcc(audio_file)

# Expand dimensions to match the input shape expected by the model (batch size of 1)
mfcc_features = np.expand_dims(mfcc_features, axis=0)

# Make a prediction
prediction = model.predict(mfcc_features)

# Output the result
if prediction >= 0.5:
    print("Slurred speech detected!")
else:
    print("Speech is normal.")
