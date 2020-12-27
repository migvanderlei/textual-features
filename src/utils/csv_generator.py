from pathlib import Path
import pandas as pd
import numpy as np

EXTRACTED_PATH = '../../res/datasets/extracted/{}_dataset_ext.csv'
DATASET_PATH = '../../res/datasets/{}_dataset.tsv'
TARGET = 'subjectivity'


def get_feature_names(features):
    return [feature[0] for feature in features]


def generate_file(feature_arrays, feature_names, name):
    """Create CSV file from data as a Numpy matrix and a list of string columns"""
    extracted_path = Path(EXTRACTED_PATH.format(name)).resolve()
    dataset_path = Path(DATASET_PATH.format(name)).resolve()

    data = pd.read_csv(dataset_path, sep='\t')
    target = data[TARGET].to_numpy().reshape(-1, 1)

    columns = get_feature_names(feature_names) + [TARGET]

    feature_arrays = np.append(feature_arrays, target, axis=1)
    extracted_dataset = [columns] + feature_arrays.tolist()

    content = []
    for line in extracted_dataset:
        content.append(",".join([str(x) for x in line]))

    with open(extracted_path, 'w+') as f:
        f.write("\n".join(content))

    print("created dataset file with {} lines and {} columns".format(len(content)-1, len(columns)))
