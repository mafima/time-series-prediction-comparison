# time series predition comparison
predict stock market prices using machine learning and traditional methods. compare accuracy of the resulting predictions.

![](credit-references/logo_cuda.jpg)
![](credit-references/logo_keras.jpg)
![](credit-references/logo_tensorflow.jpg)

# DEMO

[![DEMO](https://img.youtube.com/vi/fm4CaIVge2E/0.jpg)](https://www.youtube.com/watch?v=fm4CaIVge2E)


# requirements and install
- install all requirements. on windows: run "requirements.sh". on others: check requirements.txt.
- install tensorflow - optional: install tensorflow-GPU support

tensorflow
https://www.tensorflow.org/install
used only by 1 method (LSTM)

# data
datafiles, datamanipulation and visualisation
datapipeline - compare the same dataset with multiple approaches

# base features for comparing
visualisation - use the same class for visualising in all of them
evaluation - basic np evaluation function for getting error

# approaches / methods for predictions
current prediction methods you can use:

- Holtwinters
features: config, split, normalisation, forecast, evaluation, visualisation
- ARIMA
features: config, split, normalisation, forecast, evaluation, visualisation
- LSTM
features: config, datanormalisation, split, forecast, evaluation

# FAQ / troubleshoot

ValueError: Invalid file path or buffer object type: <class 'NoneType'> 
Check File Paths.

# LICENSE / CREDIT

Code used may has been created by others and is used under their seperate license. Reference to every original copyright and license owner is made under the "credit-references" folder and in the coresponding folders. Please contact me immediately if copyrighted files are used without your permission or without giving proper credit. In that case the corresponding code will be removed as soon as possible.

Everything else is under the MIT License:

[![GitHub license](https://img.shields.io/badge/License-MIT-brightgreen.svg?style=flat-square)](https://github.com/mafima/time-series-predition-comparison/blob/master/LICENSE) 

# Run Tests:
To run ALL functions of the program you can run the run.py class!

# base features for comparing
datapipeline - compare the same dataset with multiple approaches
datafiles, datamanipulation and visualisation
visualisation - use the same class for visualising in all of them


