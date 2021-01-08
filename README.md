# MLS_Project2020
Git Repository for the GMIT Machine Learning and Statistics Project 2020


Random numerical app.
# Linux
    export FLASK_APP=rando.py
    python3 -m flask run

# Windows
    set FLASK_APP=rando.py
    python -m flask run
    docker build . -t rando-image
    docker run --name rando-container -d -p 5000:5000 rando-image


# How to run the web service
$ export FLASK_APP=web-service.py
$ flask run
 * Running on http://127.0.0.1:5000/