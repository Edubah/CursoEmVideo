#Fatiamento - Conseguir pegar pedaços de uma string

frase = "Curso em Vídeos Python"

print(frase[9]) #Pegara a letra que está na 9ª posição

print(frase[9:13]) #Pegara da 9ª letra até a 13ª letra da variável

print(frase[9:21]) #Faz o mesmo que o de cima, perceberá que tem a mais e pegará o ultimo valor

print(frase[9:21:2]) #Pegara da 9ª letra até a 21ª letra pulano de 2 em 2

print(frase[:5]) #Pegará do início do caractere 0 e vai até a 5ª letra

print(frase[15:]) # Partirá da 15ª letra até a última

print(frase[9::3]) #Começa apartir da 9ª letra e vai até o final, pulando de 3 em 3

#Análise - Saber as característica da string

print(len(frase)) #Comprimento da variável = Quantidade de espaços, caracteres e etc

print(frase.count('o')) #Conta quantas vezes aparece o "O" na variável
print(frase.count('o', 0, 13)) #Conta do 0 ate o 12 e mostra quantos "O" existem dentro deste fatiamento

print(frase.find('deo')) #Informa onde ele encontra o que é solicitado

print(frase.find('android')) #Quando não acha ele retorna "-1"

print('Curso' in frase) #Diz se existe o que está sendo procurado (Em boleano)

#Transformação - Em via de regra uma lista de string é imutável.

print(frase.replace('Python', 'Android')) #Substitui a palavra pela outra

print(frase.upper()) #Retorna a string com as letras maiúsculas, deixando as maiúsculas e só mexendo nas minúsculas

print(frase.lower()) #Mesmo da anterio porém ao contrário

print(frase.capitalize()) #Deixa apenas a primeira letra maiúscula

print(frase.title()) #Analisa quantas palavras tem através dos espaços e deixa a primeira letra de cada palavra em maiúscila

frase2 = "  Aprenda Python  "

print(frase2.strip()) #Retira os espaços a mais

print(frase2.rstrip()) #Remove os espaços da direita
print(frase2.lstrip()) #Remove os espaços da esquerda

#Divisão - Dividir strings

print(frase.split()) #Divide a string considerando os espaços. Gera uma lista em todas as palavras numa cadeia de caracteres e recria os índices

#Junção - Junta as sting

print('-'.join(frase)) #Junta todos os elementos de "frase" e vai usar "-" como o separador, pode ser usado em espaços em branco
print(''.join(frase))



