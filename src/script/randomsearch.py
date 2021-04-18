from sklearn.model_selection import RandomizedSearchCV
import pandas as pd
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
                                     "unique" if unique else "grouped", str(group))
    else:
        dataset_path = PATH_DIR+'res/datasets/extracted/{}/{}_all_groups_dataset_ext.csv' \
            .format(dataset_name, dataset_name)

    print(dataset_path)
    dataset = pd.read_csv(dataset_path)
    
    X = dataset.loc[:, dataset.columns != 'subjectivity']
    y = dataset['subjectivity']

    search = RandomizedSearchCV(pipeline, parameters, n_iter=n_iter, scoring='f1',
                                cv=folds, verbose=verbose, n_jobs=n_jobs, random_state=42)
    search.fit(X, y)

    print(search.best_params_)
    print(search.best_score_)
    filename = ""
    if unique:
         filename = "{}logs/{}/{}_{}_{}_{}_{}.log".format(
            PATH_DIR, dataset_name, dataset_name, 'unique', OUT_NAMES[str(group)], model_name, datetime.now().strftime("%Y-%m-%d-%H-%M"))
    else:
        filename = "{}logs/{}/{}_{}_{}_{}_{}.log".format(
            PATH_DIR, dataset_name, dataset_name, 'ablation', OUT_NAMES[str(group)], model_name, datetime.now().strftime("%Y-%m-%d-%H-%M"))
    with open(filename, "w+") as f:
        f.write("Best Score (f1): {}\nParams: {}\n".format(search.best_score_, search.best_params_))