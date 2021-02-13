from sklearn.svm import SVC
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
import numpy as np

CLASSIFIERS_LIST = [
    {'id': 'svm',
     'clf': SVC(),
     'parameters':
         {'C': [0.01, 0.1, 1, 10, 100, 1000],
          'class_weight': [None, 'balanced'],
          'kernel': ['linear', 'poly', 'rbf'],
          'gamma': ['auto', 'scale'],
          }
     },
    {'id': 'lr',
     'clf': LogisticRegression(),
     'parameters':
         {'penalty': ['l2'],
          'C': [0.001, 0.01, 1, 10, 100, 1000],
          'max_iter': list(range(100, 2001, 100)),
          'solver': ['newton-cg', 'lbfgs', 'liblinear']
          }
     },
    {'id': 'rf',
     'clf': RandomForestClassifier(),
     'parameters':
         {'max_depth': [2**x for x in range(2, 10)],
          'min_samples_leaf': [1, 2, 4, 8, 12, 16, 32],
          'n_estimators': [2**x for x in range(2, 12)],
          }
     },
    {'id': 'gbt',
     'clf': GradientBoostingClassifier(),
     'parameters':
         {'learning_rate': [0.001, 0.01, 0.1, 0.5, 1],
          'max_depth': [2**x for x in range(2, 10)],
          'min_samples_leaf': [1, 2, 4, 8, 12, 16, 32],
          'n_estimators': [2**x for x in range(2, 12)],
          }
     },
]

CLASSIFIERS_PARAMETERS = {
    'tripadvisor': GradientBoostingClassifier(min_samples_leaf=1, max_depth=1, learning_rate=0.5, n_estimators=300),
    'computerbr': SVC(kernel='rbf', gamma='scale', class_weight='balanced', C=10),
    'reli': SVC(kernel='sigmoid', gamma='auto', class_weight=None, C=0.01)
}
