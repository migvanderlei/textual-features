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
    ('concept_pleasantness_sum_abs', PleasantnessScore(True, False)),
    ('concept_polarity_avg_abs', PolarityScore(True, True)),
    ('concept_polarity_sum_abs', PolarityScore(True, False)),
    ('concept_sensitivity_avg_abs', SensitivityScore(True, True)),
    ('concept_sensitivity_sum_abs', SensitivityScore(True, False)),
]

LENGHT_FEATURES_LIST_WORDS = [
    ('count_words', CountWords()),
]

LENGHT_FEATURES_LIST = [
    ('count_words', CountWords()),
    ('count_words_document', DocumentSize()),
]

LEXICON_FEATURES_LIST = [
    ('lexicon_subjective', LexiconSubjective()),
    ('lexicon_positive', LexiconSubjective()),
    ('lexicon_negative', LexiconSubjective()),
    ('lexicon_quotation_exclamation', LexiconSubjective()),
    ('lexicon_subjective_prop', LexiconSubjective(True)),
    ('lexicon_positive_prop', LexiconSubjective(True)),
    ('lexicon_negative_prop', LexiconSubjective(True)),
    ('lexicon_quotation_exclamation_prop', LexiconSubjective(True)),
]

POSITIONAL_FEATURES_LIST = [
    ('sentence_position', SentencePosition()),
    ('sentence_relative_position', SentencePosition(True))
]

SUBJECTIVITY_FEATURES_LIST = [
    ('count_named_entities', CountNE()),
    ('count_number_date_time', CountNumberDateTime()),
    ('future_tense', FutureTense()),
]

SYNTACTIC_RULES_FEATURES_LIST = [
    ('rule1', SyntacticRule1()),
    ('rule2', SyntacticRule2()),
    ('rule3', SyntacticRule3()),
    ('rule4', SyntacticRule4()),
    ('rule5', SyntacticRule5()),
]

TWITTER_FEATURES_LIST = [
    ('count_capitalized', CountCapitalized()),
    ('count_dictionary_words', CountDictionaryWords()),
    ('count_elongated', CountElongated()),
    ('count_expressions', CountExpressions()),
    ('count_mentions', CountMentions()),
    ('count_url', CountURL()),
    ('emoji_polarity_score', EmojiPolarityScore()),
    ('emoticon_polarity_score', EmoticonPolarityScore()),
    ('negation', Negation()),
    ('proportion_capitalized', ProportionCapitalized()),
]

RAW_TEXT_FEATURES = [
    ('count_words', CountWords()),
    ('count_capitalized', CountCapitalized()),
    ('count_elongated', CountElongated()),
    ('count_mentions', CountMentions()),
    ('count_url', CountURL()),
    ('proportion_capitalized', ProportionCapitalized()),
]

ALL_FEATURES_POSITIONAL = CONCEPT_FEATURES_LIST + LENGHT_FEATURES_LIST + LEXICON_FEATURES_LIST \
                          + POS_FEATURES_LIST + POSITIONAL_FEATURES_LIST + SUBJECTIVITY_FEATURES_LIST \
                          + SYNTACTIC_RULES_FEATURES_LIST

ALL_FEATURES_TWITTER = CONCEPT_FEATURES_LIST + LENGHT_FEATURES_LIST + LEXICON_FEATURES_LIST \
                          + POS_FEATURES_LIST + SUBJECTIVITY_FEATURES_LIST + SYNTACTIC_RULES_FEATURES_LIST\
                          + TWITTER_FEATURES_LIST
ALL_FEATURES_CONCEPT_INTEGER = CONCEPT_FEATURES_LIST + LENGHT_FEATURES_LIST + LEXICON_FEATURES_LIST \
                + POS_FEATURES_LIST + SUBJECTIVITY_FEATURES_LIST + SYNTACTIC_RULES_FEATURES_LIST

ALL_FEATURES = CONCEPT_FEATURES_LIST_ABS + LENGHT_FEATURES_LIST_WORDS + LEXICON_FEATURES_LIST + POS_FEATURES_LIST\
               + SUBJECTIVITY_FEATURES_LIST + SYNTACTIC_RULES_FEATURES_LIST + TWITTER_FEATURES_LIST
