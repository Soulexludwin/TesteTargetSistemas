encoding = 'utf-8'
sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
Ou = 19849.53

Faturamento = sp + rj + mg + es + Ou

print("Faturamento")
print(Faturamento)

porcentagem = Faturamento / 100

Porcentagem_sp = round((sp / porcentagem),2)
Porcentagem_rj = round((rj / porcentagem),2)
Porcentagem_mg = round((mg / porcentagem),2)
Porcentagem_es = round((es / porcentagem),2)
Porcentagem_Ou = round((Ou / porcentagem),2)
print("Porcentagem de faturamento de cada regiao") 

print("Sao paulo:")
print(Porcentagem_sp)
print("Rio de janeiro:")
print(Porcentagem_rj)
print("Minas gerais:")
print(Porcentagem_mg)
print("Espirito Santo:")
print(Porcentagem_es)
print("Outros:")
print(Porcentagem_Ou)
input("Pressione ENTER para sair...")