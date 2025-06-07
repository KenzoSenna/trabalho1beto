import random
from dados_eventos import *
from dados_participantes import *

temas_disponiveis = list({evento["tema_central"] for evento in eventos})

for participante in dados_p:
    quantidade_de_temas = random.randint(1, min(3, len(temas_disponiveis)))
    participante["preferencias_tematicas"] = random.sample(temas_disponiveis, quantidade_de_temas)

for p in dados_p:
    print(p)