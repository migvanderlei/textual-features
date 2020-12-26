from src.extractor.pos import *

POS_FEATURES_LIST = [
    ('adj', CountAdj()),
    ('adp', CountAdp()),
    ('adv', CountAdj()),
    ('aux', CountAux()),
    ('cconj', CountCconj()),
    ('det', CountDet()),
    ('intj', CountIntj()),
    ('noun', CountNoun()),
    ('num', CountNum()),
    ('part', CountPart()),
    ('pron', CountPron()),
    ('propn', CountPropn()),
    ('punct', CountPunct()),
    ('sconj', CountSconj()),
    ('sym', CountSym()),
    ('verb', CountVerb()),
    ('x', CountX()),
]
