from django.shortcuts import render  # type: ignore
import joblib  # type: ignore
import pandas as pd  # type: ignore
from .forms import PredictionForm
import logging

# Configure logging
logger = logging.getLogger(__name__)

# Load the model (use relative path or settings)
MODEL_PATH = r'C:\Users\debku\OneDrive\Desktop\heart_disease_prediction\heart_disease_prediction_model\heart_disease_risk_model.pkl'
try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    logger.error(f"Failed to load model: {e}")
    model = None  # Handle this case in prediction function

def predict_heart_disease(input_data):
    # Check if the model is loaded
    if model is None:
        return "Error: Prediction model is not available."

    # Convert form data (dictionary) into a DataFrame with the right column names
    try:
        df = pd.DataFrame([input_data])

        # Check if the input columns match the model's expected features
        expected_columns = model.feature_names_in_  # Assuming the model stores feature names
        missing_cols = set(expected_columns) - set(df.columns)

        if missing_cols:
            raise ValueError(f"Missing columns: {missing_cols}")

        # Make prediction
        prediction = model.predict(df)
        return 'The person has heart disease' if prediction[0] == 1 else 'The person does not have heart disease'
    except Exception as e:
        logger.error(f"Error during prediction: {e}")
        return "Error during prediction: Please check the input data."

def prediction_view(request):
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            # Extract cleaned form data
            input_data = form.cleaned_data

            # Make prediction using the model
            prediction = predict_heart_disease(input_data)

            # Render the result page with the prediction
            return render(request, 'prediction/result.html', {'prediction': prediction, 'form': form})
    else:
        form = PredictionForm()

    # Render the form page
    return render(request, 'prediction/form.html', {'form': form})
