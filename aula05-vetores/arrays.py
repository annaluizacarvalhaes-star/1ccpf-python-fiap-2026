lista_frutas = ["Uva", "Banana", "Melancia"]
print(lista_frutas[1])

lista_frutas.append("Pitaya") # adiciona ao final da lista
print(lista_frutas)

for i in range(len(lista_frutas)): # Len = calcula o tamanho da lista
    print(lista_frutas[i])
    print()

for fruta in lista_frutas:
    print(fruta)
