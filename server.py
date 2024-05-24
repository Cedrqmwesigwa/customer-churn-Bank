from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
import time

app= Flask(__name__)
model= joblib.load(open('classification_model.joblib', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

app.route('/return', methods= ['POST'])
def predict():
    float_features= [float(x) for x in request.form.values()]
    features= [np.array(float-features)]
    prediction= model.predict(features)
    return render_template('index.html',prediction text= f'species is {prediction}')

if __name__== "__main__":
    app.run(debug=True)