#!/bin/bash
export PATH=$PATH:/home/ubuntu/anaconda3/bin
cd /home/ubuntu/covid-back
export FLASK_APP=covid-server.py
export FLASK_RUN_PORT=8080
flask run --host=0.0.0.0 &