from src.extractor.lenght.document_size import DocumentSize
from src.utils import SpacyPreprocessor
from src.extractor.lenght.count_words import CountWords
from src.extractor.positional import SentencePosition
from src.utils.spacy_sent_tokenizer import SpacySentenceTokenizer
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
data = pd.read_csv("/home/miguel/PycharmProjects/textual-features/res/datasets/computerbr_dataset.tsv", sep='\t')
sentences = data['sentence'].to_list()
targets = data['subjectivity'].to_list()

for i in range(len(sentences[:10])):
    sbj = targets[i]
    print('--')
    for sent in SpacySentenceTokenizer().transform(sentences[i]):
        print(sbj, sent)

# with open('/home/miguel/PycharmProjects/textual-features/sentences_computerbr.txt', 'w+') as f:
#     f.write('\n'.join(tokenized))
