# time series predition comparison
predict stock market prices using machine learning and traditional methods. compare accuracy of the resulting predictions.

## ONLY CONTAINS RESULTS, VISUALS and CONFIGURATIONS right now!

![](credit-references/logo_cuda.jpg)
![](credit-references/logo_keras.jpg)
![](credit-references/logo_tensorflow.jpg)

## DEMO

[![DEMO](https://img.youtube.com/vi/fm4CaIVge2E/0.jpg)](https://www.youtube.com/watch?v=fm4CaIVge2E)


## requirements and install
- install all requirements. on windows: run "requirements.sh". on others: check requirements.txt.
- install tensorflow - optional: install tensorflow-GPU support

tensorflow
https://www.tensorflow.org/install
used only by 1 method (LSTM)

## input data


| group | datapoints | stock tickers |
| --------------- | --------------- | --------------- |
| Saisonal  | 8799  | 7 |
| Trend  | 6286 | 5 |
| Index  | 14731 | 3 |
| total  | 29816 | 15 |

as input data stock market prices are used.
new input data can be generated by a webcrawler located in the data folder.
input data is read from the "data" folder. containing files can be changed. new predictions will be generated on the new data.
datamanipulation and visualisation can be done with the scripts in the data folder.
by default you can compare the same dataset with multiple approaches.


## approaches / methods for predictions
current prediction methods you can use:

- Holtwinters
features: config, split, normalisation, forecast, evaluation, visualisation
- ARIMA
features: config, split, normalisation, forecast, evaluation, visualisation
- LSTM
features: config, datanormalisation, split, forecast, evaluation

## results and comparison

| approach | accuracy (mean MAPE) |
| --------------- | --------------- |
| Holt-Winters  | 11.43254053624151  |
| ARIMA  | 10.305568060027946  |
| LSTM  | 10.74913006361077 |

[![results](https://github.com/mafima/time-series-prediction-comparison/blob/master/results_comparison/approach%20comparison/ARIMA.png)]

[![results2](https://github.com/mafima/time-series-prediction-comparison/blob/master/results_comparison/approach%20comparison/LSTM.png)]

prediction visualisation - use the same class for visualising
evaluation - basic np evaluation function for getting error
result visualisation

## FAQ / troubleshoot

ValueError: Invalid file path or buffer object type: <class 'NoneType'> 
Check File Paths.

## LICENSE / CREDIT

Code used may has been created by others and is used under their seperate license. Reference to every original copyright and license owner is made under the "credit-references" folder and in the coresponding folders. Please contact me immediately if copyrighted files are used without your permission or without giving proper credit. In that case the corresponding code will be removed as soon as possible.

Everything else is under the MIT License:

[![GitHub license](https://img.shields.io/badge/License-MIT-brightgreen.svg?style=flat-square)](https://github.com/mafima/time-series-predition-comparison/blob/master/LICENSE) 

## Run Tests:
To run ALL functions of the program you can run the run.py class!

## base features for comparing
datapipeline - compare the same dataset with multiple approaches
datafiles, datamanipulation and visualisation
visualisation - use the same class for visualising in all of them


