from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # This allows your website to talk to the API without errors

@app.route('/predict', methods=['POST'])
def predict_crop():
    data = request.json
    
    # Extract data from the website
    soil = data.get('soil_type')
    ph = float(data.get('ph'))
    temp = float(data.get('temp'))
    rain = float(data.get('rainfall'))
    
    # Advanced Recommendation Logic
    recommendation = "Maize" # Default
    advice = "Ensure balanced NPK fertilizers."

    if soil == "Black":
        if rain > 200:
            recommendation = "Rice"
            advice = "Ideal for water-intensive cultivation."
        else:
            recommendation = "Cotton"
            advice = "Ensure good drainage during monsoon."
            
    elif soil == "Alluvial":
        if temp < 20:
            recommendation = "Wheat"
        else:
            recommendation = "Sugarcane"

    return jsonify({
        "crop": recommendation,
        "advice": advice,
        "status": "Success"
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)