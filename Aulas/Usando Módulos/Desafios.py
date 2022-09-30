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

# numero = int(input('Informe um número: '))
# u = numero // 1 % 10
# d = numero // 10 % 10
# c = numero // 100 % 10
# m = numero // 1000 % 10
#
# print('Unidade: {}'.format(u))
# print('Dezena: {}'.format(d))
# print('Centena: {}'.format(c))
# print('Milhar: {}'.format(m))

# Ex:
# Digite um número: 1834
#
# Unidade: 4
# Dezena: 3
# Centena: 8
# Milhar: 1

#___________________________________________________________________________________________________#

# Crie um sistema que leia o nome de uma cidade e diga se ela começa ou não com a palavra SANTO.

# cid = str(input('Informe a cidade: ')).strip().upper()
# print('Sua cidade inicia por SANTO? {}'.format(cid[:5] == 'SANTO'))

#___________________________________________________________________________________________________#

#Crie um programa que leia um nome e diga se a pessoa tem SILVA no nome

# nome = str(input('Informe seu nome: ')).strip().upper()
# print('Você tem silva no nome? {}'.format('SILVA' in nome))
#___________________________________________________________________________________________________#

# Crie um programa que leia uma frase e mostre:

# frase = str(input('Digite uma frase: ')).upper().strip()
# Quantas vezes aparece a letra A;
# print('A letra A aparece {} vezes.'.format(frase.count('A')))
# Em que posição ela aparece a primeira vez;
# print('A letra A aparece pela primeira na {}ª posição.'.format(frase.find('A') + 1))
# Em que posição ela aparece a última vez;
# print('A letra A aparece pela última vez na {}ª posição.'.format(frase.rfind('A') +1))
#___________________________________________________________________________________________________#

#Faça um programa que leia o nome de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente

# nome = str(input('Informe seu nome: ')).strip().split()
# print('Primeiro nome {}'.format(nome[0]))
# print('Último nome: {}'.format(nome[len(nome) -1]))
# Ex: Ana Maria de Souza
# Primeiro nome: Ana
# Último nome: Souza

#___________________________________________________________________________________________________#

#Escreva um programa que faça o computador 'pensar' entre um número inteiro de 0 a 5 e peça para o usuário
#descobrir qual número foi escolhido pelo computador
# lista_numero = [0, 1, 2, 3, 4, 5]
# pc = random.choice(lista_numero)
#
# usuario_escolha = int(input('Advinhe o número que escolhi: '))
#
# if pc == usuario_escolha:
#     print('Parabêns você acertou!!!')
# else:
#     print('Infelizmente você errou!!!')
#OBS. O programa deverá escrever na tela se o usuário venceu ou perdeu!


#___________________________________________________________________________________________________#

#Escreva um programa que leia a velocidade de um carro, se ele ultrapassar 80km/h mostre uma mensagem que ele
#foi multado. A multa custa R$7,00 por cada km acima do limite.
# velocidade = float(input("Digite a velocidade do seu carro:"))
# if velocidade > 80:
#     multa = (velocidade - 80) * 7
#     print(f"Você foi multado em R$ {multa:7.2f}!")
# if velocidade <= 80:
#     print("Sua velocidade está ok, boa viagem!")
#___________________________________________________________________________________________________#

#Crie um programa que leia um número inteiro qualquer e mostre na tela se ele é par ou ímpar

# n = int(input('Insira um número: '))
# if n % 2 == 0:
#     print(f'{n} é par')
# else:
#     print(f'{n} é ímpar')
#___________________________________________________________________________________________________#

#Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando
#R$0.50 por km para viagens de até 200km e R$0.45 para viagens mais longes.

# km = int(input('Informe a distância em KM: '))
#
# if km <= 200:
#     valor = km * 0.50
#     print(f'O valor da sua viagem ficou em R${valor:.2f}')
# else:
#     valor = km * 0.45
#     print(f'O valor da sua viagem ficou em R${valor:.2f}')
#___________________________________________________________________________________________________#


#Faça um programa que leie um ano qualquer e informe se é bissexto.


# ano = int(input('Insira o ano: '))
#
# if ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0:
#     print(f'{ano}, é Bissexto!')
# elif ano % 4 == 0 and ano % 100 != 0:
#     print(f'{ano}, é Bissexto!')
# else:
#     print(f'{ano}, não é Bissexto!')


#___________________________________________________________________________________________________#


#Faça um programa que leia qualquer número e informe qual o maior e qual o menor.

# n1 = int(input('informe o número: '))
# n2 = int(input('Informe outro número: '))
#
# if n1 > n2:
#     print(f'{n1} é maior que {n2}')
# else:
#     print(f'{n2} é maior que {n1}')

#___________________________________________________________________________________________________#

#Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento.

# sal = float(input('Fala o teu salário para o papai dar um aumento: '))

#Para inferiores ou iguais o aumento é de 15%.
# if sal <= 1.250:
#     sal = sal + (sal * 0.15)
#     print(f'{sal} este é o seu novo salário com aumento de 15%')
#Para salários superiores a R$1.250,00 calcule um aumento de 10%.
# elif sal > 1.250:
#     sal = sal + (sal * 0.1)
#     print(f'{sal} este é o seu novo salário com aumento de 10%')


#___________________________________________________________________________________________________#


#Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuário se ela podem ou não formar um triãngulo.

reta1 = float(input('Informe o comprimento da 1ª reta: '))
reta2 = float(input('Informe o comprimento da 2ª reta: '))
reta3 = float(input('Informe o comprimento da 3ª reta: '))

