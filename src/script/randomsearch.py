from sklearn.model_selection import RandomizedSearchCV, cross_val_score
import pandas as pd
import numpy as np
from src.utils.paths import PATH_DIR
from datetime import datetime
import time

DATASET_PATH = PATH_DIR+'res/datasets/extracted/{}/{}_{}_{}_dataset_ext.csv'
OUT_NAMES = {
        '0': 'POS',
        '1': 'SYNTACTIC_RULES',
        '2': 'LEXICON',
        '3': 'CONCEPT_ABS',
        '4': 'MISCELLANEOUS',
        '5': 'TWITTER',
        '6': 'TEXT_STRUCTURE',
        '7': 'ALL'
}
REPORT_FILENAME = "{}logs/{}/{}_{}_{}_{}_{}.txt"

def perform_randomsearch(pipeline, dataset_name, parameters, model_name, unique, group=0, folds=5, n_iter=100, verbose=10, n_jobs=10):
    """Performs RandomSearch for the specified pipeline and params"""
    dataset_path = ''
    if group != '7':
        dataset_path = DATASET_PATH.format(dataset_name, dataset_name,
                                     "unique" if unique else "groups", str(group))
    else:
        dataset_path = PATH_DIR+'res/datasets/extracted/{}/{}_all_groups_dataset_ext.csv' \
            .format(dataset_name, dataset_name)


    print(dataset_path)
    dataset = pd.read_csv(dataset_path)
    
    X = dataset.loc[:, dataset.columns != 'subjectivity']
    y = dataset['subjectivity']

    scoring = ['f1_macro', 'accuracy', 'precision_macro', 'recall_macro']

    search = RandomizedSearchCV(pipeline, parameters, n_iter=n_iter, scoring=scoring, refit='f1_macro',
                                cv=folds, verbose=verbose, n_jobs=n_jobs, random_state=42)
    start_time = time.time()
    search.fit(X, y)
    end_time = time.time()

    content = get_content(search, unique, group, dataset.columns, dataset_name, end_time-start_time)
    print(content)
   
    if unique:
        filename = "{}logs/{}/{}_{}_{}_{}_{}.txt".format(
            PATH_DIR, dataset_name, dataset_name, 'unique', OUT_NAMES[str(group)], model_name, datetime.now().strftime("%Y-%m-%d-%H-%M"))
        
    else:
        if group != '7':
            filename = "{}logs/{}/NEW_{}_{}_{}_{}_{}.txt".format(
                PATH_DIR, dataset_name, dataset_name, 'ablation', OUT_NAMES[str(group)], model_name, datetime.now().strftime("%Y-%m-%d-%H-%M"))
        else:
            filename = "{}logs/{}/NEW_{}_{}_{}_{}.txt".format(
                PATH_DIR, dataset_name, dataset_name, OUT_NAMES[str(group)], model_name, datetime.now().strftime("%Y-%m-%d-%H-%M"))

    with open(filename, "w+") as f:
        f.write(content)

def get_content(search, unique, group, columns, dataset_name, search_time):
    description = get_description(unique, group, columns)
    f1, f1_folds = get_metric('f1_macro', search.cv_results_)
    accuracy, accuracy_folds = get_metric('accuracy', search.cv_results_)
    precision, precision_folds = get_metric('precision_macro', search.cv_results_)
    recall, recall_folds = get_metric('recall_macro', search.cv_results_)

    content = ("Dataset: {}\n"+
                "Description: {}\n"+
                "F1 macro: {} ({})\n"+
                "Accuracy: {} ({})\n"+
                "Precision macro: {} ({})\n"+
                "Recall macro: {} ({})\n" +
                "Params: {}\n" +
                "Search time: {} seconds").format(
                    dataset_name, description, f1, f1_folds, accuracy, accuracy_folds,
                    precision, precision_folds, recall, recall_folds, search.best_params_,
                    search_time)
    return content

def get_description(unique, group, columns):
    if unique:
        if int(group) < 7:
            return "Only {} features from group {}" \
                    .format(len(columns)-1, OUT_NAMES[str(group)])
        else: 
            return "All {} features from all groups" \
                    .format(len(columns)-1)
    else:
        if int(group) < 7:
            return "Group ablation study with {} features and removing group {}" \
                .format(len(columns)-1, OUT_NAMES[str(group)])
        else: 
            return "All {} features from all groups" \
                .format(len(columns)-1)

def get_metric(metric_name, results, goal_metric='f1_macro', folds=5):
    best_score_index = np.where(results['rank_test_'+goal_metric] == 1)[0][0]
    fold_metrics = []
    for i in range(folds):
        fold_metrics.append(results['split'+str(i)+'_test_'+metric_name][best_score_index])
    return (results['mean_test_'+metric_name][best_score_index], fold_metrics)