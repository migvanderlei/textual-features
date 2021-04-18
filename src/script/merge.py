import csv, sys
import pandas as pd

OUT_NAMES = {
        '0': 'POS',
        '1': 'CONCEPT',
        '2': 'CONCEPT_ABS',
        '3': 'LEXICON',
        '4': 'SUBJECTIVITY',
        '5': 'SYNTACTIC_RULES',
        '6': 'TWITTER'
}

def merge_csv(path_sent, path_data, path_out):
    sentences = pd.read_csv(path_sent, sep='\t', quoting=csv.QUOTE_NONE)
    data = pd.read_csv(path_data, sep=',', quoting=csv.QUOTE_NONE)
    sentences = sentences[['sentence']]
    merged_data = sentences.merge(data, left_index=True, right_index=True, how='outer')
    merged_data.to_csv(path_out, index=False)

# def merge_csv(path_sent, path_data, path_out):
#     sentences = pd.read_csv(path_sent, sep='\t', quoting=csv.QUOTE_NONE)
#     data = pd.read_csv(path_data, sep=',', quoting=csv.QUOTE_NONE)
#     sentences = sentences[['sentence']]
#     merged_data = sentences.merge(data, left_index=True, right_index=True, how='outer')
#     merged_data.to_csv(path_out, index=False)

BASE_PATH='/home/miguel/Workspace/textual-features/res/datasets'

dataset=sys.argv[1]

# merge_csv('{}/raw/{}_dataset.tsv'.format(
#                         BASE_PATH, dataset),
#                 '{}/extracted/{}/{}_grouped_7_dataset_ext.csv'.format(
#                         BASE_PATH, dataset, dataset),
#                 '{}/extracted/{}/{}.csv'.format(
#                         BASE_PATH, dataset, dataset))
# for i in range(7):
#         merge_csv('{}/raw/{}_dataset.tsv'.format(
#                         BASE_PATH, dataset),
#                 '{}/extracted/{}/{}_unique_{}_dataset_ext.csv'.format(
#                         BASE_PATH, dataset, dataset, i),
#                 '{}/extracted/{}/{}_group_{}.csv'.format(
#                         BASE_PATH, dataset, dataset, OUT_NAMES[str(i)]))
