from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC
import pandas as pd
import numpy as np
from src.utils.paths import PATH_DIR
from datetime import datetime
from sklearn.metrics import classification_report, f1_score, make_scorer

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

def perform_report(execution_id, model, dataset_name, group, n_jobs=8, model_name='svm', unique=False, folds=5):
    """Performs RandomSearch for the specified pipeline and params"""
    global REPORT_FILENAME 
    dataset_path = ''
    if group != 7:
        dataset_path = DATASET_PATH.format(dataset_name, dataset_name,
                                     "unique" if unique else "groups", str(group))
    else:
        dataset_path = PATH_DIR+'res/datasets/extracted/{}/{}_all_groups_dataset_ext.csv' \
            .format(dataset_name, dataset_name)

    REPORT_FILENAME = REPORT_FILENAME.format(
        PATH_DIR, dataset_name, dataset_name, 'REPORT_FINAL', OUT_NAMES[str(group)], model_name, datetime.now().strftime("%Y-%m-%d-%H-%M"))

    print(dataset_path)
    dataset = pd.read_csv(dataset_path)
    
    X = dataset.loc[:, dataset.columns != 'subjectivity']
    y = dataset['subjectivity']

    report = cross_val_score(model, X=X, y=y, cv=folds, n_jobs=n_jobs,
               scoring=make_scorer(classification_report_with_f1_score))
    print("[{}] F-1 scores for validation:".format(execution_id), report) 
    REPORT_FILENAME = "{}logs/{}/{}_{}_{}_{}_{}.txt"

def classification_report_with_f1_score(y_true, y_pred):
    global REPORT_FILENAME 
    with open(REPORT_FILENAME, 'a+') as f:
        print(classification_report(
            y_true, y_pred, target_names=['objective', 'subjective'], digits=16
            )+"\n"+"-"*85, file=f)
    return f1_score(y_true, y_pred)

MODELS = [
    ("HOTEL_ALL", SVC(kernel='rbf', gamma='scale', class_weight=None, C=10), 'hotel', 7),
    ("HOTEL_POS", SVC(kernel='rbf', gamma='scale', class_weight=None, C=10), 'hotel', 0),
    ("HOTEL_SYNTACTIC_RULES", SVC(kernel='rbf', gamma='scale', class_weight=None, C=10), 'hotel', 1),
    ("HOTEL_LEXICON", SVC(kernel='rbf', gamma='scale', class_weight=None, C=10), 'hotel', 2),
    ("HOTEL_CONCEPT", SVC(kernel='rbf', gamma='scale', class_weight=None, C=10), 'hotel', 3),
    ("HOTEL_MISCELLANEOUS", SVC(kernel='rbf', gamma='auto', class_weight=None, C=1), 'hotel', 4),
    ("HOTEL_TWITTER", SVC(kernel='rbf', gamma='scale', class_weight=None, C=10), 'hotel', 5),
    ("HOTEL_TEXT_STRUCTURE", SVC(kernel='rbf', gamma='scale', class_weight=None, C=1), 'hotel', 6),

    ("TRIPADVISOR_ALL", SVC(kernel='rbf', gamma='scale', class_weight=None, C=10), 'tripadvisor', 7),
    ("TRIPADVISOR_POS", SVC(kernel='linear', gamma='auto', class_weight=None, C=10), 'tripadvisor', 0),
    ("TRIPADVISOR_SYNTACTIC_RULES", SVC(kernel='rbf', gamma='scale', class_weight=None, C=10), 'tripadvisor', 1),
    ("TRIPADVISOR_LEXICON", SVC(kernel='linear', gamma='auto', class_weight=None, C=0.01), 'tripadvisor', 2),
    ("TRIPADVISOR_CONCEPT", SVC(kernel='linear', gamma='auto', class_weight=None, C=0.01), 'tripadvisor', 3),
    ("TRIPADVISOR_MISCELLANEOUS", SVC(kernel='linear', gamma='auto', class_weight=None, C=0.01), 'tripadvisor', 4),
    ("TRIPADVISOR_TWITTER", SVC(kernel='rbf', gamma='scale', class_weight=None, C=10), 'tripadvisor', 5),
    ("TRIPADVISOR_TEXT_STRUCTURE", SVC(kernel='rbf', gamma='scale', class_weight=None, C=10), 'tripadvisor', 6),

    ("COMPUTERBR_ALL", SVC(kernel='linear', gamma='auto', class_weight='balanced', C=1000), 'computerbr', 7),
    ("COMPUTERBR_POS", SVC(kernel='linear', gamma='auto', class_weight='balanced', C=0.01), 'computerbr', 0),
    ("COMPUTERBR_SYNTACTIC_RULES", SVC(kernel='linear', gamma='auto', class_weight='balanced', C=1), 'computerbr', 1),
    ("COMPUTERBR_LEXICON", SVC(kernel='linear', gamma='auto', class_weight='balanced', C=100), 'computerbr', 2),
    ("COMPUTERBR_CONCEPT", SVC(kernel='linear', gamma='auto', class_weight='balanced', C=1000), 'computerbr', 3),
    ("COMPUTERBR_MISCELLANEOUS", SVC(kernel='linear', gamma='auto', class_weight='balanced', C=0.01), 'computerbr', 4),
    ("COMPUTERBR_TWITTER", SVC(kernel='linear', gamma='auto', class_weight='balanced', C=0.01), 'computerbr', 5),
    ("COMPUTERBR_TEXT_STRUCTURE", SVC(kernel='rbf', gamma='scale', class_weight='balanced', C=1), 'computerbr', 6),

    ("RELI_ALL", SVC(kernel='linear', gamma='auto', class_weight=None, C=1000), 'reli', 7),
    ("RELI_POS", SVC(kernel='rbf', gamma='scale', class_weight=None, C=10), 'reli', 0),
    ("RELI_SYNTACTIC_RULES", SVC(kernel='poly', gamma='auto', class_weight=None, C=1), 'reli', 1),
    ("RELI_LEXICON", SVC(kernel='poly', gamma='auto', class_weight=None, C=0.1), 'reli', 2),
    ("RELI_CONCEPT", SVC(kernel='linear', gamma='auto', class_weight=None, C=10), 'reli', 3),
    ("RELI_MISCELLANEOUS", SVC(kernel='linear', gamma='auto', class_weight=None, C=1000), 'reli', 4),
    ("RELI_TWITTER", SVC(kernel='linear', gamma='auto', class_weight=None, C=1000), 'reli', 5),
    ("RELI_TEXT_STRUCTURE", SVC(kernel='rbf', gamma='scale', class_weight=None, C=10), 'reli', 6),
]

for name, model, dataset_name, group in MODELS:
    perform_report(name, model, dataset_name, group, n_jobs=8, model_name='svm', unique=False, folds=5)