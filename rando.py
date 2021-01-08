# flask for web app.
import flask as fl

# numpy for numerical work.
import numpy as np

# numpy for numerical work.
from flask import request

# Create a new web app.
app = fl.Flask(__name__)

# Add root route.
@app.route("/")
def home():
    return app.send_static_file('index1.html')

# Add uniform route.
# Application Programming Interface
@app.route('/api/uniform')
def uniform():
  return {"value": np.random.uniform()} #ie returns random number as dict

# Add normal route.
@app.route('/api/normal')
def normal():
  return {"value": np.random.normal()} #ie returns random number as dict and jsonified

###############################################################################################




@app.route('/api/train', methods=['POST'])
def train():
    # get parameters from request
    parameters = request.get_json()

    # read iris data set
    iris = datasets.load_iris()
    X, y = iris.data, iris.target

    # fit model
    clf = svm.SVC(C=float(parameters['C']),
                  probability=True,
                  random_state=1)
    clf.fit(X, y)

    # persist model
    joblib.dump(clf, 'model.pkl')

    return jsonify({'accuracy': round(clf.score(X, y) * 100, 2)})


@app.route('/api/predict', methods=['POST'])
def predict():
    # get iris object from request
    X = request.get_json()
    X = [[float(X['sepalLength']), float(X['sepalWidth']), float(X['petalLength']), float(X['petalWidth'])]]

    # read model
    clf = joblib.load('model.pkl')
    probabilities = clf.predict_proba(X)

    return jsonify([{'name': 'Iris-Setosa', 'value': round(probabilities[0, 0] * 100, 2)},
                    {'name': 'Iris-Versicolour', 'value': round(probabilities[0, 1] * 100, 2)},
                    {'name': 'Iris-Virginica', 'value': round(probabilities[0, 2] * 100, 2)}])


if __name__ == '__main__':
    # run web server
    app.run(host=HOST,
            debug=True,  # automatic reloading enabled
            port=PORT)