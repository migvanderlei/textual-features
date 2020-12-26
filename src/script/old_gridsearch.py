import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline, FeatureUnion
from features import *
import argparse

# args
parser = argparse.ArgumentParser()
parser.add_argument('--task', help='Task 1 ou 2')
parser.add_argument('--ds', help='Dataset [books, restaurants, tweets, apps]')
parser.add_argument('--jobs', help="Numero de jobs executados. Default = 4")
parser.add_argument('--cv', help="Numero de folds. Default = 10")
parser.add_argument('--clf', help="Classifier. 0 = SVM; 1 = GBT. Default = 0")
args = parser.parse_args()

# fazendo parsing dos argumentos
jobs = 1
task = '1'
dataset = 'books'
classifier = 0
cv = 10

if args.jobs is not None:
    jobs = int(args.jobs)
if args.cv is not None:
    _cv = int(args.cv)
if args.task is not None:
    task = args.task
if args.ds is not None:
    if args.ds == 'apps' and args.task == '1':
        raise ValueError("Dataset apps não disponível para a tarefa 1")
    else:
        dataset = args.ds
if args.clf is not None:
    classifier = int(args.clf)

# lendo os dados
csv_file_name = './data/task{}/{}.tsv'.format(task, dataset)

print("Task: {}\nDataset: {}\nClassifier: {}\nCross Validation: {} folds\nJobs: {}"
      .format("Subjectivity (1)" if task == "1" else "Polarity (2)", dataset,
              "Support Vector Machine" if classifier == 0 else "Gradient Bosting Trees", cv, jobs))
print("-- Arquivos carregados --")

data = pd.read_csv(csv_file_name, sep="\t", dtype={'sentence': 'object'})
data.fillna('', inplace=True)
print(data.has_opinion.unique())

corpus = data.sentence
if task == '1':
    targets = data.has_opinion
else:
    targets = data.polarity

classifiers = [
    SVC(random_state=42),
    GradientBoostingClassifier(random_state=42)
]

# features
pipeline = Pipeline(steps=[
    ('features', FeatureUnion(
        transformer_list=[
            ('qtWords', CountWords()),
            ('tree', Pipeline([
                ('spacy', SpacyTransformer()),
                ('tree_features', FeatureUnion(
                    transformer_list=[
                        ('qtAdjectives', CountAdjectives()),
                        ('qtComparatives', CountComparatives()),
                        ('qtSuperlatives', CountSuperlatives()),
                        ('qtAdverbs', CountAdverbs()),
                        ('qtNouns', CountNouns()),
                        ('qtAmod', CountAmod()),
                    ]+['qtAmod2', CountAmod()]))
            ]))
        ],
    )),
    ('clf', classifiers[classifier]),
])

print("-- Pipeline preparada --")

parameters_svm = {
    'clf__C': (1, 10, 100, 1000),
    'clf__class_weight': (None, 'balanced'),
    'clf__kernel': ('linear', 'poly', 'rbf', 'sigmoid'),
    'clf__gamma': ('auto', 'scale')
}

parameters_gbt = {
    'clf__learning_rate': (0.01, 0.1, 0.5, 1),
    'clf__max_depth': (1, 3, 6, 8, 9),
    'clf__min_samples_leaf': (1, 2, 4),
    'clf__n_estimators': (1, 10, 100),
}

parameters = [parameters_svm, parameters_gbt]

grid_search = GridSearchCV(pipeline, parameters[classifier], scoring='f1', cv=cv, verbose=10, n_jobs=jobs)

print("-- Iniciando GridSearch --")
print("pipeline:", [name for name, _ in pipeline.steps])
grid_search.fit(corpus, targets)

print("\nBest score: %0.3f" % grid_search.best_score_)
print("Best parameters set:")
best_parameters = grid_search.best_estimator_.get_params()
for param_name in sorted(parameters[classifier].keys()):
    print("\t%s: %r" % (param_name, best_parameters[param_name]))
