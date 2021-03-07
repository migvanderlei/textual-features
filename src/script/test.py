import pandas as pd
import spacy

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
data = pd.read_csv("/home/miguel/Workspace/textual-features/res/datasets/raw/computerbr_dataset.tsv", sep='\t')
sentences = data['sentence'].to_list()
nlp = spacy.load('pt_core_news_sm')

for sentence in sentences[:5]:
	print(sentence)
	parsed = nlp(sentence) 
	print(nlp(sentence).pos_)