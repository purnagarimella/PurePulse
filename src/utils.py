# utils.py

import os
import logging
from datetime import datetime

# Set up logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_current_timestamp():
    """
    Returns the current timestamp as a string in 'YYYY-MM-DD HH:MM:SS' format.

    :return: A string representing the current timestamp.
    """
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def create_directory(directory_path):
    """
    Creates a directory if it doesn't already exist.

    :param directory_path: Path of the directory to be created.
    """
    try:
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
            logging.info(f"Directory created at: {directory_path}")
        else:
            logging.info(f"Directory already exists at: {directory_path}")
    except Exception as e:
        logging.error(f"Failed to create directory {directory_path}: {str(e)}")

def save_audio_file(file_path, audio_data):
    """
    Save the audio data to a file at the specified path.

    :param file_path: Path to the file where audio data will be saved.
    :param audio_data: Audio data to be saved (in bytes).
    """
    try:
        with open(file_path, 'wb') as f:
            f.write(audio_data)
            logging.info(f"Audio file saved at: {file_path}")
    except Exception as e:
        logging.error(f"Failed to save audio file: {str(e)}")

def read_audio_file(file_path):
    """
    Reads the content of an audio file.

    :param file_path: Path to the audio file.
    :return: The audio data read from the file (in bytes).
    """
    try:
        with open(file_path, 'rb') as f:
            audio_data = f.read()
            logging.info(f"Audio file read from: {file_path}")
            return audio_data
    except Exception as e:
        logging.error(f"Failed to read audio file: {str(e)}")
        return None

def validate_motion_data(motion_data):
    """
    Validates motion data for expected format (list/array of numeric values).
    
    :param motion_data: List or array of motion data.
    :return: Boolean indicating whether the motion data is valid.
    """
    if isinstance(motion_data, (list, np.ndarray)):
        if all(isinstance(i, (int, float)) for i in motion_data):
            logging.info("Motion data is valid.")
            return True
        else:
            logging.error("Motion data contains non-numeric values.")
    else:
        logging.error("Motion data is not in list/array format.")
    return False

def log_user_activity(user_id, activity):
    """
    Logs user activity, such as recommendations received or actions taken.
    
    :param user_id: Unique identifier of the user.
    :param activity: A string describing the activity (e.g., 'received recommendation').
    """
    timestamp = get_current_timestamp()
    logging.info(f"User {user_id} activity at {timestamp}: {activity}")
