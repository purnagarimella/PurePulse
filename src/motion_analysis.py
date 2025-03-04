# motion_analysis.py
import numpy as np

def detect_alcohol_effects(motion_data):
    """
    Detects potential effects of alcohol consumption based on motion data.
    This basic implementation looks for abnormal patterns in movement.

    :param motion_data: List or array of motion data (e.g., accelerometer readings)
    :return: A string indicating the detection result (e.g., 'alcohol effect detected', 'normal movement')
    """
    print("Analyzing motion data...")
    
    # Convert motion data to a numpy array for easier manipulation
    motion_data = np.array(motion_data)
    
    # Step 1: Analyze the magnitude of acceleration
    # We assume the motion data represents accelerometer readings in x, y, z axes.
    # For simplicity, we'll assume `motion_data` is a 1D array (e.g., total movement magnitude).
    
    # Compute the total movement magnitude (or you can use the raw x, y, z components for a more detailed analysis)
    movement_magnitude = np.linalg.norm(motion_data)
    
    print(f"Total Movement Magnitude: {movement_magnitude}")
    
    # Step 2: Look for erratic movement patterns
    # In a real-world application, you would analyze the pattern of movement (e.g., step irregularities, sudden stops).
    
    # For simplicity, we assume that alcohol-induced movement might involve sudden erratic movements.
    # Here, we define a threshold for normal movement vs. erratic movement.
    movement_threshold = 2.0  # Arbitrary threshold for abnormal movement magnitude
    
    if movement_magnitude > movement_threshold:
        # We assume a higher magnitude indicates alcohol effect
        return "Possible alcohol effect detected"
    
    # Step 3: Analyze motion smoothness
    # If the user is walking, their motion should follow a relatively smooth pattern. Abrupt changes might indicate intoxication.
    motion_diff = np.diff(motion_data)
    smoothness = np.mean(np.abs(motion_diff))  # Low smoothness might indicate stumbling

    print(f"Motion Smoothness: {smoothness}")
    
    # Define a threshold for smoothness
    smoothness_threshold = 0.5
    
    if smoothness > smoothness_threshold:
        return "Possible alcohol effect detected (erratic movement)"
    
    return "Normal movement detected"


# Example of usage (you can remove this part in production):
if __name__ == "__main__":
    # Simulated motion data (replace with actual accelerometer data)
    motion_data = [0.1, 0.2, 0.3, 0.5, 0.8, 1.1, 1.5, 1.8, 2.0, 2.3, 2.1]
    result = detect_alcohol_effects(motion_data)
    print(result)
