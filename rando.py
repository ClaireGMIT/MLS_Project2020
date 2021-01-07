# flask for web app.
import flask as fl

# numpy for numerical work.
import numpy as np

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

