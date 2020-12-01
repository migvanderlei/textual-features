echo "Instalando as libs do Python"
pip3 install -r ./requirements.txt

echo "Baixando o modelo do spaCy"
python3 -m spacy download pt_core_news_lg

