from flask import Flask, request, jsonify
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

application = Flask(__name__)

@application.route("/")
def index():
    return "Your Flask App Works! V1.0"

def load_model(input_text):
    with open('basic_classifier.pkl', 'rb') as fid:
        loaded_model = pickle.load(fid)
    with open('count_vectorizer.pkl', 'rb') as vd:
        vectorizer = pickle.load(vd)
    prediction = loaded_model.predict(vectorizer.transform([input_text]))[0]
    return prediction

@application.route("/predict", methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        input_text = request.form['input_text']
        prediction = load_model(input_text)
        return jsonify({'input': input_text, 'prediction': prediction})
    

if __name__ == "__main__":
    application.run(port=5000, debug=True)
