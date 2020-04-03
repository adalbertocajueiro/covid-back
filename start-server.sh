#!/bin/sh
cd /home/ubuntu/
source .bashrc
cd /home/ubuntu/covid-back
export FLASK_APP=covid-server.py
export FLASK_RUN_PORT=8080
flask run
