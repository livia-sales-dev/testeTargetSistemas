num = int(input('Digite um número:')) #entrada do numero

valor1 = 0
valor2 = 1
valor3 = []

while valor2 < num: #a cada laço, faz a soma e o numero anterior ocupa a próxima posição, até chegar no numero digitado pelo usuario
    valor3 = valor1 + valor2
    valor1 = valor2
    valor2 = valor3

if valor3 == num : #se o resultado da soma for igual ao numero digitado, então ele pertence à sequencia
        print(f'O número {num} pertence à sequência de Fibonacci!!')
else:
        print(f'O número {num} não pertence à sequência de Fibonacci!!')