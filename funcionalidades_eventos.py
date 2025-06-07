import random
from datetime import datetime, timedelta
from dados_eventos import *

data_inicio = "2020-01-01"
data_fim = "2025-12-31"

def gerar_data_aleatoria(inicio, fim):
    inicio_dt = datetime.strptime(inicio, "%d-%m-%Y")
    fim_dt = datetime.strptime(fim, "%d-%m-%Y")
    diferenca = fim_dt - inicio_dt
    dias_aleatorios = random.randint(0, diferenca.days)
    return inicio_dt + timedelta(days=dias_aleatorios)

for evento in eventos:
    data = gerar_data_aleatoria(data_inicio, data_fim)
    evento["data_realizacao"] = data.strftime("%d-%m-%Y")