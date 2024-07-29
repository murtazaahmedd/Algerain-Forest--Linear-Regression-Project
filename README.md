# Algerian Forest Linear Regression Project

## Overview

The Algerian Forest Linear Regression Project aims to predict the Fire Weather Index (FWI) in Algerian forests using various meteorological and environmental features. This machine learning project uses linear regression models to assess fire risk based on historical data.

## Features

- **Predictive Modeling**: Uses a linear regression model to predict FWI.
- **Data Preprocessing**: Includes data normalization and scaling.
- **Web Interface**: Allows users to input data and get predictions via a web form.

## Project Structure

- `app.py`: The main Flask application for running the web server and handling predictions.
- `models/`: Directory containing pre-trained models and scaler files.
  - `ridge.pkl`: The trained Ridge Regression model.
  - `scaler.pkl`: The Standard Scaler used for feature scaling.
- `templates/`: Directory containing HTML templates for the web interface.
  - `home.html`: The main page with a form to input data and display predictions.
- `static/`: Directory for static files like CSS stylesheets.
  - `styles.css`: The stylesheet for styling the web interface.
- `data/`: Directory for storing datasets (if applicable).

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/murtazaahmedd/Algerian-Forest-Linear-Regression-Project.git
   cd Algerian-Forest-Linear-Regression-Project
   ```

2. **Create a virtual environment** (optional but recommended):

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install the required packages**:

   ```bash
   pip install -r requirements.txt
   ```

   Ensure you have a `requirements.txt` file with the following dependencies:

   ```
   Flask==2.1.0
   scikit-learn==1.2.0
   numpy==1.24.0
   pandas==2.1.0
   ```

5. **Download or train the model**:

   Ensure that you have the pre-trained model (`ridge.pkl`) and scaler (`scaler.pkl`) in the `models/` directory.

## Usage

1. **Run the Flask application**:

   ```bash
   python application.py
   ```

   The web server will start on `http://127.0.0.1:5000/`.

2. **Navigate to the web interface**:

   Open a web browser and go to `http://127.0.0.1:5000/`. You will see a form to enter data for prediction.

3. **Enter Data**:

   Fill out the form with the required data and click "Predict" to get the FWI prediction.

## Example

Here is a brief example of how to use the web interface:

- **Temperature**: 30
- **Relative Humidity (RH)**: 50
- **Wind Speed (Ws)**: 10
- **Rainfall (Rain)**: 0
- **FFMC**: 85
- **DMC**: 25
- **ISI**: 5
- **Classes**: 1
- **Region**: 2

Click "Predict" to receive the FWI prediction.

## Contributing
Contributions are welcome! Please fork the repository, make your changes, and submit a pull request. Ensure that your changes are well-tested and documented.
## Contact

For any questions or inquiries, please contact murtazaahmad087@gmail.com
