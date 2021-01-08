# MLS_Project2020
Git Repository for the GMIT Machine Learning and Statistics Project 2020

There are a number files saved in this GIT repository:

1. Wind_Turbine_Notebook
This is a Jupyter notebook describing the stages in developing the machine learning model.

2. model.py and model.pkl
This is the file where the chosen machine learning model is saved.

3. Dockerfile
Random numerical app.
# Linux
    export FLASK_APP=rando.py
    python3 -m flask run

# Windows
    set FLASK_APP=rando.py
    python -m flask run
    docker build . -t rando-image
    docker run --name rando-container -d -p 5000:5000 rando-image

4. rando.py
This is the flask server to run the web services.
# How to run the web service
$ export FLASK_APP=web-service.py
$ flask run
 * Running on http://127.0.0.1:5000/

5. Static Pages containing the index1.html web page for user interaction

6. powerproduction.csv
The data for analysis

7. requirements.txt
Requirements for running the files