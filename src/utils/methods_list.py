from sklearn.svm import SVC
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
import numpy as np

CLASSIFIERS_LIST = [
    {'id': 'svm',
     'clf': SVC(),
     'parameters':
         {'C': (1, 10, 100, 1000),
          'class_weight': [None, 'balanced'],
          'kernel': ['linear', 'poly', 'rbf', 'sigmoid'],
          'gamma': ['auto', 'scale'],
          }
     },
    {'id': 'lr',
     'clf': LogisticRegression(),
     'parameters':
         {'penalty': ['l1', 'l2'],
          'C': [0.001, 0.01, 1, 10, 100, 1000],
          'solver': ['lbfgs', 'liblinear', 'sag', 'saga']
          }
     },
    {'id': 'rf',
     'clf': RandomForestClassifier(),
     'parameters':
         {'max_depth': [1, 3, 6, 8, 9],
          'min_samples_leaf': [1, 2, 4],
          'max_features': ['auto', 'sqrt'],
          'n_estimators': [x for x in range(100, 1001, 100)],
          }
     },
    {'id': 'gbt',
     'clf': GradientBoostingClassifier(),
     'parameters':
         {'learning_rate': [0.01, 0.1, 0.5, 1],
          'max_depth': [1, 3, 6, 8, 9],
          'min_samples_leaf': [1, 2, 4],
          'n_estimators': [x for x in range(100, 1001, 100)],
          }
     },
]
