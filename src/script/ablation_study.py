from pathlib import Path
import pandas as pd
from src.utils.paths import PATH_DIR
from datetime import datetime
from sklearn.model_selection import cross_validate

DATASET_PATH = PATH_DIR + 'res/datasets/extracted/{}_dataset_ext.csv'


def perform_ablation(clf, dataset_name):
    """Performs ablation study"""
    dataset = pd.read_csv(DATASET_PATH.format(dataset_name))

    X = dataset.loc[:, dataset.columns != 'subjectivity']
    y = dataset['subjectivity']
    features = X.columns
    results = []
    for feature in features:
        X_less = X.loc[:, X.columns != feature]

        # X_train, X_test, y_train, y_test = train_test_split(X_less, y, test_size=0.30, random_state=42)
        scores = cross_validate(clf, X=X_less, y=y, scoring=['f1', 'precision', 'recall'], cv=5, n_jobs=4)
        results.append((scores['test_f1'].mean(), scores['test_precision'].mean(),
                        scores['test_recall'].mean(), feature))

    results.sort(key=lambda tup: tup[0])

    with open("{}logs/{}_ablation_{}.csv".format(
            PATH_DIR, dataset_name, datetime.now().strftime("%m%d%Y%H%M%S")), "w+") as f:
        f.write('f1,precision,recall,feature\n'+'\n'.join('{},{},{},{}'.format(x[0], x[1], x[2], x[3]) for x in results))
