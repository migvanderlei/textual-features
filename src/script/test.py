from src.extractor.twitter.count_dictionary_words import CountDictionaryWords
from src.utils.spacy_preprocessor import SpacyPreprocessor

sentences = ['O abacaxi é doce', 'A casa é amarela demais', "A sobremesa é boa"]
spacy_sentences = SpacyPreprocessor().transform(sentences)

extractor = CountDictionaryWords()
print(extractor.transform(spacy_sentences))
