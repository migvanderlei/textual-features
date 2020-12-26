from src.extractor.lenght.document_size import DocumentSize
from src.utils import SpacyPreprocessor
from src.extractor.lenght.count_words import CountWords
from src.extractor.pos import CountAdj
from src.extractor.concept import AptitudeScore
import pandas as pd
"""
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
"""
data = pd.read_csv("/home/miguel/PycharmProjects/textual-features/res/datasets/tripadvisor_dataset.tsv", sep='\t')
sentences = data['sentence'].to_list()
spacy_sentences = SpacyPreprocessor().transform(sentences)

extractor1 = DocumentSize()
extractor2 = CountWords()

adj_extractor = CountAdj()
aptitude_extractor = AptitudeScore(True, True)

features = aptitude_extractor.transform(spacy_sentences)

# print(features)
print(features.shape)
features = adj_extractor.transform(sentences)
