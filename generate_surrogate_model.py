import joblib
from sklearn import linear_model
import pandas as pd

linear_regression = joblib.load("regression.joblib")
surrogate_model = linear_model.LinearRegression(**linear_regression.get_params())
df = pd.read_csv("production_data.csv")
df["target"] = linear_regression.predict(df[["A", "B", "C", "D"]])
surrogate_model.fit(df[["A", "B", "C", "D"]], df["target"])
joblib.dump(surrogate_model, "surrogate.joblib")
