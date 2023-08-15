#while loops 

#eu preciso criar um promocao para um produto no valor de 100
#so  que a promocao tem um porem ela comeca com 100 e depois vai baixando pra 5

''''valor = 100
dia = 0

while valor > 20:
    dia += 1
    print('{}° dia da promocao'.format(dia))
    print('esta no valor {},00$ de desconto '.format(valor))
    valor -= 5'''
    
#operador ternario

idade = 15

'''if idade >= 16:
    resultado = print('voto permitido')
    resultado = print('nao permitido')'''
    
resultado = 'voto permitido' if idade >= 16 else 'voto nao permitido'
print(resultado)

