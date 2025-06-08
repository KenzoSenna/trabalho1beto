import random
from datetime import datetime, timedelta
from dados_eventos import *
from dados_participantes import *

data_inicio = "01-01-2020"
data_fim = "31-12-2025"

def gerar_data_aleatoria(inicio, fim):
    inicio_dt = datetime.strptime(inicio, "%d-%m-%Y")
    fim_dt = datetime.strptime(fim, "%d-%m-%Y")
    diferenca = fim_dt - inicio_dt
    dias_aleatorios = random.randint(0, diferenca.days)
    return inicio_dt + timedelta(days=dias_aleatorios)

for evento in eventos:
    data = gerar_data_aleatoria(data_inicio, data_fim)
    evento["data_realizacao"] = data.strftime("%d-%m-%Y")

def distribuir_participantes_aleatoriamente(eventos, participantes, min_por_evento=1, max_por_evento=3):
    ids_participantes = [p["id"] for p in participantes]

    for evento in eventos:
        quantidade = random.randint(min_por_evento, min(max_por_evento, len(ids_participantes)))
        evento["participantes"] = random.sample(ids_participantes, quantidade)

distribuir_participantes_aleatoriamente(eventos, participantes)

print("Eventos com participantes distribuídos aleatoriamente:")
for evento in eventos:
    print(f"Evento: {evento['nome']}, Data: {evento['data_realizacao']}, Participantes: {evento['participantes']}")
print("\nParticipantes:")
for participante in participantes:
    print(f"ID: {participante['id']}, Nome: {participante['nome']}, Email: {participante['email']}, Preferências: {participante['preferencias_tematicas']}")
