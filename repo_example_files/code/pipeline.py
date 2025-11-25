import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error

# 1. Load data + define features and target
df = pd.read_csv('../data/football_wages.csv')

# Drop categorical column and target
X = df.drop(columns=["log_wages", "nationality_name"])
y = df["log_wages"]

# 2. Train / test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# 3. Build KNN pipeline
knn_pipeline = Pipeline(steps=[
    ("scaler", StandardScaler()),
    ("knn", KNeighborsRegressor(n_neighbors=5))
])

# 4. Train the model
knn_pipeline.fit(X_train, y_train)

# 5. Evaluate using MAE
y_pred = knn_pipeline.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)

print(f"Mean Absolute Error (MAE) on test set: {mae:.4f}")
