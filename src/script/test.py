from src.extractor.twitter.count_dictionary_words import CountDictionaryWords
from src.utils.spacy_preprocessor import SpacyPreprocessor
from src.extractor.twitter.emoji_polarity_score import EmojiPolarityScore

sentences = ["☷ 😊 🥺 😍", "😘 😚 😜 😂 😝", "😳 😁 😣 😢 😭"]
# sentences = [":)", "lalalal :) :) ;)", ":("]
spacy_sentences = SpacyPreprocessor().transform(sentences)

# for sentence in sentences:
#     for doc in sentence:
#         print(doc)
#         print(doc.encode('utf-8').hex())

extractor = EmojiPolarityScore()
print(extractor.transform(spacy_sentences))
