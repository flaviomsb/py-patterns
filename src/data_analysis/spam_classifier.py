import os
import io
import json
import pandas as pd
from pandas import DataFrame
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

current_dir = os.path.dirname(__file__)

def readFiles(path):
    path = os.path.join(current_dir, f"../../support_files/{path}")
    for root, _, filenames in os.walk(path):
        for filename in filenames:
            path = os.path.join(root, filename)

            inBody = False
            lines = []
            f = io.open(path, 'r', encoding='latin1')
            for line in f:
                if inBody:
                    lines.append(line)
                elif line == '\n':
                    inBody = True
            f.close()
            message = '\n'.join(lines)
            yield path, message


def dataFrameFromDirectory(path, classification):
    rows = []
    for _, message in readFiles(path):
        rows.append({'message': message, 'class': classification})

    return DataFrame(rows)

data = DataFrame({'message': [], 'class': []})

data = pd.concat([data, dataFrameFromDirectory("emails/spam", "spam")])
data = pd.concat([data, dataFrameFromDirectory("emails/ham", "not spam")])

vectorizer = CountVectorizer()
counts = vectorizer.fit_transform(data['message'].values)

classifier = MultinomialNB()
targets = data['class'].values
classifier.fit(counts, targets)

examples = ['Free utility bills!', "Hi Paul, when are you going to Mexico?", "Lottery ticket to success"]
example_counts = vectorizer.transform(examples)
predictions = classifier.predict(example_counts)

print(json.dumps(dict(zip(examples, predictions)), indent=4))

