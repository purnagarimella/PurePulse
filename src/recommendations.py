# recommendations.py
from src.speech_analysis import detect_slurred_speech
from src.motion_analysis import detect_alcohol_effects
from src.health_data import get_user_health_data

def generate_recommendations(motion_data, audio_file, user_id):
    """
    Generates health recommendations based on the user's motion data, speech analysis, and health metrics.

    :param motion_data: List or array of motion data (accelerometer readings)
    :param audio_file: Path to the audio file for speech analysis
    :param user_id: Unique identifier for the user (to fetch personalized health data)
    :return: A list of personalized health recommendations
    """
    recommendations = []

    # Step 1: Analyze motion data to detect alcohol effects or movement abnormalities
    motion_result = detect_alcohol_effects(motion_data)
    if "alcohol effect detected" in motion_result:
        recommendations.append("We recommend taking a break and hydrating. Please rest and avoid strenuous activities.")

    # Step 2: Analyze speech data to detect slurred speech or alcohol consumption
    speech_result = detect_slurred_speech(audio_file)
    if "slurred speech detected" in speech_result:
        recommendations.append("Your speech may be impaired. It's important to stay safe and avoid activities like driving.")

    # Step 3: Retrieve user health data (e.g., hydration, exercise levels, sleep patterns)
    user_health_data = get_user_health_data(user_id)
    
    if user_health_data:
        hydration_status = user_health_data.get("hydration_status")
        exercise_level = user_health_data.get("exercise_level")
        sleep_quality = user_health_data.get("sleep_quality")
        
        # Step 4: Provide recommendations based on user health data
        if hydration_status == "dehydrated":
            recommendations.append("You may be dehydrated. Please drink more water to stay hydrated.")
        if exercise_level == "low":
            recommendations.append("Regular exercise is important for your overall well-being. Consider incorporating more physical activity into your routine.")
        if sleep_quality == "poor":
            recommendations.append("Your sleep quality seems to be poor. We recommend getting more restful sleep for better health.")
        
    # Step 5: General recommendations based on motion and speech results
    recommendations.append("Maintain a healthy lifestyle by staying active, hydrated, and getting enough sleep.")
    
    return recommendations


# Example usage:
if __name__ == "__main__":
    # Simulated motion data and audio file path for demonstration
    motion_data = [0.1, 0.2, 0.3, 0.5, 0.8, 1.1, 1.5, 1.8, 2.0, 2.3, 2.1]
    audio_file = "user_audio.wav"  # Example audio file path
    user_id = 1  # Example user ID
    
    recommendations = generate_recommendations(motion_data, audio_file, user_id)
    
    print("Health Recommendations:")
    for recommendation in recommendations:
        print(f"- {recommendation}")
