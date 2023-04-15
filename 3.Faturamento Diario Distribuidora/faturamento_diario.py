import json

with open("dados.json", encoding='utf-8') as dados_json:
    dados = json.load(dados_json)

valores = []
media = []

for dia in dados:
    valor = dia['valor']   #menor e maior valores
    valores.append(valor)
    menor_valor = min(valores)
    maior_valor = max(valores)
    if dia['valor'] != 0:   #media de valores, excluindo dias de valores = 0
        media_valores = dia['valor']
        media.append(media_valores)
        media_1 = sum(media) / len(media)
    if dia['valor'] > media_1:  #dias com faturamento abaixo da media mensal
        maior = str(dia['valor'])
        quant_dias = len(maior)



print(f'O menor valor de faturamento ocorrido foi:, {menor_valor}')
print(f'O maior valor de faturamento ocorrido foi:, {maior_valor}')
print(f'A quantidade de dias com faturamento diário superior à média mensal é: {quant_dias}')
