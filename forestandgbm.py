__author__ = 'kirk'
# code to compare gbm and rf for datafest 2014
# w/ more time would've liked to check out an arima/rnn hybrid
# but energy data has looooong seasonality
# so wouldve taken too long to train
# also had to sign an nda for the data so no longer available
# but data set 3 years' worth of hourly data from 110 buildings
# features included:
# total electricity consumption,
# electricity consumption by appliance,
# and weather data
# chose to model each building separately d/t bldg-specific trends
# also turned findings into flask bootstrap app (thanks mike)
# available here: mutianzhai.com
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn import preprocessing
from pybrain.datasets.supervised import SupervisedDataSet as SDS
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure.modules import TanhLayer, LinearLayer
from sklearn.linear_model import LinearRegression


combined = pd.read_csv('/home/kirk/revised.csv')


bldg1 = combined.ix[combined['Building'] == 'BLDG001']


bldg1 = pd.read_csv('revised.csv')
bldg1 = bldg1.dropna(axis=1, how='all')
del bldg1['Building']

#THIS GRABS THE WEATHER DATA
#AND THE DAY OF THE WEEK
#FROM THE CSV THAT YOU WRITTEN FROM R
inputs = bldg1.ix[:, 0:8]
#THIS GRABS THE DATE
inputs['date'] = bldg1['date']
# THIS GRABS THE HOUR
inputs['hours'] = bldg1['hour']
# THIS CONVERTS THE DATE COLUMN TO A DATE FORMAT PANDAS RECOGNIZES
inputs.index = pd.to_datetime(inputs['date'])
# THIS CREATES THE MONTH VARIABLE
inputs['date'] = inputs.index.month
del inputs['IntervalStart']
# THIS ELIMINATES MISSING VALUES
inputs = inputs.apply(pd.Series.interpolate)
#comparing rf vs gbm

# this is a model for one building not for all 110
# building is a large restaurant in nc

bldg1RF = RandomForestRegressor(n_estimators=20000, oob_score=True, max_depth=4, n_jobs=32)
bldg1RFfitted = bldg1RF.fit(inputs, bldg1['Main.Load'])
fitsRF = {'fitted':bldg1RFfitted.oob_prediction_, 'actual': bldg1['Main.Load'], 'difference': bldg1['Main.Load'] - bldg1RFfitted.oob_prediction_}
fitsRF = pd.DataFrame(fitsRF)
scoreRF = bldg1RF.score(inputs, bldg1['Main.Load'])
print 'Random Forest R2: ', scoreRF
print 'Random Forest R2 OOB: ', bldg1RF.oob_score_
fitsRF.to_csv('fitresultsRF.csv')

#THIS RUNS THE GBM
#need to get tony's code for tuning this
bldg1GBM = GradientBoostingRegressor(n_estimators=5000, learning_rate=.01, max_features=.4,max_depth=4, subsample=.6, random_state=0, loss='ls')
bldg1GBMfitted = bldg1GBM.fit(inputs, bldg1['Main.Load'])
fitsGBM = {'fitted':bldg1GBMfitted.predict(inputs), 'actual': bldg1['Main.Load'], 'difference': bldg1['Main.Load'] - bldg1GBMfitted.predict(inputs)}
fitsGBM = pd.DataFrame(fitsGBM)
scoreGBM = bldg1GBM.score(inputs, bldg1['Main.Load'])
print scoreGBM
fitsGBM.to_csv('fitresultsGBM2nd.csv')

#rf performs worse than the gbm
# most likely b/c data set was narrow and long
# rf does better when it can create many different feature combinations
# i.e. lots of different trees
# so rf performs better w/ square-ish data
# or when data is wide and long

