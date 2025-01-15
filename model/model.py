import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib

# Load the dataset
df = pd.read_csv("C:/Users/Yash Agrawal/OneDrive/Desktop/spam_detection/spam.csv", encoding='ISO-8859-1')

# Preprocessing steps...
df.rename(columns={"v1": "Category", "v2": "Message"}, inplace=True)
df['Spam'] = df['Category'].apply(lambda x: 1 if x == 'spam' else 0)

# Create a machine learning pipeline
clf = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('nb', MultinomialNB())
])

# Train the model
X = df['Message']
y = df['Spam']
clf.fit(X, y)

# Save the model for later use
joblib.dump(clf, 'spam_model.pkl')

def detect_spam(email_text):
    model = joblib.load('spam_model.pkl')
    prediction = model.predict([email_text])
    return "This is a Spam Email!" if prediction[0] == 1 else "This is a Ham Email!"
