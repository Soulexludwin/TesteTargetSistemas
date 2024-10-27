encoding = 'utf-8'
def fibbonacci(n):
    seq_fibbonacci = [0, 1]

    while True:
        next_fib = seq_fibbonacci[-1] + seq_fibbonacci[-2]
        if next_fib > n:
            #Separação
            break
        seq_fibbonacci.append(next_fib)

    if n in seq_fibbonacci:
        return f"{n} pertence à sequência de Fibonacci."
    else:
        return f"{n} não pertence à sequência de Fibonacci."

numero = int(input("Insira um número: "))
resultado = fibbonacci(numero)
print("Resultados:")
print(resultado)
input("Aperte enter para sair..")