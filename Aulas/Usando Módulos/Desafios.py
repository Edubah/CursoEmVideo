import math
import random
import time
#from pygame import mixer

#___________________________________________________________________________________________________#

# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela sua porção inteira
# Exemplo: Digite o número: 6.127 / O número 6.127, tem a parte inteira 6

# real = float(input("Digite um número: "))
# nInteiro = int(real)
#
# print(f'O número {real:.3f}, tem sua parte inteira igual a {nInteiro}.')

# real = float(input("Digite um valor: "))
# print(f'O valor informado {real} tem a sua porção inteira igual a {math.trunc(real)}')

#___________________________________________________________________________________________________#

# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um Triângulo retângulo
# calcule e mostre o comprimento da hipotenusa.

# catetoO = float(input("Informe o Cateto Oposto: "))
# catetoA = float(input("Informe o Cateto Adjacente: "))$
#
# compHipotenusa = pow(catetoO,2) + pow(catetoA,2)
# res = compHipotenusa ** 0.5
# print(f'O comprimento da Hipotenusa é igual a {res}')

# co = float(input("Informe o Cateto Oposto: "))
# ca = float(input("Informe o Cateto Adjacente: "))
# h1 = math.hypot(co, ca)
# h1 = (co ** 2 + ca ** 2) ** 0.5
# print(f'A hipotenusa vai medir {h1:.2f}')

#___________________________________________________________________________________________________#

# Faça um programa que leia o ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente deste ângulo.

# angulo = float(input("Insira o valor do ângulo: "))
# #
# #
# seno = math.sin(math.radians(angulo))
# print(f'O seno de {angulo:.0f}º é: {seno:.2f}º.')
# cosseno = math.cos(math.radians(angulo))
# print(f'O seno de {angulo:.0f}º é: {cosseno:.2f}º.')
# tangente = math.tan(math.radians(angulo))
# print(f'O seno de {angulo:.0f}º é: {tangente:.2f}º.')


# Eixo vertical = seno/Eixo horizontal = cosseno

#___________________________________________________________________________________________________#

# Um professor quer sortear um de seus 4 alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo o nome do escolhido
# listAluno = []
# for c in range(4):
#     aluno = input("Digite o nome do aluno: ")
#     listAluno.append(aluno)
# print(random.choice(listAluno))

#___________________________________________________________________________________________________#

# O mesmo professor quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que
# Leia o nome dos 4 alunos e mostrem a ordem sorteada.

# a1 = input("Digite o primeiro aluno: ")
# a2 = input("Digite o segundo aluno: ")
# a3 = input("Digite o terceiro aluno: ")
# a4 = input("Digite o quarto aluno: ")
# lista = [a1, a2, a3, a4]
# random.shuffle(lista)
# print(f'A ordem de apresentação será \n{lista}')

# listAluno = []
# for c in range(4):
#     aluno = input("Digite o nome do aluno: ")
#     listAluno.append(aluno)
#     listAluno.sort()
#
# print(listAluno)

#___________________________________________________________________________________________________#

# Faça um programa que abra e reproduza o áudio de um arquivo MP3.

# mixer.init()
# musica = mixer.Sound('FatherStretchMyHandsPt.1.mp3')
# musica.play()
# musica.set_volume(0.5)
# time.sleep(150)


#___________________________________________________________________________________________________#
# Crie um programa que leia o nome completo de uma pessoa e mostre:

# nome = input('Digite seu nome: ')

# O nome com todas as letras maiúsculas;
# print(nome.upper())

# O nome com todas as letras minúsculas;
# print(nome.lower())

# Quantas letras ao todos sem considerar os espaços;
# res = 0
# for c in nome.split():
#     res += len(c)
#
# print("Quantidade de letras em seu nome: ",res)

# Quantas letras tem o primeiro nome;
# nome1 = nome.split()
# res = len(nome1[0])
# print(f'Quantidade de letras no primeiro nome: {nome1} = ',res)
#___________________________________________________________________________________________________#

# Faça um programa que leia números de 0 a 9999 e mostre na tela cada um dos dígitos separados

# Ex:
# Digite um número: 1834
#
# Unidade: 4
# Dezena: 3
# Centena: 8
# Milhar: 1

#___________________________________________________________________________________________________#

# Crie um sistema que leia o nome de uma cidade e diga se ela começa ou não com a palavra SANTO.

#___________________________________________________________________________________________________#

#Crie um programa que leia um nome e diga se a pessoa tem SILVA no nome

#___________________________________________________________________________________________________#

# Crie um programa que leia uma frase e mostre:

# Quantas vezes aparece a letra A;
#
# Em que posição ela aparece a primeira vez;
#
# Em que posição ela aparece a última vez;

#___________________________________________________________________________________________________#

#Faça um program que leia o nome de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente

# Ex: Ana Maria de Souza
# Primeiro nome: Ana
# Último nome: Souza