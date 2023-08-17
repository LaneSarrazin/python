#geralmente o default fica na frente do non-default

#non-default

'''def boas_vindas(quantidade, nome='marcos'):
    print(f'ola {nome}')
    print(f'temos{str(quantidade)} laptops em estoque')
    
    boas_vindas(7)
    
    #print realiza a tarefa
    #return calcula o rertorno do valor
    
    def cliente(nome):
        print(f'ola {nome}')
        cliente('maria')
        
        
    def cliente2(nome):
        return f'ola {nome}'
    cliente2('Jose')
    
    x = cliente('maria')
    y = cliente2('Jose')
    
    print(x)
    print(y)'''
    
#criar uma funcao que soma varios numeros
#* colocando o asteristicos posso receber varios valores
#* um asteristicos para receber varios parametros

def soma(*numeros):
    
    resultado = 0
    
    for num in numeros:
        resultado +=num
        
    return resultado

x = soma(2,3,4,5,7)
print(x)

def somador(v1,v2):
    soma = v1 +v2
    return soma

#define soma
#criando uma variavel para receber esse valor 

#chama a funcao
res = somador (3,4)

print(f'valor e {res}')

#declarcao da funcao
def imprime_msg(nomePessoa):
    print(f'o usuario {nomePessoa} kkkkkkkkk')
    
#chamando a funcao

nome = input('digite seu nome')
imprime_msg(nome)


#criar uma funcao que armazena numeros e strings(dados)

#varios argumentos
#dois asteristicos posso armazenar mais argumento

def agencia(**carro):
    return carro

print(agencia(marca= 'gol',cor = 'branca',motor= 1.0))
print(agencia(marca= 'fiat',cor = 'azul',motor= 2.0))
print(agencia(marca= 'siena',cor = 'rosa',motor= 3.0))


    
    





        
        