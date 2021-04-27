import csv, sys
import pandas as pd

OUT_NAMES = {
        '0': 'POS',
        '1': 'SYNTACTIC_RULES',
        '2': 'LEXICON',
        '3': 'CONCEPT_ABS',
        '4': 'MISCELLANEOUS',
        '5': 'TWITTER',
        '6': 'TEXT_STRUCTURE'
}

def merge_csv(path_sent, path_data, path_out):
    sentences = pd.read_csv(path_sent, sep='\t', quoting=csv.QUOTE_NONE)
    data = pd.read_csv(path_data, sep=',', quoting=csv.QUOTE_NONE)
    sentences = sentences[['sentence']]
    merged_data = sentences.merge(data, left_index=True, right_index=True, how='outer')
    merged_data.to_csv(path_out, index=False)

BASE_PATH='/home/miguel/Workspace/textual-features/res/datasets'

dataset=sys.argv[1]

merge_csv('{}/raw/{}_dataset.tsv'.format(
                        BASE_PATH, dataset),
                '{}/extracted/{}/{}_all_groups_dataset_ext.csv'.format(
                        BASE_PATH, dataset, dataset),
                '{}/extracted/{}/sentences/{}_all_groups.csv'.format(
                        BASE_PATH, dataset, dataset))
for i in range(7):
        merge_csv('{}/raw/{}_dataset.tsv'.format(
                        BASE_PATH, dataset),
                '{}/extracted/{}/{}_unique_{}_dataset_ext.csv'.format(
                        BASE_PATH, dataset, dataset, i),
                '{}/extracted/{}/sentences/{}_group_{}.csv'.format(
                        BASE_PATH, dataset, dataset, OUT_NAMES[str(i)]))
