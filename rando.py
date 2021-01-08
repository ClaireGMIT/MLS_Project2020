# flask for web app.
import flask as fl

# numpy for numerical work.
import numpy as np

# numpy for numerical work.
from flask import  Flask, jsonify, request

# Create a new web app.
app = fl.Flask(__name__)

# Add root route.
@app.route("/")
def home():
    return app.send_static_file('index1.html')

@app.route('/predict', methods=['POST']) 
def predict():
    return {"value" : model.pkl}


if __name__ == '__main__':
    app.run()