#valor do faturamento mensal em cada estado:
faturamento_mensal = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}
#faturamento mensal total:
soma = sum(faturamento_mensal.values())

#calculo de porcentagem de faturamento em cada estado e resultado:
print("O percentual de cada estado em relação ao faturamento mensal total da distribuidora é: ")
for estado, valor in faturamento_mensal.items():
    porcentagem = (valor / soma) * 100
    print(f"{estado}: {porcentagem:.2f}%")
