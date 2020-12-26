from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.svm import SVC as SVM
from pathlib import Path
import pandas as pd

from src.extractor.lenght.count_words import CountWords

DATASET_PATH = '../../res/datasets/{}.tsv'


def perform_gridsearch(pipeline, dataset_name, parameters, folds=10):
    """Performs GridSearchCV for the specified pipeline and params"""
    dataset_path = Path(DATASET_PATH.format(dataset_name)).resolve()
    dataset = pd.read_csv(dataset_path, sep='\t')

    gridsearch = GridSearchCV(pipeline, parameters, scoring='f1', cv=folds, verbose=10, n_jobs=10)
    gridsearch.fit(dataset['sentence'], dataset['subjectivity'])
    print(gridsearch.best_params_)


parameters_svm = {
    'clf__C': (1, 10, 100, 1000),
    'clf__class_weight': (None, 'balanced'),
    'clf__kernel': ('linear', 'poly', 'rbf', 'sigmoid'),
    'clf__gamma': ('auto', 'scale')
}

pipeline = Pipeline(steps=[
    ('features', FeatureUnion(
        transformer_list=[
            ('qtWords', CountWords()),
            ])),
    ('clf', SVM()),
])

perform_gridsearch(pipeline, 'teste', parameters_svm, folds=3)
