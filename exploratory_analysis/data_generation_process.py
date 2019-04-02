import pandas as pd
import numpy as np
import joblib

df = pd.DataFrame()
for _ in range(10000):
    a = np.random.normal(0, 1)
    b = np.random.normal(0, 3)
    c = np.random.normal(12, 4)
    if a + b + c > 11:
        target = 1
    else:
        target = 0
    df = df.append({
        "A": a,
        "B": b,
        "C": c,
        "target": target
    }, ignore_index=True)

df.to_csv("data.csv", index=False)
