#desafio 16

'''num=int(input("insira um numero: "))

if num > 10:
    print("o numero é maior que 10")
else:
    if num <= 10:
     print("o numero é menor ou igual a 10")'''

#desafio 17

'''idade=int(input("insira sua idade: "))

if idade < 13:
    print("Você é uma crionça")
else:
    if idade >= 13 and idade <= 19:
     print("Você é um aborrecente")
    else:
       print("Voce é um adulto")'''

#desafio 18

carros = ["BMW X6", "BMW i5", "BMWi8"]


compra = str(input("qual o nome do carro que voce quer comprar? "))

if compra in carros :
    print("este carro esta disponivel")
else:
    print("desculpe, este carro nao esta disponivel")
