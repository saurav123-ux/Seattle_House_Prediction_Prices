from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_grade_names', methods=['GET'])
def get_grade_names():
    response = jsonify({
        'grade': util.get_grade_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    sqft_living = float(request.form['sqft_living'])
    grade = request.form['grade']
    bedrooms= int(request.form['bedrooms'])
    bathrooms = int(request.form['bathrooms'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(grade,sqft_living,bathrooms,bedrooms)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()