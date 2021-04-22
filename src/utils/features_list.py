from src.extractor.pos import *
from src.extractor.concept import *
from src.extractor.lenght import *
from src.extractor.lexicon import *
from src.extractor.positional import *
from src.extractor.subjectivity import *
from src.extractor.syntactic_rules import *
from src.extractor.twitter import *

POS_FEATURES_LIST = [
    ('pos_adj', CountAdj()),
    ('pos_adp', CountAdp()),
    ('pos_adv', CountAdv()),
    ('pos_aux', CountAux()),
    ('pos_cconj', CountCconj()),
    ('pos_det', CountDet()),
    ('pos_intj', CountIntj()),
    ('pos_noun', CountNoun()),
    ('pos_num', CountNum()),
    ('pos_pron', CountPron()),
    ('pos_propn', CountPropn()),
    ('pos_punct', CountPunct()),
    ('pos_sconj', CountSconj()),
    ('pos_sym', CountSym()),
    ('pos_verb', CountVerb()),
    ('pos_x', CountX()),
    ('pos_comparatives', CountComparatives()),
    ('pos_superlatives', CountSuperlatives()),
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
    ('concept_pleasantness_sum_abs', PleasantnessScore(True, False)),
    ('concept_polarity_avg_abs', PolarityScore(True, True)),
    ('concept_polarity_sum_abs', PolarityScore(True, False)),
    ('concept_sensitivity_avg_abs', SensitivityScore(True, True)),
    ('concept_sensitivity_sum_abs', SensitivityScore(True, False)),
]

LEXICON_FEATURES_LIST = [
    ('lexicon_subjective', LexiconSubjective()),
    ('lexicon_positive', LexiconPositive()),
    ('lexicon_negative', LexiconNegative()),
    ('lexicon_quotation_exclamation', LexiconQuotationExclamation()),
    ('lexicon_subjective_prop', LexiconSubjective(True)),
    ('lexicon_positive_prop', LexiconPositive(True)),
    ('lexicon_negative_prop', LexiconNegative(True)),
    ('lexicon_quotation_exclamation_prop', LexiconQuotationExclamation(True)),
]

MISCELLANEOUS_FEATURES_LIST = [
    ('count_dictionary_words', CountDictionaryWords()),
    ('count_named_entities', CountNE()),
    ('count_number_date_time', CountNumberDateTime()),
]

SYNTACTIC_RULES_FEATURES_LIST = [
    ('rule1', SyntacticRule1()),
    ('rule2', SyntacticRule2()),
    ('rule3', SyntacticRule3()),
    ('rule4', SyntacticRule4()),
    ('rule5', SyntacticRule5()),
]

TEXT_STRUCTURE_FEATURES_LIST = [
    ('count_words', CountWords()),
    ('count_capitalized_words', CountCapitalizedWords()),
    ('proportion_capitalized_words', ProportionCapitalizedWords()),
    ('count_capitalized_chars', CountCapitalizedChars()),
    ('proportion_capitalized_chars', ProportionCapitalizedChars()),
]

TWITTER_FEATURES_LIST = [
    ('count_url', CountURL()),
    ('count_elongated', CountElongated()),
    ('count_mentions', CountMentions()),
    ('emoji_polarity_score', EmojiPolarityScore()),
    ('emoticon_polarity_score', EmoticonPolarityScore()),
]

RAW_TEXT_FEATURES = [
    ('count_words', CountWords()),
    ('count_capitalized_words', CountCapitalizedWords()),
    ('proportion_capitalized_words', ProportionCapitalizedWords()),
    ('count_capitalized_chars', CountCapitalizedChars()),
    ('proportion_capitalized_chars', ProportionCapitalizedChars()),
    ('count_url', CountURL()),
    ('count_elongated', CountElongated()),
    ('count_mentions', CountMentions()),
    ('count_dictionary_words', CountDictionaryWords()),
]

# ALL_FEATURES_POSITIONAL = CONCEPT_FEATURES_LIST + LENGHT_FEATURES_LIST + LEXICON_FEATURES_LIST \
#                           + POS_FEATURES_LIST + POSITIONAL_FEATURES_LIST + SUBJECTIVITY_FEATURES_LIST \
#                           + SYNTACTIC_RULES_FEATURES_LIST

# ALL_FEATURES_TWITTER = CONCEPT_FEATURES_LIST + LENGHT_FEATURES_LIST_WORDS + LEXICON_FEATURES_LIST \
#                           + POS_FEATURES_LIST + SUBJECTIVITY_FEATURES_LIST + SYNTACTIC_RULES_FEATURES_LIST\
#                           + TWITTER_FEATURES_LIST
# ALL_FEATURES_CONCEPT_INTEGER = CONCEPT_FEATURES_LIST + LENGHT_FEATURES_LIST_WORDS + LEXICON_FEATURES_LIST \
#                 + POS_FEATURES_LIST

ALL_FEATURES = [POS_FEATURES_LIST, SYNTACTIC_RULES_FEATURES_LIST, LEXICON_FEATURES_LIST, \
                CONCEPT_FEATURES_LIST, CONCEPT_FEATURES_LIST_ABS, MISCELLANEOUS_FEATURES_LIST, \
                TWITTER_FEATURES_LIST, TEXT_STRUCTURE_FEATURES_LIST]