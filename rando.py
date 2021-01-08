# Ref: 
# 1: https://medium.com/@dvelsner/deploying-a-simple-machine-learning-model-in-a-modern-web-application-flask-angular-docker-a657db075280
# 2: https://www.analyticsvidhya.com/blog/2020/09/integrating-machine-learning-into-web-applications-with-flask/

# flask for web app.
import flask as fl

# numpy for numerical work.
import numpy as np

# numpy for numerical work.
from flask import  Flask, jsonify, request
import pickle



# Create a new web app.
app = fl.Flask(__name__)

model1 = pickle.load(open('model.pkl', 'rb'))

# Add root route.
@app.route("/")
def home():
    return app.send_static_file('index1.html')

#To use the predict button in our web-app
@app.route('/predict',methods=['POST'])
def predict():
    #For rendering results on HTML GUI
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model1.predict(final_features)
    output = round(prediction[0], 2) 
    return render_template('index1.html', prediction_text='Estimated power outage :{}'.format(output))

if __name__ == '__main__':
    app.run()


