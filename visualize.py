import matplotlib.pyplot as plt

def plot_results(data, X_train, y_test, y_pred, ticker):
    test_dates = data.index[len(X_train):]

    plt.figure(figsize=(14, 6))

    plt.plot(test_dates, y_test.values, label="Actual Price")
    plt.plot(test_dates, y_pred, label="Predicted Price")

    plt.title(f"{ticker} Stock Prediction")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()
