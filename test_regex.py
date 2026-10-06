import re

def norm(text: str) -> str:
    text = re.sub(r'\([^\]+)\', r'\1', text)
    text = re.sub(r'[\u2018\u2019\u0060\u00B4]', \"'\", text)
    text = re.sub(r'[\u201C\u201D]', '\"', text)
    text = re.sub(r'[\u2013\u2014\u2012\u2015]', '-', text)
    return text

print(norm('caixa-d\gua e \codigo\ e “aspas” e – travessao'))
