from flask import Flask, request, jsonify

app = Flask(__name__)

# Temporary storage (replace with a database later)
heart_rate_data = []

@app.route('/update_heart_rate', methods=['POST'])
def update_heart_rate():
    data = request.json
    heart_rate = data.get("heart_rate")
    hrv = data.get("hrv")

    if heart_rate is None or hrv is None:
        return jsonify({"error": "Invalid data"}), 400

    # Store data
    heart_rate_data.append({"heart_rate": heart_rate, "hrv": hrv})

    print(f"Received: Heart Rate={heart_rate} BPM, HRV={hrv} ms")
    return jsonify({"message": "Data received successfully", "data": data})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
