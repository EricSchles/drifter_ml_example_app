from sklearn.linear_model import LinearRegression
import pandas as pd
import joblib

def main():
    df = pd.read_csv("training_data.csv")
    linear_regression = LinearRegression()
    linear_regression.fit(df[["A", "B", "C", "D"]], df["target"])
    joblib.dump(linear_regression, "regression.joblib")

if __name__ == '__main__':
    main()
