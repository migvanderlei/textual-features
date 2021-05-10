from sklearn.pipeline import FeatureUnion, Pipeline
import pandas as pd
from functools import reduce
from src.utils.features_list import ALL_FEATURES, RAW_TEXT_FEATURES
from src.utils.spacy_preprocessor import SpacyPreprocessor
from src.utils.csv_generator import generate_file
from src.utils.paths import PATH_DIR
from tqdm import tqdm
import numpy as np
import csv, sys

DATASET_PATH = PATH_DIR+"res/datasets/raw/{}_dataset.tsv"

RAW_TEXT_FEATURES_NAMES = [feature[0] for feature in RAW_TEXT_FEATURES]
SPACY_FEATURES = [feature for feature in ALL_FEATURES if feature[0] not in RAW_TEXT_FEATURES_NAMES]


# def feature_extraction(dataset_name):
#     try:
#         dataset_path = DATASET_PATH.format(dataset_name)

#         data = pd.read_csv(dataset_path, sep='\t', quoting=csv.QUOTE_NONE)
#         raw_sentences = data['sentence']
#         spacy_union = FeatureUnion(transformer_list=SPACY_FEATURES)

#         pipeline = Pipeline(steps=[
#             (features, FeatureUnion(
#                 transformer_list=RAW_TEXT_FEATURES + [('spacy', Pipeline(steps=[
#                         ('spacy_preprocessor', SpacyPreprocessor()),
#                         ('spacy_features', spacy_union)
#                     ]))],
#             ))
#         ])

#         features = pipeline.fit_transform(raw_sentences)

#         generate_file(features, RAW_TEXT_FEATURES+SPACY_FEATURES, dataset_name)
#     except FileNotFoundError:
#         print("Path do arquivo não econtrado: {}".format(dataset_path))
#     except Exception as err:
#         print(err)

# def extract_variations(dataset):
#     all_features = [POS_FEATURES_LIST, CONCEPT_FEATURES_LIST, CONCEPT_FEATURES_LIST_ABS,LEXICON_FEATURES_LIST,SUBJECTIVITY_FEATURES_LIST, SYNTACTIC_RULES_FEATURES_LIST, TWITTER_FEATURES_LIST]

#     dataset_path = DATASET_PATH.format(dataset)

#     data = pd.read_csv(dataset_path, sep='\t', quoting=csv.QUOTE_NONE)
#     raw_sentences = data['sentence']

#     for i in tqdm(range(len(all_features)+1)):
#         features = all_features[:]
#         if i < len(all_features):
#             features.pop(i)
#         features = reduce(lambda x, y: x+y, features)
#         # print('total', len(features))
#         # getting raw text to process later
#         raw_text_features = list(filter(lambda x: x[0] in RAW_TEXT_FEATURES_NAMES, features))
#         # print('total de texto puro', len(list(raw_text_features)))
#         filtered_features = list(filter(lambda x: x[0] not in RAW_TEXT_FEATURES_NAMES, features))
#         # print('total filtrado', len(list(filtered_features)))

#         spacy_union = FeatureUnion(transformer_list=filtered_features)
        
#         pipeline = Pipeline(steps=[
#             ('features', FeatureUnion(
#                 transformer_list=raw_text_features + [('spacy', Pipeline(steps=[
#                         ('spacy_preprocessor', SpacyPreprocessor()),
#                         ('spacy_features', spacy_union)
#                     ]))],
#             ))
#         ])

#         extracted = pipeline.fit_transform(raw_sentences)

#         generate_file(extracted, features, dataset, '_grouped_{}'.format(i))

# def extract_single(dataset):
#     all_features = [POS_FEATURES_LIST, CONCEPT_FEATURES_LIST, CONCEPT_FEATURES_LIST_ABS,LEXICON_FEATURES_LIST,SUBJECTIVITY_FEATURES_LIST, SYNTACTIC_RULES_FEATURES_LIST, TWITTER_FEATURES_LIST]

#     dataset_path = DATASET_PATH.format(dataset)

#     data = pd.read_csv(dataset_path, sep='\t', quoting=csv.QUOTE_NONE)
#     raw_sentences = data['sentence']

#     for i in tqdm(range(len(all_features))):
#         features = all_features[i]
#         # getting raw text to process later
#         raw_text_features = list(filter(lambda x: x[0] in RAW_TEXT_FEATURES_NAMES, features))
#         # print('total de texto puro', len(list(raw_text_features)))
#         filtered_features = list(filter(lambda x: x[0] not in RAW_TEXT_FEATURES_NAMES, features))
#         # print('total filtrado', len(list(filtered_features)))

#         spacy_union = FeatureUnion(transformer_list=filtered_features)
        
#         pipeline = Pipeline(steps=[
#             ('features', FeatureUnion(
#                 transformer_list=raw_text_features + [('spacy', Pipeline(steps=[
#                         ('spacy_preprocessor', SpacyPreprocessor()),
#                         ('spacy_features', spacy_union)
#                     ]))],
#             ))
#         ])

#         extracted = pipeline.fit_transform(raw_sentences)

#         generate_file(extracted, features, dataset, '_unique_{}'.format(i))

def new_extraction(dataset, ablation=True, unique=True):
    extracted_features = []

    dataset_path = DATASET_PATH.format(dataset)

    data = pd.read_csv(dataset_path, sep='\t', quoting=csv.QUOTE_NONE)
    raw_sentences = data['sentence']
    print("extracting groups of features...")
    for features, i in zip(ALL_FEATURES, range(len(ALL_FEATURES))):
        raw_text_features = list(filter(lambda x: x[0] in RAW_TEXT_FEATURES_NAMES, features))
        filtered_features = list(filter(lambda x: x[0] not in RAW_TEXT_FEATURES_NAMES, features))
        
        if len(filtered_features) > 0:
            spacy_union = FeatureUnion(transformer_list=filtered_features)
            pipeline = Pipeline(steps=[
                ('features', FeatureUnion(
                    transformer_list=raw_text_features + [('spacy', Pipeline(steps=[
                            ('spacy_preprocessor', SpacyPreprocessor()),
                            ('spacy_features', spacy_union)
                        ]))],
                ))
            ])
        else:
            pipeline = Pipeline(steps=
                [('features', FeatureUnion(transformer_list=raw_text_features))]
            )
        extracted = pipeline.fit_transform(raw_sentences)

        extracted_features.append(extracted)
        print("extracted {}/{} groups...".format(i+1, len(ALL_FEATURES)))
    
    print("finished extracting groups")

    if ablation:
        print("creating files for ablation study...")
        for i in range(len(extracted_features)+1):
            features_group = ALL_FEATURES[:]
            features = extracted_features[:]
            if i < len(extracted_features):
                features_group.pop(i)
                features.pop(i)
            features = np.concatenate(tuple(features), axis=1)
            features_group = reduce(lambda x, y: x+y, features_group)
            if i < len(extracted_features):
                generate_file(features, features_group, dataset, '_groups_{}'.format(i))
            else:    
                generate_file(features, features_group, dataset, '_all_groups')
            print("created {}/{} files...".format(i+1, len(extracted_features)))
        print("finished creating files for ablation study")
    
    if unique:
        features = []
        print("creating files for unique groups...")     
        for i in range(len(extracted_features)):
            features = extracted_features[i]
            generate_file(features, ALL_FEATURES[i], dataset, '_unique_{}'.format(i))
            print("created {}/{} files...".format(i+1, len(extracted_features)))
        print("finished creating files for unique groups")

    print("finished extraction process")


if __name__ == "__main__":
    # dataset=sys.argv[1]
    # for dataset in ['reli', 'hotel', 'computerbr', 'tripadvisor']:
    for dataset in ['comp_twitter', 'comp_buscape']:
        new_extraction(dataset)
    # extract_single(dataset)
