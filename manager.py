import argparse

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

args = parser.parse_args('--randomsearch -d reli -c 10 -i 200 --jobs 10'.split(" "))
print(args.randomsearch, args.dataset, args.crossval, args.jobs)

if args.extract:
    if args.dataset:
        print("Extract {} dataset".format(args.dataset))
    else:
        print("Extract datasets")
if args.randomsearch:
    if args.dataset:
        crossval = args.crossval if args.crossval else 5
        iterations = args.iter if args.iter else 100
        verbose = args.verbose if args.verbose else 10
        jobs = args.jobs if args.jobs else 10

        print("Run RandomSearch for {} with {} folds, {} iterations, {} verbosity level, {} jobs"
              .format(args.dataset, crossval, iterations, verbose, jobs))
    else:
        print("Run RandomSearch for all datasets")
