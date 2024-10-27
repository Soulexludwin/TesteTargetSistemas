import json
encoding = 'utf-8'
with open('dados.json', 'r') as file:

    dados = json.load(file)

Fatura = [item['valor'] for item in dados if item['valor'] > 0]
#Round arredondado para 2 casas decimais, melhora a aparencia.
MenorFaturamento = round(min(Fatura), 2)
MaiorFaturamento = round(max(Fatura), 2)

MediaMensal = sum(Fatura) / len(Fatura)

DiasMediaAlta = len([valor for valor in Fatura if valor > MediaMensal])

print("Menor Faturamento do mês:", MenorFaturamento)
print("Maior faturamento do mês:", MaiorFaturamento)
print("Quantas vezes o dia teve um faturamento acima da média mensal:", DiasMediaAlta)