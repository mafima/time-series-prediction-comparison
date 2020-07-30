# Visualizer for Results
__author__ = "Manuel Fischer"
__copyright__ = "Manuel Fischer 2020"
__version__ = "1.0.0"
__license__ = "MIT"

#import libraries
import matplotlib.pyplot as plt
import numpy as np
# Fixing random state for reproducibility
np.random.seed(7)
import json

import sys
sys.path.append('../..')  # parent folder import
import base.jsonparser_results as jparse


def visualize_all():
    config = json.load(open('config_visualizer.json'))

    results_json, all_data, approaches_len, appr_titles, metric = jparse.json_to_results_list(
        config['input']['filename'], config['input']['inner_metric'])
    # visualize by each result
    for i in range(approaches_len):  # approaches_len
        # fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(9, 4))
        # result mode
        violin_not_box = config['visuals']['mode'] is 'violin'  # optional TO DO: enum implemention
        if violin_not_box:
            plt.violinplot(all_data[i], showmeans=False, showmedians=True)
        else:
            box = plt.boxplot(all_data[i])




        # adding horizontal grid lines, labels
        plt.grid(True)
        plt.xlabel(config['visuals']['xlabel'])
        plt.ylabel(config['visuals']['ylabel'])

        # add x-tick labels. dataset names
        titles_of_all_datasets = []
        errorvalues_of_datasets=[]
        for key, values in results_json[appr_titles[i]][metric].items():
            # reduce key
            if config['visuals']['reducekeys']['reduce']:  # ignore if reduce is False
                skey = str(key)
                if (config['visuals']['reducekeys']['reduceby'] in skey):
                    key = skey.split(config['visuals']['reducekeys']['reduceby'])[
                        config['visuals']['reducekeys']['splitID']]  # split id. 0=first
            # add dataset name to all dataset names
            titles_of_all_datasets.append(key)
            # add dataset value as mean value for mean endresult
            errorvalues_of_datasets.append(np.array(values).mean())

        offset = config['visuals']['xlabeloffset'] # default is "xlabeloffset": 1, to get a range(1, len keys+1)
        plt.xticks(range(offset, len(titles_of_all_datasets) + offset), titles_of_all_datasets)
        plt.tick_params(axis='x', labelsize=config['visuals']['xlabelsize'])
        plt.tick_params(axis='y', labelsize=config['visuals']['ylabelsize'])

        # set title: approach name and ERROR mean
        allmeans = np.array(errorvalues_of_datasets).mean()
        approach_title = appr_titles[i] + ', MAPE(Mean): ' + str(allmeans)
        plt.title(approach_title)
        print(approach_title)
        plt.show()

    #OLD backup 3 in one. usable for datasets * approaches < 15
    # fig, axes = plt.subplots(nrows=1, ncols=approaches_len, figsize=(9, 4))
    # violin_not_box=False
    # for i in range(approaches_len):
    #     if violin_not_box:
    #         axes[i].violinplot(all_data[i],
    #                            showmeans=False,
    #                            showmedians=True)
    #     else:
    #         axes[i].boxplot(all_data[i])
    #     axes[i].set_title(appr_titles[i])
    #
    # # adding horizontal grid lines
    # for ax in axes:
    #     ax.yaxis.grid(True)
    #     ax.set_xticks([y + 1 for y in range(len(all_data[1]))])
    #     ax.set_xlabel('datasets')
    #     ax.set_ylabel('MAPE')
    #
    #     # add x-tick labels
    #     xticklabels = resultsfile[appr_titles[1]][metric]
    #     plt.setp(axes[i], xticks=[y + 1 for y in range(len(all_data[1]))],
    #              xticklabels=xticklabels)
    #
    # plt.show()

if __name__ == '__main__':
    visualize_all()