#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import covid_api as api

print('Test load model')
#model = api.load_model_from_file('model.h5')
#model = api.load_model_from_file('model.h5')
#print('Model loaded')

model = api.ModelSingleton.getInstance().model
meta_data = api.run_tests(model)

print('Test Loss ', meta_data[0])
print('Test Accuracy ', meta_data[1])

print('Analysing image 1 for COVID ', api.is_covid(model,'/Users/adalbertocajueiro/Downloads/normal-image.jpeg'))
print('Analysing image 2 for COVID ', api.is_covid(model,'/Users/adalbertocajueiro/Documents/covid-19/tmp_files/1585853453.017824-covid-image.jpeg'))
