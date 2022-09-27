#Desfios da aula

#Programa que leia um número e informe o sucessor e o antecessor.
# n = int(input("Digite um número: "))
#
# nup = n + 1
# ndown = n - 1
#
# print("Seu número: {}, \n o antecessor do número digitado é {}, \n o sucessor do número digitado é {}".format(n, ndown, nup))


#Algoritmo que leia um número e informe seu dobro, triplo e sua raiz quadrada.

# n1 = int(input("Digite um número: "))
#
# dobro = n1 * 2
# triplo = n1 * 3
# rquadrada = (n1 ** (0.5))
#
# print(f"Seu número é {n1}, este é o dobro {dobro}, este o trípulo {triplo} e por fim, a raiz quadrada {rquadrada:,.2f}.")

#Programa que leia as duas notas de um aluno e calcule sua média

# nota1 = float(input("Digite a primeira nota: "))
# nota2 = float(input("Digite a segunda nota: "))
#
# media = (nota1 + nota2) / 2
#
# print(f"A primeira nota foi {nota1:.2f}, a segunda nota foi {nota2:.2f} e a média é {media:.2f}.")

#Programa que leia um valor em metros e a exiba convertida em centímetros e milímetros

# metros = float(input("Informe o metro: "))
#
# centimetros = (metros * 100) / 1
#
# milimetros = (metros * 1000) / 1
#
# print(f"{metros} metros são {centimetros} centímetros e {milimetros} milímetros!")

#Programa que leia um número inteiro e mostre sua tabuada

# n = int(input("Digite um número: "))
# #
# # # n1 = n * 1
# # # n2 = n * 2
# # # n3 = n * 3
# # # n4 = n * 4
# # # n5 = n * 5
# # # n6 = n * 6
# # # n7 = n * 7
# # # n8 = n * 8
# # # n9 = n * 9
# # # n10 = n * 10
#
# print("-" * 20)
# print("-"* 5, "Tabuada", "-" * 6)
# print("-" * 20)
#
# for c in range(11):
#     n1 = n * c
#     print(f"{n} x {c} = {n1}")


#Programa que leia quanto o usuário tem na carteira e mostre quantos dólares ela pode comprar

# carteira = float(input("Quanto você tem? "))
#
# dolar = carteira * 3.27
#
# print(f"Você pode comprar {dolar} dólares!")


#Faça um programa que leia a largura e a altura de uma parede em metros e calcule a área e a quantidade de tinta necessária para pintá-la.
#Sabendo que cada litro de tinta pinta uma área de 2m²

# altura = float(input("Digite a altura da parede: "))
# largura = float(input("Digite a largura da parede: "))
#
# area = altura * largura
#
# litros = float(area / 2)
#
# print(f"Sua parede tem a dimensão de {altura}x{largura} e sua área é de {area}m²."
#       f"Serão necessários {litros:.3f} litros de tinta para pintá-la.")

#Algoritimo que leia preço de um produto e mostre seu novo preço, com 5% de desconto

# preco = float(input("Digite o preço do produto para aplicar o desconto, R$ "))
#
# desconto = preco * 0.05
#
# total = preco - desconto
#
# print(f"Valor total com desconto: {total:.2f}")

#Algoritmo que leia o salário de um funcionário e mostre o novo salário com 15% de aumento

# salario = float(input("Digite seu salário R$ "))
#
# aumento = salario * 0.15
#
# total = salario + aumento
#
# print(f"Parabéns você teve um aumento de 15%, este é o seu novo salário R$ {total:.2f}")
#
#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e
# a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input("Informe a quantidade de dias: "))
km = float(input("Informe quantos quilômetoros percorridos: "))

valorT = float((60 * dias) + (0.15 * km))

print(f"Pelos {km}Km percorridos e pelo(s) {dias} alugado(s), seu valor ficou em R${valorT}")
