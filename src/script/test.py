from src.extractor.twitter.count_dictionary_words import CountDictionaryWords
from src.utils.spacy_preprocessor import SpacyPreprocessor
from src.extractor.twitter.emoji_polarity_score import EmojiPolarityScore

sentences = ['O abacaxi é doce', 'A casa é amarela demais', "A sobremesa é boa"]
spacy_sentences = SpacyPreprocessor().transform(sentences)

emojis = "☷ 😊 🥺 😍 😘 😚 😜 😂 😝 😳 😁 😣 😢 😭"
print(emojis)
print(emojis.encode('unicode-escape'))

# extractor = EmojiPolarityScore()
# print(extractor.transform(spacy_sentences))
