__author__ = "Manuel Fischer"
__version__ = "1.0.0"

# goal: running all tests with one script adaptively
# intented functions:   adaptive datainput, adaptive approaches, visualisation
# current functions:    adaptive datainput, static approaches, visualisation
# TODO: adaptive approaches, low priority

# import libraries
import json
import os
# import data input managers
import data.data_crawler as crawl
import data.data_loader as loader

# import visualizer
from results_comparison import visualizer_for_results as visu

def start_all(crawldata):
    # DATA can be changed by moving/copying .txt or .csv into /data!

    # load settings for the testruns from json
    config = json.load(open('./config_runall.json', 'r'))

    # get all valid input data in folder
    path_to_folder = config['data']['folder']
    approaches_folder = config['approaches_folder']

    # import custom approaches
    from approaches._1_holtwinters import run as hw
    from approaches._2_ARIMA import run as arima
    from approaches._3_LSTM import run as lstm

    # add all prediction approaches to list
    apps = [arima, hw, lstm]

    if crawldata:
        # get data by crawl
        frames = crawl.get_dataframes_by_crawl(['ORCL', 'TSLA', 'IBM', 'YELP', 'MSFT'], 2015, 2019)
        for f in frames:
            dataloader = loader.DataLoader(
                f,
                config['data']['train_test_split'],
                config['data']['columns']
            )

    approaches = config['approaches']

    #print(os.listdir(os.curdir))
    os.chdir(approaches_folder)
    #print(os.listdir(os.curdir))

    # loop trough all approaches
    i = 0
    for app in apps:
        #os.chdir(approaches_folder)
        os.chdir(approaches[i])
        #if i==0: os.chdir('_1_holtwinters')
        #else: os.chdir('_2_ARIMA')
        print(approaches[i])
        # assuming all approaches have a run() function. could be improved by abstract class.
        app.run(
                    # '/'+
                    # approaches_folder+
                    # '/'+
                    # approaches[i]+
                    # '/' +
                    'config.json') #\
            #if crawldata is False else app.run(dataloader)
        os.chdir('..')
        i += 1

    # visuals for comparing all approaches
    visu.visualize_all()

# def execute_all():
#     config = json.load(open('./config.json', 'r'))
#     os.chdir(os.curdir + config['methodsfolder'])
#     for f in os.listdir(os.curdir):
#         f.find('run.py')
#         #somehow run the python script

if __name__ == '__main__':
    start_all(crawldata=False)
    # start_all_static()
