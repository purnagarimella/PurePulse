# main.py
from src import collect_health_data, detect_slurred_speech, detect_alcohol_effects, analyze_health_data

def main():
    # User ID (in a real app, this could be dynamically assigned based on the logged-in user)
    user_id = "user_12345"
    
    # Step 1: Collect User's Health Data
    print("Collecting health data...")
    user_data = collect_health_data(user_id)
    
    # Print collected data for debugging purposes (can be removed later)
    print(f"Collected Health Data: {user_data}")
    
    # Step 2: Analyze Health Data for General Recommendations
    print("Analyzing health data...")
    health_advice = analyze_health_data(user_data)
    print(f"Health Advice: {health_advice}")
    
    # Step 3: Detect Slurred Speech (Simulated for now)
    audio_file = "user_audio.wav"  # Sample audio file
    print(f"Detecting slurred speech from audio file: {audio_file}...")
    speech_detection_result = detect_slurred_speech(audio_file)
    print(f"Speech Detection Result: {speech_detection_result}")
    
    # Step 4: Detect Alcohol Effect from Motion Data
    # Sample motion data (replace with real sensor data or accelerometer input)
    motion_data = [0.1, 0.2, 0.5, 0.9, 1.3, 0.8, 0.5, 1.1, 0.3, 0.6]  # Simulated motion data
    print("Detecting alcohol effect based on motion data...")
    alcohol_detection_result = detect_alcohol_effects(motion_data)
    print(f"Alcohol Effect Detection Result: {alcohol_detection_result}")
    
    # Final output (you can further extend the app to provide personalized advice based on all the results)
    print("\n--- PurePulse Report ---")
    print(f"Health Advice: {health_advice}")
    print(f"Speech Detection: {speech_detection_result}")
    print(f"Alcohol Effect Detection: {alcohol_detection_result}")

if __name__ == "__main__":
    main()
