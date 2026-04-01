#EXERCÍCIO 1
mp3 = print(input("Cole o link da música em mp3 desejada: "))
print(f'Tocando {mp3}')


# EXERCÍCIO 2
num = int(input("Digite um número: "))

if num % 2 == 0:
    print("Esse número é par")
else:
    print("Esse número é impar")


#EXERCÍCIO 3
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

if num1 > num2:
    print(f'{num1} é maior que {num2}')
elif num1 < num2:
    print(f'{num2} é maior que {num1}')
else:
    print("Os valores são iguais")

#EXERCÍCIO 4
nota1 = int(input('Primeira nota: '))
nota2 = int(input('Segunda nota: '))
nota3 = int(input('Terceira nota: '))
nota4 = int(input('Quarta nota: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 7:
    print("Aprovado")
elif 5 <= media <7:
    print("Recuperação")
else:
    print("Reprovado")


#EXERCÍCIO 5
A = int(input("Digite o primeiro numero: "))
B = int(input("Digite o segundo numero: "))

if A > B:
    conta1 = A % B
    if conta1 == 0:
        print("São multiplos")
    else:
        print(" Não são multiplos")
elif B > A:
    conta2 = B % A
    if conta2 == 0:
        print("São multiplos")
    else:
        print("Não são múltiplos")

else:
    print("São Multiplos")

#EXERCÍCIO 6
num1 = int(input('digite um numero: '))
num2 = int(input('digite outro numero: '))
caracter =  input('digite uma caracter: ')

soma = num1 + num2
mult = num1 * num2
divi = num1 / num2
sub = num1 - num2

if caracter == '+':
    print(soma)
elif caracter == '-':
    print(sub)
elif caracter == '*':
    print(mult)
else:
    print(divi)


#EXERCÍCIO 7
nascimento = int(input("Digite o ano de nascimento: "))

idade = 2026 - int(nascimento)

if idade >= 18:
    print("Pode votar")
elif 16<= idade <18 or idade>=70:
    print("O voto é opcional")
else:
    print("Proibido votar")


#EXERCÍCIO 8
salario = float(input("Digite o seu salário: "))

if salario <= 280:
    print(salario)
    print("Aumento de 20%")
    print(f"Valor aumentado: {0.20 * salario}")
    print(f'Valor final: {salario + 0.20 * salario}')
elif 280<salario<=700:
    print(salario)
    print("Aumento de 15%")
    print(f"Valor aumentado: {0.15 * salario}")
    print(f'Valor final: {salario + 0.15 * salario}')

elif 700 < salario <= 1500:
    print(salario)
    print("Aumento de 10%")
    print(f"Valor aumentado: {0.10 * salario}")
    print(f'Valor final: {salario + 0.10 * salario}')

else:
    print(salario)
    print("Aumento de 5%")
    print(f"Valor aumentado: {0.05 * salario}")
    print(f'Valor final: {salario + 0.05 * salario}')


#EXERCÍCIO 9
estado = int(input("Digite o codigo do estado (de 1 a 5): "))
peso = float(input("Digite o peso da carga em toneladas: "))
carga = float(input("Digite o código da carga (de 10 a 40): "))

peso_kg = peso * 1000
print(peso_kg)

if 20<= carga <=20:
    preco_kg = 100
    print(f'O preço da carga será: {preco_kg * peso_kg: .2f}')
elif 20< carga <=30:
    preco_kg = 250
    print(f'O preço da carga é igual: {preco_kg * peso_kg: .2f}')
else:
    preco_kg = 340
    print(f'O preço da carga é igual: {preco_kg * peso_kg: .2f}')

if estado == 1:
    imposto = 0.35
    print(f"Imposto igual a {imposto * 100} %")
elif estado == 2:
    imposto = 0.25
    print(f"Imposto igual a {imposto * 100} %")
elif estado == 3:
    imposto = 0.15
    print(f"Imposto igual a {imposto * 100} %")
elif estado == 4:
    imposto = 0.05
    print(f"Imposto igual a {imposto * 100} %")
else:
    imposto = 0
    print("Sem imposto")

print( (preco_kg * peso_kg) + ((preco_kg * peso_kg)*imposto))


#EXERCÍCIO 10
A = int(input("Digite o primeiro numero: "))
B = int(input("Digite o segundo numero: "))
C = int(input("Digite o terceiro numero: "))

if A>= (B+C):
    print("não representa um triângulo")
elif A**0.5 == (B**0.5) + (C**0.5):
    print("Triângulo retângulo")
elif A**0.5 > (B**0.5) + (C**0.5):
    print("Triângulo obtusangulo")
elif A**0.5 < (B**0.5) + (C**0.5):
    print("Triângulo acutangulo")
elif A==B and B==C:
    print("Triângulo retangulo")
else:
    print("Triângulo isóceles")