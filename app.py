from flask import Flask, render_template, request
from flask_cors import cross_origin
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open('life_expectancy_model.pkl', 'rb') as file:
    model = pickle.load(file)

print("Model Loaded:")

@app.route("/", methods=['GET'])
@cross_origin()
def index():
    return render_template("index.html")

@app.route("/predict", methods=['POST'])
@cross_origin()
def predict():
    if request.method == "POST":
        try:
            # Retrieve form data
            Country_ID = float(request.form['Country_ID'])
            Year = float(request.form['Year'])
            adult_mortality = float(request.form['Adult mortality'])
            infant_deaths = float(request.form['infant deaths'])
            alcohol = float(request.form['Alcohol'])
            percentage_expenditure = float(request.form['Percentage Expenditure'])
            hepatitis_b = float(request.form['Hepatitis B'])
            measles = float(request.form['Measles'])
            bmi = float(request.form['BMI'])
            under_five_deaths = float(request.form['under-five deaths'])
            polio = float(request.form['Polio'])
            total_expenditure = float(request.form['Total expenditure'])
            diphtheria = float(request.form['Diphtheria'])
            hiv_aids = float(request.form['HIV/AIDS'])
            gdp = float(request.form['GDP'])
            population = float(request.form['Population'])
            thinness_1_19_years = float(request.form['thinness  1-19 years'])
            thinness_5_9_years = float(request.form['thinness 5-9 years'])
            income_composition = float(request.form['Income composition of resources'])
            schooling = float(request.form['Schooling'])

            # Create the input array for prediction
            features = np.array([Country_ID, Year, adult_mortality, infant_deaths, alcohol,
                                percentage_expenditure, hepatitis_b, measles, bmi, under_five_deaths,
                                polio, total_expenditure, diphtheria, hiv_aids, gdp, population,
                                thinness_1_19_years, thinness_5_9_years, income_composition, schooling]).reshape(1, -1)

            # Predict the life expectancy using the loaded model
            pred = model.predict(features)
            output = pred[0]

            return render_template("predict.html", prediction=output)

        except Exception as e:
            return str(e)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
