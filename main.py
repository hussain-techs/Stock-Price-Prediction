from data_loader import get_stock_data
from model import train_model, predict_model
from visualize import plot_results
import yfinance as yf

ticker = "AAPL"

# Load data
data = get_stock_data(ticker)

# Train model
model, X_test, y_test, y_pred, X_train = train_model(data)

# Plot results
plot_results(data, X_train, y_test, y_pred, ticker)

# Live prediction
latest_data = yf.download(ticker, period="1d")
prediction = predict_model(model, latest_data)

print("\n--- Live Prediction ---")
print("Next Close Price:", prediction)
