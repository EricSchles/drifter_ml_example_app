from sklearn.linear_model import LinearRegression
import pandas as pd

df = pd.read_csv("training_data.csv")
linear_regression = LinearRegression()
linear_regression.fit(df[["A", "B", "C", "D"]], df["target"])

