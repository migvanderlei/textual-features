from sklearn.model_selection import RandomizedSearchCV, cross_val_score
import pandas as pd
import numpy as np
from src.utils.paths import PATH_DIR
from datetime import datetime
from sklearn.metrics import classification_report, make_scorer

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

    scoring = ['f1_macro', 'accuracy_macro', 'precision_macro', 'recall_macro']

    search = RandomizedSearchCV(pipeline, parameters, n_iter=n_iter, scoring=scoring, refit='f1_macro',
                                cv=folds, verbose=verbose, n_jobs=n_jobs, random_state=42)
    search.fit(X, y)
    # print(search.cv_results_)
    # global REPORT_FILENAME 
    # REPORT_FILENAME = REPORT_FILENAME.format(
    #     PATH_DIR, dataset_name, dataset_name, 'report', OUT_NAMES[str(group)], model_name, datetime.now().strftime("%Y-%m-%d-%H-%M"))
    content = get_content(search, unique, group, dataset.columns, dataset_name)
    print(content)
    # report = cross_val_score(search, X=X, y=y, cv=folds,
    #            scoring=make_scorer(classification_report_with_f1_score))
    # print("F-1 scores for validation:", report) 
    if unique:
        filename = "{}logs/{}/{}_{}_{}_{}_{}.log".format(
            PATH_DIR, dataset_name, dataset_name, 'unique', OUT_NAMES[str(group)], model_name, datetime.now().strftime("%Y-%m-%d-%H-%M"))
        
    else:
        filename = "{}logs/{}/NEW_{}_{}_{}_{}_{}.log".format(
            PATH_DIR, dataset_name, dataset_name, 'ablation', OUT_NAMES[str(group)], model_name, datetime.now().strftime("%Y-%m-%d-%H-%M"))
    with open(filename, "w+") as f:
        f.write(content)

def get_content(search, unique, group, columns, dataset_name):
    description = get_description(unique, group, columns)
    f1, f1_folds = get_metric('f1_macro', search.cv_results_)
    accuracy, accuracy_folds = get_metric('accuracy_macro', search.cv_results_)
    precision, precision_folds = get_metric('precision_macro', search.cv_results_)
    recall, recall_folds = get_metric('recall_macro', search.cv_results_)

    content = ("Dataset: {}\n"+
                "Description: {}\n"+
                "F1 macro: {} ({})\n"+
                "Accuracy macro: {} ({})\n"+
                "Precision macro: {} ({})\n"+
                "Recall macro: {} ({})\n" +
                "Params: {}").format(
                    dataset_name, description, f1, f1_folds, accuracy, accuracy_folds,
                    precision, precision_folds, recall, recall_folds, search.best_params_)
    return content

def get_description(unique, group, columns):
    if unique:
        if int(group) < 8:
            return "Only {} features from group {}" \
                    .format(len(columns)-1, OUT_NAMES[str(group)])
        else: 
            return "All {} features from all groups" \
                    .format(len(columns)-1)
    else:
         return "Group ablation study with {} features and removing group {}" \
                .format(len(columns)-1, OUT_NAMES[str(group)])

def get_metric(metric_name, results, goal_metric='f1_macro', folds=5):
    best_score_index = np.where(results['rank_test_'+goal_metric] == 1)[0][0]
    fold_metrics = []
    for i in range(folds):
        fold_metrics.append(results['split'+str(i)+'_test_'+metric_name][best_score_index])
    return (results['mean_test_'+metric_name][best_score_index], fold_metrics)

# def classification_report_with_f1_score(y_true, y_pred):
#     global REPORT_FILENAME 
#     with open(REPORT_FILENAME, 'a+') as f:
#         print(classification_report(
#             y_true, y_pred, target_names=['objective', 'subjective'], digits=16
#             )+"\n"+"-"*85, file=f)
#     return f1_score(y_true, y_pred)