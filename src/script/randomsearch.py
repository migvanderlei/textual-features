from sklearn.model_selection import RandomizedSearchCV
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.svm import SVC as SVM
from pathlib import Path
import pandas as pd

from src.extractor.lenght.count_words import CountWords

DATASET_PATH = '../../res/datasets/extracted/{}_dataset_ext.csv'


def perform_randomsearch(pipeline, dataset_name, parameters, folds=5, n_iter=10):
    """Performs RandomSearch for the specified pipeline and params"""
    dataset_path = Path(DATASET_PATH.format(dataset_name)).resolve()
    dataset = pd.read_csv(dataset_path)

    X = dataset.loc[:, dataset.columns != 'subjectivity']
    y = dataset['subjectivity']

    search = RandomizedSearchCV(pipeline, parameters, n_iter=n_iter, scoring='f1', cv=folds, verbose=10, n_jobs=10)
    search.fit(X, y)

    print(search.best_params_)


parameters_svm = {
    'C': (1, 10, 100, 1000),
    'class_weight': (None, 'balanced'),
    'kernel': ('linear', 'poly', 'rbf', 'sigmoid'),
    'gamma': ('auto', 'scale')
}


perform_randomsearch(SVM(), 'teste', parameters_svm, folds=3)
