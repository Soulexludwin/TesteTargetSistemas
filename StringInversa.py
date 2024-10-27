
encoding = 'utf-8'
def reverter_string(s):
    string_inversa = ""
    for i in range(len(s) - 1, -1, -1):
        string_inversa += s[i]

    return string_inversa

string = input("escreva uma string para inverter: ")

resultado = reverter_string(string)

print("String invertida:")
print(resultado)
input("aperte enter para sair.")
