from src.extractor.pos import *
from src.extractor.concept import *

POS_FEATURES_LIST = [
    ('pos_adj', CountAdj()),
    ('pos_adp', CountAdp()),
    ('pos_adv', CountAdj()),
    ('pos_aux', CountAux()),
    ('pos_cconj', CountCconj()),
    ('pos_det', CountDet()),
    ('pos_intj', CountIntj()),
    ('pos_noun', CountNoun()),
    ('pos_num', CountNum()),
    ('pos_part', CountPart()),
    ('pos_pron', CountPron()),
    ('pos_propn', CountPropn()),
    ('pos_punct', CountPunct()),
    ('pos_sconj', CountSconj()),
    ('pos_sym', CountSym()),
    ('pos_verb', CountVerb()),
    ('pos_x', CountX()),
]

CONCEPT_FEATURES_LIST = [
    ('concept_aptitude_avg', AptitudeScore(False, True)),
    ('concept_aptitude_sum', AptitudeScore(False, False)),
    ('concept_attention_avg', AttentionScore(False, True)),
    ('concept_attention_sum', AttentionScore(False, False)),
    ('concept_pleasantness_avg', PleasantnessScore(False, True)),
    ('concept_pleasantness_sum', PleasantnessScore(False, False)),
    ('concept_polarity_avg', PolarityScore(False, True)),
    ('concept_polarity_sum', PolarityScore(False, False)),
    ('concept_sensitivity_avg', SensitivityScore(False, True)),
    ('concept_sensitivity_sum', SensitivityScore(False, False)),
]

CONCEPT_FEATURES_LIST_ABS = [
    ('concept_aptitude_avg_abs', AptitudeScore(True, True)),
    ('concept_aptitude_sum_abs', AptitudeScore(True, False)),
    ('concept_attention_avg_abs', AttentionScore(True, True)),
    ('concept_attention_sum_abs', AttentionScore(True, False)),
    ('concept_pleasantness_avg_abs', PleasantnessScore(True, True)),
    ('concept_attention_sum_abs', PleasantnessScore(True, False)),
    ('concept_polarity_avg_abs', PolarityScore(True, True)),
    ('concept_polarity_sum_abs', PolarityScore(True, False)),
    ('concept_sensitivity_avg_abs', SensitivityScore(True, True)),
    ('concept_sensitivity_sum_abs', SensitivityScore(True, False)),
]
