print(""" \nOlá, esse programa vai pedir um número e mostrar sua Unidade, Dezena, Centena e Milhar!
Para usar esse programa, por favor digite apenas números! """)

num = int(input("\nDigite um número de 0 a 9999: "))
n = str(num)

# se só tiver um número:
if n == n[0:1]:
    print(f"\nUnidade: {n[0]}\nDezena: \nCentena: \nMilhar: ")

# se tiver dois números:
elif n == n[0:2]:
    print(f"\nUnidade: {n[1]}\nDezena: {n[0]}\nCentena: \nMilhar: ")

# se tiver três números:
elif n == n[0:3]:
    print(f"\nUnidade: {n[2]}\nDezena: {n[1]}\nCentena: {n[0]}\nMilhar: ")

# se tiver quatro números:
elif n == n[0:4]:
    print(f"\nUnidade: {n[3]}\nDezena: {n[2]}\nCentena: {n[1]}\nMilhar: {n[0]}")

else:
    print("\nTECLA INVÁLIDA")
