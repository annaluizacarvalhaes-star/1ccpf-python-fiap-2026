from sqlalchemy.sql.operators import truediv
from statsmodels.discrete.discrete_margins import margeff_cov_with_se

num1 = 4
num2 = 2

print(type(num1), type(num2))

resultado = num1 / num2
print(resultado, type(resultado))

#OPERADORES DE ATRIBUIÇÃO
num = 15
print() #pular linha
print(num)

num -= 2
print(num)

#OPERADORES RELACIONAIS
print()
print (6 < 2)

idade = 28
print(idade == 28)

logado = True
print(logado, type(logado))

maior_idade = idade >= 18
print(maior_idade, type(maior_idade))

#STRINGS
nome1 = "marcos"
nome2 = "Marcos"

print(nome1.upper() == nome2.upper()) #Desconsidera diferença entre letra maiuscula e minuscula
