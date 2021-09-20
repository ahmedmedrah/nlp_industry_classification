import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__, static_url_path='/static')
model = pickle.load(open('voting.pkl', 'rb'))
rev_lbl_mapper = {0:'IT', 1:'Marketing', 2:'Education', 3:'Accountancy'}

@app.route('/')
def index():
    return render_template('predict.html')

@app.route('/predict',methods=['POST'])
def predict():

    print(request.get_json(force=True))
    job_title = request.get_json(force=True)['job_title']
    print(job_title)
    prediction = model.predict([job_title])[0]    
    output = rev_lbl_mapper[prediction]
    print(output)
    response = jsonify({'industry':output})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    app.run(debug=True)