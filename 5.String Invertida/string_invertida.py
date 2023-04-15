#recebe a string
string = input("Digite uma palavra: ")

#string vazia pra armazenar a string invertida
string_invertida = ""

#contagem das letras, de traz para frente e criar a nova string adcionando cada letra
for x in range(len(string)-1, -1, -1):
    string_invertida += string[x]

print("A string invertida é:", string_invertida)