import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
# 1. Create a sample dataset (replace with your actual data loading)
# A real dataset would have columns like 'timestamp', 'temperature',␣
↪'consumption', etc.
data = {
'temperature': [20, 22, 25, 28, 21, 19, 24, 26, 23, 20],
'hour_of_day': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
'energy_consumption': [100, 110, 130, 150, 105, 95, 125, 140, 115, 100]
}
df = pd.DataFrame(data)
# 2. Define features (X) and target variable (y)
X = df[['temperature'
,
'hour_of_day']] # Features
y = df['energy_consumption'] # Target variable
# 3. Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,␣
↪random_state=42)
# 4. Initialize and train the model
model = LinearRegression()
model.fit(X_train, y_train)
# 5. Make predictions
predictions = model.predict(X_test)
# 6. Evaluate the model
mae = mean_absolute_error(y_test, predictions)
rmse = np.sqrt(mean_squared_error(y_test, predictions))
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
1
# 7. Visualize actual vs. predicted (simple plot)
plt.figure(figsize=(10, 6))
plt.scatter(y_test, predictions, edgecolors=(0, 0, 0))
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=4) # Diagonal line
plt.xlabel('Actual Consumption')
plt.ylabel('Predicted Consumption')
plt.title('Actual vs. Predicted Energy Consumption')
plt.show()
# 8. Example of making a new prediction
new_data = pd.DataFrame({'temperature': [27], 'hour_of_day': [11]})
predicted_consumption = model.predict(new_data)
print(f"\nPredicted consumption for new data: {predicted_consumption[0]:.2f}")
