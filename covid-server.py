#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# servidos python que entra no ar e responde a algumas rotas simples
# colocado no ar usando o framework flask
# Para usar é necessario instalar as dependencias (com pip) e rodar os comandos:
# export FLASK_APP=covid-server.py 
# export FLASK_RUN_PORT=8080 (para configurar a porta)
# flask run

from flask import Flask,request
from werkzeug.utils import secure_filename
from flask_cors import CORS
import covid_api as api
import time as t

# caminho onde os arquivos analisados sao salvos. mudar convenientemente este caminho
#files_path = '/Users/adalbertocajueiro/Documents/covid-19/tmp_files/'
files_path = '/home/ubuntu/tmp_files/'

#carrega o modelo quando da inicializacao do servico
model = api.ModelSingleton.getInstance().model
meta_data = api.run_tests(model)
app = Flask(__name__)
# para resolver o problema de Cross Origins com o front-end
CORS(app)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return 'Hello. I am a program for analysing images against covid!'

@app.route('/covid', methods=['GET', 'POST'])
def check_covid():
  return {
    "answer": True,
    "answer2": False
  }

@app.route('/model', methods=['GET', 'POST'])
def model():
  return { 
    "loss": str(meta_data[0]),
    "accuracy":str(meta_data[1])
  }

@app.route('/analyse', methods=['POST'])
def analyse_file():
      f = request.files['file']
      timeStamp = t.time()
      #print('FILE NAME ', str(timeStamp) + '-' + secure_filename(f.filename))
      newFilePath = files_path + str(timeStamp) + '-' + secure_filename(f.filename)
      print('FILE ', newFilePath)
      f.save(newFilePath)
      model = api.ModelSingleton.getInstance().model
      answer = api.is_covid(model,newFilePath)
      return {
        "answer":answer
      }