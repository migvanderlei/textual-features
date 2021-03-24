from sklearn.model_selection import RandomizedSearchCV
from sklearn.preprocessing import StandardScaler
from pathlib import Path
import pandas as pd
from src.utils.paths import PATH_DIR
from datetime import datetime

DATASET_PATH = PATH_DIR+'res/datasets/extracted/{}/{}_unique_{}_dataset_ext.csv'


def perform_randomsearch(pipeline, dataset_name, parameters, model_name, group=0, folds=5, n_iter=100, verbose=10, n_jobs=10, preprocess=False):
    """Performs RandomSearch for the specified pipeline and params"""
    dataset_path = DATASET_PATH.format(dataset_name, dataset_name, str(group))
    print(dataset_path)
    dataset = pd.read_csv(dataset_path)
    
    X = dataset.loc[:, dataset.columns != 'subjectivity']
    y = dataset['subjectivity']

    if preprocess:
        scaler = StandardScaler()
        X = scaler.fit_transform(X)

    search = RandomizedSearchCV(pipeline, parameters, n_iter=n_iter, scoring='f1',
                                cv=folds, verbose=verbose, n_jobs=n_jobs, random_state=42)
    search.fit(X, y)

    print(search.best_params_)
    print(search.best_score_)
    filename = ""
    if preprocess:
        filename = "{}logs/{}_randomsearch_unique_{}_{}.log".format(
            PATH_DIR, dataset_name+"_scaled", model_name, datetime.now().strftime("%%Y-%m-%d-%H-%M"))
    else:
        filename = "{}logs/{}/{}_{}_{}_{}.log".format(
            PATH_DIR, dataset_name, dataset_name, str(group), model_name, datetime.now().strftime("%Y-%m-%d-%H-%M"))
    with open(filename, "w+") as f:
        f.write("Best Score (f1): {}\nParams: {}\n".format(search.best_score_, search.best_params_))