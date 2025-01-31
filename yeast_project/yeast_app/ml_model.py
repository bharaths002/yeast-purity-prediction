import tensorflow as tf
from tensorflow.keras.models import load_model
import os
import numpy as np
import joblib

# Define the path to the model and scaler files
model_path = os.path.join(os.path.dirname(__file__), 'models', 'transfer_learning_model.h5')
scaler_path = os.path.join(os.path.dirname(__file__), 'models', 'scaler.pkl')

# Load your pre-trained model and scaler
model = load_model(model_path)
scaler = joblib.load(scaler_path)


def predict_purity(molasses_amount, grain_starch_amount, potato_starch_amount, water, nutrients_vitamins, emulsifiers):
    # Preprocess input data
    input_data = np.array(
        [[molasses_amount, grain_starch_amount, potato_starch_amount, water, nutrients_vitamins, emulsifiers]],
        dtype=np.float32)
    input_data_scaled = scaler.transform(input_data)

    # Predict purity using the model
    prediction = model.predict(input_data_scaled)

    # Convert output to percentage
    purity_percentage = prediction[0][0] * 100

    # Ensure the purity percentage is in a realistic range (e.g., 0 to 100)
    purity_percentage = min(max(purity_percentage, 0), 100)

    return purity_percentage
