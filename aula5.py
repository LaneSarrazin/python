#operadores logicos


#and
'''renda_acima_5mil = True
nome_limpo = True

if not(renda_acima_5mil and nome_limpo):
    print('aprovado')
else:
    print('negado')
    
#or
renda_acima_5mil = True
nome_limpo = True

if renda_acima_5mil or nome_limpo:
    print('aprovado')
else:
    print('negado') '''
    
#idade_Lucas = 21
#idade_Carolina = 19


#operador or

'''if idade_Lucas >= 18 or idade_Carolina >= 18:
 print("pelo menos um do dois é maior de idade")
else:
    print('lucas e carolina sao maiores de idade')'''
    
#operador and
'''if idade_Lucas >= 18 and idade_Carolina >= 18:
    print("lucas e carolina sao maiores de idade")
else:
    print('pelo menos um do dois é maior de idade')'''
    
#multiplos operadores

#valor = 20

#f 20 <= valor < 40:

'''if valor >= 20 and valor < 40:
    print('produto aceito!')
else:
    print('produto nao aceito')'''


#for- imprimir de 1 a 5

'''for numero in range (1,20,2):
    print(numero)'''
    
'''lojas = ['rio', 'sampa', 'belo', 'Manaus']
    
for loja in lojas:
    print(loja)
print('acabou')

for i in range(6):
    #print(i)
    print(loja[i])'''
    
#for para strings

'''palavra = 'google'

for letra in palavra:
    print(letra + ' esta dentro da palavra google')'''
    
#desafio 6

#frutas = ['maça', 'banana', 'manga', 'uva']

#print(frutas)

#desafio 7

'''for fruta in frutas:
    print(frutas[0])
    print(frutas[3])'''
    

#for loop - utilizando if e else
#enviar um email com detalhes da compra online , para compras confirmadas

'''for enviar in range(3):
    if compra_confirmada:
        print('dados das compras')
        break
    else:
        print('falha na compra')'''
        
#for loop - utilizando if e else aninhandos

#outer loop (laço externo)

''''for numero1 in range(5):
    print(numero1)
    for numero2 in range(5):
        print(numero1, [numero2])'''
        
#inner loop (laço interno)

'''for numero1 in range(1,6):
    print('produto {}'.format(numero1))
    for numero2 in range(5):
        print(numero1, [numero2])'''
    
#modificar de fantastico para f a n t a s t i s c o

'''palavra = 'FANTASTICO'

for space in palavra:
    print(space, end='') #sem espaçamento de uma letra para outra
    print(space, end=' ')#espacamento de uma letra para outra'''

#criar um retangulo 6x6

linha = 6
coluna = 6
simbolo = '$'

for l in range(linha):
    for c in range (coluna):
        print(simbolo, end='')



