import pandas as pd
import numpy as np
import os
from sklearn.ensemble import RandomForestClassifier
 
current_dir = os.path.dirname(__file__)
df = pd.read_csv(os.path.join(current_dir, '../../support_files/past_hires.csv'), header=0)

print(df.head())

def normalize_yn(val): 
    return {'Y': 1, 'N': 0}[val]

def normalize_ed_level(val):
    return {'BS': 0, 'MS': 1, 'PhD': 2}[val]

def translate_decision(val):
    return 'Yes' if val[0] == 1 else 'No'

fields = {
    'Hired': normalize_yn,
    'Employed?': normalize_yn,
    'Top-tier school': normalize_yn,
    'Interned': normalize_yn,
    'Level of Education': normalize_ed_level,
}

for field, normalizer in fields.items():
    df[field] = df[field].apply(normalizer)

print(df.head())

features = list(df.columns[:6])

y = df['Hired']
X = np.array(df[features])

classifier = RandomForestClassifier(n_estimators=10)
classifier = classifier.fit(X, y)

print('Predict an employed person with 10 years of experience:')
decision = classifier.predict([[10, 1, 4, 0, 0, 0]])
print(translate_decision(decision))

print('Predict an unemployed person with 1 year of experience and only one previous job:')
decision = classifier.predict([[1, 0, 1, 0, 0, 0]])
print(translate_decision(decision))
