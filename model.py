from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

feature_cols = ["Open", "High", "Low", "Close", "Volume"]

def train_model(data):
    X = data[feature_cols]
    y = data["Next_Close"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, shuffle=False
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    return model, X_test, y_test, y_pred, X_train


def predict_model(model, latest_data):
    feature_cols = ["Open", "High", "Low", "Close", "Volume"]

    if isinstance(latest_data.columns, pd.MultiIndex):
        latest_data.columns = latest_data.columns.get_level_values(0)

    X_live = latest_data[feature_cols]
    return model.predict(X_live)[0]
