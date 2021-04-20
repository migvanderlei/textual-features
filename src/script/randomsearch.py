from scipy.stats.stats import describe
from sklearn.model_selection import RandomizedSearchCV
import pandas as pd
import numpy as np
from src.utils.paths import PATH_DIR
from datetime import datetime

DATASET_PATH = PATH_DIR+'res/datasets/extracted/{}/{}_{}_{}_dataset_ext.csv'
OUT_NAMES = {
        '0': 'POS',
        '1': 'SYNTACTIC_RULES',
        '2': 'LEXICON',
        '3': 'CONCEPT',
        '4': 'CONCEPT_ABS',
        '5': 'MISCELLANEOUS',
        '6': 'TWITTER',
        '7': 'TEXT_STRUCTURE',
        '8': 'ALL'
}

def perform_randomsearch(pipeline, dataset_name, parameters, model_name, unique, group=0, folds=5, n_iter=100, verbose=10, n_jobs=10):
    """Performs RandomSearch for the specified pipeline and params"""
    dataset_path = ''
    if group != '8':
        dataset_path = DATASET_PATH.format(dataset_name, dataset_name,
                                     "unique" if unique else "groups", str(group))
    else:
        dataset_path = PATH_DIR+'res/datasets/extracted/{}/{}_all_groups_dataset_ext.csv' \
            .format(dataset_name, dataset_name)

    print(dataset_path)
    dataset = pd.read_csv(dataset_path)
    
    X = dataset.loc[:, dataset.columns != 'subjectivity']
    y = dataset['subjectivity']

    scoring = ['f1', 'accuracy', 'precision', 'recall']

    search = RandomizedSearchCV(pipeline, parameters, n_iter=n_iter, scoring=scoring, refit='f1',
                                cv=folds, verbose=verbose, n_jobs=n_jobs, random_state=42)
    search.fit(X, y)

    content = get_content(search, unique, group, dataset.columns, dataset_name)
    print(content)
    if unique:
         filename = "{}logs/{}/{}_{}_{}_{}_{}.log".format(
            PATH_DIR, dataset_name, dataset_name, 'unique', OUT_NAMES[str(group)], model_name, datetime.now().strftime("%Y-%m-%d-%H-%M"))
    else:
        filename = "{}logs/{}/{}_{}_{}_{}_{}.log".format(
            PATH_DIR, dataset_name, dataset_name, 'ablation', OUT_NAMES[str(group)], model_name, datetime.now().strftime("%Y-%m-%d-%H-%M"))
    with open(filename, "w+") as f:
        f.write(content)

def get_content(search, unique, group, columns, dataset_name):
    description = get_description(unique, group, columns)
    return "Dataset: {}\nDescription: {}\nBest Score (F1): {}\nAccuracy: {}\nPrecision: {}\nRecall: {}\nParams: {}".format(
                    dataset_name, description, get_metric('f1', search.cv_results_), 
                    get_metric('accuracy', search.cv_results_), get_metric('precision', search.cv_results_), 
                    get_metric('recall', search.cv_results_), search.best_params_) 

def get_description(unique, group, columns):
    if unique:
        if int(group) < 8:
            return "Only {} features from the group {}" \
                    .format(len(columns)-1, OUT_NAMES[str(group)])
        else: 
            return "All {} features from all groups" \
                    .format(len(columns)-1)
    else:
         return "Group ablation study with {} features and removing the group {}" \
                .format(len(columns)-1, OUT_NAMES[str(group)])

def get_metric(metric_name, results):
    best_score_index = np.where(results['rank_test_'+metric_name] == 1)[0][0]
    return results['mean_test_'+metric_name][best_score_index]