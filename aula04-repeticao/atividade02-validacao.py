def verificar_nota(Nota):
    while Nota < 0 or Nota > 10:
        print("A nota deve estar entre 0 e 10")
        Nota = float(input("Digite a nota novamente: "))
    return Nota  #fora do while, pq se estiver dentro com apenas 1 erro ele sai da função


NotaA = float(input("Digite a 1 nota: "))
NotaA = verificar_nota(NotaA)

NotaB = float(input("Digite a 2 nota: "))
NotaB = verificar_nota(NotaB)

# Enquanto os dois códigos forem igyuais, pode-se criar uma função
media = (NotaA + NotaB)/2
print(media)