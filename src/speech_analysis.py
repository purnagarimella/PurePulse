# speech_analysis.py
import speech_recognition as sr
import librosa
import numpy as np

def detect_slurred_speech(audio_file):
    """
    Detects slurred speech from an audio file using basic audio analysis.
    In practice, this can be enhanced with more sophisticated models.

    :param audio_file: Path to the audio file (e.g., WAV, MP3)
    :return: A string indicating the detection result (e.g., 'slurred speech detected', 'normal speech')
    """
    
    print(f"Analyzing speech from {audio_file}...")
    
    # Step 1: Convert audio to text using SpeechRecognition
    recognizer = sr.Recognizer()
    
    try:
        # Load audio file
        with sr.AudioFile(audio_file) as source:
            audio = recognizer.record(source)  # Record the entire file
            
        # Perform speech-to-text using Google Web Speech API (can be replaced with other APIs)
        text = recognizer.recognize_google(audio)
        print(f"Recognized Text: {text}")
        
        # Here, we assume slurred speech detection is based on certain keywords or speech patterns
        # This is a basic implementation. A machine learning model would be more accurate.
        
        slurred_keywords = ["uh", "um", "err", "like"]  # Words often used in slurred speech
        text_lower = text.lower()
        
        if any(keyword in text_lower for keyword in slurred_keywords):
            return "Slurred speech detected"
        
        # Step 2: Audio feature extraction (using librosa to check speech quality)
        y, sr = librosa.load(audio_file)
        spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)
        
        # Compute average spectral centroid, which may correlate with speech clarity
        avg_spectral_centroid = np.mean(spectral_centroid)
        
        if avg_spectral_centroid < 1000:  # Low spectral centroid may indicate slurred speech
            return "Possible slurred speech detected"
        
        return "Normal speech detected"
    
    except Exception as e:
        print(f"Error in speech analysis: {e}")
        return "Error in speech analysis"


# Example of usage (you can remove this part in production):
if __name__ == "__main__":
    result = detect_slurred_speech("user_audio.wav")
    print(result)
