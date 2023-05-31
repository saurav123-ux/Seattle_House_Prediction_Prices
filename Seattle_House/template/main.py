from flask import Flask, render_template,request
import pandas as pd
import pickle
import jinja2

app = Flask(__name__,template_folder='../template')
data = pd.read_csv('Cleaned_data_5.csv')
pipe = pickle.load(open("RandomForest4.pkl",'rb'))


@app.route('/')
def index():
    grades = data['grade']
    return render_template('index.html', grades=grades)

@app.route('/predict',methods=['POST'])
def predict():
    grade = float(request.form.get('grade'))
    bedrooms = float(request.form.get('bedrooms'))
    bathrooms = float(request.form.get('bathrooms'))
    sqft_living = float(request.form.get('sqft_living'))

    print(grade,bedrooms,bathrooms,sqft_living)
    input = pd.DataFrame([[grade,bedrooms,bathrooms,sqft_living]],columns=['grade','bedrooms','bathrooms','sqft_living'])
    prediction=pipe.predict(input)[0]



    return str(prediction)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
