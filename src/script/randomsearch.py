from sklearn.model_selection import RandomizedSearchCV
from pathlib import Path
import pandas as pd
from src.utils.paths import PATH_DIR
from datetime import datetime

DATASET_PATH = PATH_DIR+'res/datasets/extracted/{}_dataset_ext.csv'


def perform_randomsearch(pipeline, dataset_name, parameters, folds=5, n_iter=100, verbose=10, n_jobs=10):
    """Performs RandomSearch for the specified pipeline and params"""
    dataset_path = Path(DATASET_PATH.format(dataset_name)).resolve()
    dataset = pd.read_csv(dataset_path)

    X = dataset.loc[:, dataset.columns != 'subjectivity']
    y = dataset['subjectivity']

    search = RandomizedSearchCV(pipeline, parameters, n_iter=n_iter, scoring='f1',
                                cv=folds, verbose=verbose, n_jobs=n_jobs, random_state=42)
    search.fit(X, y)

    print(search.best_params_)
    print(search.best_score_)
    with open("{}logs/{}_randomsearch_{}.log".format(
            PATH_DIR, dataset_name, datetime.now().strftime("%m-%d-%Y-%H-%M-%S")), "w+") as f:
        f.write("Best Score (f1): {}\nParams: {}\n".format(search.best_score_, search.best_params_))