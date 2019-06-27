import pandas as pd
import random

def generate_production_data(n):
    df = pd.DataFrame()
    for _ in range(n):
        data = {
            "A": random.randint(0, 1000),
            "B": random.randint(0, 1000),
            "C": random.randint(0, 1000),
            "D": random.randint(0, 1000),
        }
        df = df.append(data, ignore_index=True)
    return df

print("Let's generate some data!")
n = int(input("How much data do you want? (must enter an integer)"))
df = generate_production_data(n)
columns = df.columns.tolist()
columns = [elem for elem in columns if "Unnamed" not in elem]
df = df[columns]
df.to_csv("production_data.csv", index=False)
