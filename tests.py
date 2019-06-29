from drifter_ml.regression_tests import RegressionTests
import pandas as pd
import joblib

surrogate_model = joblib.load("surrogate.joblib")
validation = pd.read_csv("validation_data.csv")
columns = ["A", "B", "C", "D"]
reg_tests = RegressionTests(
    surrogate_model,
    validation,
    "target",
    columns
)

def test_difference():
    assert reg_tests.regression_testing(200, 200)


    
