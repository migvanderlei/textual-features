import csv
import pandas as pd
def merge_csv(path_sent, path_data, path_out):
    sentences = pd.read_csv(path_sent, sep='\t', quoting=csv.QUOTE_NONE)
    data = pd.read_csv(path_data, sep=',', quoting=csv.QUOTE_NONE)
    sentences = sentences[['sentence']]
    merged_data = sentences.merge(data, left_index=True, right_index=True, how='outer')
    merged_data.to_csv(path_out, index=False)

merge_csv('/home/miguel/Workspace/textual-features/res/datasets/raw/computerbr_dataset.tsv',
        '/home/miguel/Workspace/textual-features/res/datasets/extracted/computerbr_dataset_ext.csv',
        '/home/miguel/Workspace/textual-features/res/datasets/extracted/computerbr_dataset_sent.csv')
merge_csv('/home/miguel/Workspace/textual-features/res/datasets/raw/reli_dataset.tsv',
        '/home/miguel/Workspace/textual-features/res/datasets/extracted/reli_dataset_ext.csv',
        '/home/miguel/Workspace/textual-features/res/datasets/extracted/reli_dataset_sent.csv')
merge_csv('/home/miguel/Workspace/textual-features/res/datasets/raw/tripadvisor_dataset.tsv',
        '/home/miguel/Workspace/textual-features/res/datasets/extracted/tripadvisor_dataset_ext.csv',
        '/home/miguel/Workspace/textual-features/res/datasets/extracted/tripadvisor_dataset_sent.csv')
