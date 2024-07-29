from flask import Flask, request, render_template
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Import ridge regressor and standard scaler pickle
ridge_model = pickle.load(open('models/ridge.pkl', 'rb'))
standard_scaler = pickle.load(open('models/scaler.pkl', 'rb'))

@app.route("/")
def index():
    return render_template('home.html')

@app.route('/predictdata', methods=['POST'])
def predict_datapoint():
    if request.method == "POST":
        try:
            # Get values from form
            temperature = float(request.form.get('Temperature'))
            rh = float(request.form.get('RH'))
            ws = float(request.form.get('Ws'))
            rain = float(request.form.get('Rain'))
            ffmc = float(request.form.get('FFMC'))
            dmc = float(request.form.get('DMC'))
            isi = float(request.form.get('ISI'))
            classes = float(request.form.get('Classes'))
            region = float(request.form.get('Region'))

            # Prepare new data for prediction
            new_data = np.array([[temperature, rh, ws, rain, ffmc, dmc, isi, classes, region]])
            new_data_scaled = standard_scaler.transform(new_data)
            result = ridge_model.predict(new_data_scaled)

            return render_template('home.html', results=result[0])
        except Exception as e:
            return str(e)  # For debugging, display error message

    return render_template('home.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0")
