from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib

# Load test data
X, y = load_diabetes(return_X_y=True)
_, X_test, _, y_test = train_test_split(X, y, test_size=0.2)

# Load model
model = joblib.load("model.pkl")
y_pred = model.predict(X_test)

# Evaluate
mse = mean_squared_error(y_test, y_pred)
print(f"Model MSE: {mse:.2f}")
