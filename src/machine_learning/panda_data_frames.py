import pandas as pd

data = {
    "name": ["Joe", "Tom", "Nancy"],
    "age": [20, 32, 27],
    "city": ["Austin", "Chicago", "Dallas"],
}

df = pd.DataFrame(data=data)

print(df)
