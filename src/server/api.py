import sys
import os

print(os.getcwd())
sys.path.append(os.getcwd())

from flask import Flask, jsonify, request, render_template
from src.model.model import Churn
from src.modulos.parser import parser

app = Flask(__name__, template_folder='../templates', static_folder='../static')
churn = Churn()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict(): 
    values = parser(request)
    result = churn.predict(values)
    return render_template('home.html',  tables=[result.to_html(classes='data', header="true")])

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 33507))
    app.run(host="0.0.0.0",port=port)

