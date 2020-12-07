from src.extractor.positional.sentence_position import SentencePosition
from src.utils import SpacyPreprocessor
from src.extractor.lexicon.count_words import CountWords

docs = ["Hamburgueria artesanal com tempero diferenciado, de primeira qualidade, fora o atendimento no qual "
        "diferencia por serem bilíngues,. Recomendo quem quer saciar a fome..",
        "Excelente peixe, para quem esta localizado no Distrito Industrial, excelente pedida para almoço. dica "
        "Matrinxã recheada.",
        "Serve lanches e cerveja gelada, tem mesinhas fora do estabelecimento, funciona em uma casa antiga o que "
        "faz parte do seu charme. Recomendo. ",
        "Bom para experimentar releituras de pratos da comida regional. Adorei TUDO que experimentei, "
        "especialmente, o pesto de Jambu. Fora isso, o atendimento é MUITO bom e o ambiente/vista são lindos."]

sentences = ["Hamburgueria artesanal com tempero diferenciado, de primeira qualidade, fora o atendimento no qual "
             "diferencia por serem bilíngues,",
             ". Recomendo quem quer saciar a fome..",
             "Excelente peixe, para quem esta localizado no Distrito Industrial, excelente pedida para almoço.",
             "dica Matrinxã recheada.",
             "Serve lanches e cerveja gelada, tem mesinhas fora do estabelecimento, funciona em uma casa antiga o que "
             "faz parte do seu charme.",
             "Recomendo. ",
             "Bom para experimentar releituras de pratos da comida regional.",
             "Adorei TUDO que experimentei especialmente, o pesto de Jambu. ",
             "Fora isso, o atendimento é MUITO bom e o ambiente/vista são lindos."]

spacy_sentences = SpacyPreprocessor().transform(sentences)

extractor1 = SentencePosition(relative=True)
extractor2 = CountWords()

feat1 = extractor1.transform(docs)
feat2 = extractor2.transform(sentences)

print(feat1)
print(feat2)
