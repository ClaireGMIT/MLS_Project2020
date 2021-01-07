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