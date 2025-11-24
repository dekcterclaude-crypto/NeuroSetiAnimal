import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model.selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

data = {
    "text": [
        "я рад", "я очень счастлив", "мне нравится этот день", "это отличный фильм",
        "я грустный", "мне плохо", "ужасное настроение", "где сладости?", "гони бабки", "где все"
        ],
        "label":[1,1,1,1,0,0,0,0,0]
    }

df = pd.DataFrame(data)

Vectorizer = CountVectorizer()
x = vectorizer.fit_transform(df["text"])
y = df["label"]


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state=42)


model =MLPClassifier(hidden_layer_sizes=(10,), max_iter=1000)
model.fit(x_train, y_train)


