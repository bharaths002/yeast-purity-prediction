import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import joblib

# Example training data
x_train = np.random.rand(100, 6)  # 100 samples, 6 features
y_train = np.random.rand(100, 1)  # 100 samples, 1 target

# Scale inputs
scaler = MinMaxScaler()
x_train_scaled = scaler.fit_transform(x_train)

# Save the fitted scaler
scaler_path = 'yeast_app/models/scaler.pkl'
joblib.dump(scaler, scaler_path)

# Define the model
model = Sequential([
    Dense(64, activation='relu', input_shape=(x_train_scaled.shape[1],)),
    Dense(64, activation='relu'),
    Dense(1, activation='sigmoid')  # Sigmoid output for normalization
])

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])

# Train the model
model.fit(x_train_scaled, y_train, epochs=50, batch_size=32)

# Save the model
model.save('yeast_app/models/transfer_learning_model.h5')
