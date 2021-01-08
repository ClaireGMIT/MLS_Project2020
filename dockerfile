#FROM python:3

FROM python:3.7.9 
# I had to change this to the exact version of python on my machine as per Elizabeth email
# check your version of python by using the following in command line: python -VV

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=rando.py

CMD flask run --host=0.0.0.0




