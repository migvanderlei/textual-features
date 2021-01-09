from pathlib import Path
import pandas as pd
from src.utils.paths import PATH_DIR
from datetime import datetime
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split

DATASET_PATH = PATH_DIR + 'res/datasets/extracted/{}_dataset_ext.csv'


def perform_ablation(clf, dataset_name):
    """Performs ablation study"""
    dataset_path = Path(DATASET_PATH.format(dataset_name)).resolve()
    dataset = pd.read_csv(dataset_path)

    X = dataset.loc[:, dataset.columns != 'subjectivity']
    y = dataset['subjectivity']
    features = X.columns
    results = []
    for feature in features:
        X_less = X.loc[:, X.columns != feature]

        X_train, X_test, y_train, y_test = train_test_split(X_less, y, test_size=0.30, random_state=42)

        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        score = f1_score(y_pred, y_test)
        results.append((score, feature))

    results.sort(key=lambda tup: tup[0])

    with open("{}logs/{}_ablation_{}.log".format(
            PATH_DIR, datetime.now().strftime("%m-%d-%Y-%H-%M-%S"), dataset_name), "w+") as f:
        f.write('\n'.join('{} {}'.format(x[0], x[1]) for x in results))
