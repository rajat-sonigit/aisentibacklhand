import nltk
import joblib
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Download necessary NLTK data
nltk.download("punkt")
nltk.download("stopwords")

# Sample dataset for training
training_data = [
    ("I love my job and my team!", "Positive"),
    ("I enjoy coming to work every day.", "Positive"),
    ("The work environment is toxic.", "Negative"),
    ("I feel stressed and overworked.", "Negative"),
]

# Preprocessing function
def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stopwords.words("english")]
    return " ".join(tokens)

# Prepare data
texts, labels = zip(*training_data)
processed_texts = [preprocess_text(text) for text in texts]

# Train model
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(processed_texts)
model = MultinomialNB()
model.fit(X_train, labels)

# Save model and vectorizer
joblib.dump(model, "analytics/sentiment_model.pkl")
joblib.dump(vectorizer, "analytics/vectorizer.pkl")

print("Model trained and saved successfully!")
