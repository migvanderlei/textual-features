import argparse
from src.utils.methods_list import CLASSIFIERS_LIST

parser = argparse.ArgumentParser(description='Manage operations like feature extraction and parameter search')
parser.add_argument('--extract', help='Extract features from text. Specify --dataset (-d) '
                                      'or it will run for all datasets.', dest='extract', action='store_true')
parser.add_argument('--randomsearch', help='Perform RamdomizedSearchCV Specify --dataset (-d) '
                                           'or it will run for all datasets. Check default params.',
                    dest='randomsearch', action='store_true')
parser.add_argument('--dataset', '-d', help='Dataset name. [computerbr, reli, tripadvidor, teste]', dest='dataset')
parser.add_argument('--crossval', '-c', help='Cross validation number of folds (default = 5)', dest='crossval')
parser.add_argument('--iter', '-i', help='Number of iterations on RandomizedSearchCV (default = 100)', dest='iter')
parser.add_argument('--verbose', '-v', help='Verbosity level (default = 10)', dest='verbose')
parser.add_argument('--jobs', '-j', help='Number of threads (default = 10)', dest='jobs')
parser.add_argument('--clf', help='Method to run. Specify one from list [svm, lr, rf, gbt]', dest='clf')

args = parser.parse_args()

if args.extract:
    from src.script.feature_extraction import feature_extraction
    if args.dataset:
        if args.dataset in ['computerbr', 'reli', 'tripadvisor']:
            print("Extract {} dataset".format(args.dataset))
            feature_extraction(args.dataset)
            print("{} extraction finished".format(args.dataset))
        else:
            print("{} not a dataset. Finishing.".format(args.dataset))

    else:
        for dataset in ['computerbr', 'reli', 'tripadvisor']:
            print("Extracting {} dataset".format(dataset))
            # feature_extraction(dataset)
            print("{} extraction finished".format(dataset))

if args.randomsearch:
    if args.clf:
        from src.script.randomsearch import perform_randomsearch

        if args.dataset:
            crossval = int(args.crossval) if args.crossval else 5
            iterations = int(args.iter) if args.iter else 100
            verbose = int(args.verbose) if args.verbose else 10
            jobs = int(args.jobs) if args.jobs else 10
            clf_name = args.clf

            print("Running RandomSearch for {} with {} folds, {} iterations, {} verbosity level, {} jobs and method {}"
                  .format(args.dataset, crossval, iterations, verbose, jobs, clf_name))

            elem = [elem for elem in CLASSIFIERS_LIST if elem['id'] == clf_name][0]
            clf = elem['clf']
            parameters = elem['parameters']

            perform_randomsearch(clf, args.dataset, parameters, crossval, iterations, verbose, jobs)
        else:
            print("Running RandomSearch for all datasets")
            for dataset in ['computerbr', 'reli', 'tripadvisor']:
                crossval = int(args.crossval) if args.crossval else 5
                iterations = int(args.iter) if args.iter else 100
                verbose = int(args.verbose) if args.verbose else 10
                jobs = int(args.jobs) if args.jobs else 10
                clf_name = args.clf

                print("Running RandomSearch for {} with {} folds, {} iterations, {} verbosity level, {} jobs and "
                      "method {} "
                      .format(dataset, crossval, iterations, verbose, jobs, clf_name))

                elem = [elem for elem in CLASSIFIERS_LIST if elem['id'] == clf_name][0]
                clf = elem['clf']
                parameters = elem['parameters']

                perform_randomsearch(clf, dataset, parameters, crossval, iterations, verbose, jobs)

    else:
        print("Classifier must be specified with --clf. Specify one from list [svm, lr, rf, gbt]")
