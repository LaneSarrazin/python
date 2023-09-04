'''class Pessoa:
    def __init__(self, nome , idade):
        self.nome = nome
        self.idade = idade'''
        
'''class funcionarios:
    nome = "Rosi"
    sobrenome ="Sarrazin"
    
usuario1 = funcionarios()

print(usuario1.nome)'''

#importando modulo

from datetime import datetime

#criar classe

class Funcionario:
    def __init__(self,nome,sobrenome,data_nas):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nas = data_nas
        
    def nome_completo(self):
        return self.nome + " " + self.sobrenome
    
    def idade_funcionario(self):
         ano_atual = datetime.now().year
         self.data_nas = int(ano_atual - self.data_nas)
         return self.data_nas
         


#criar um objeto

usuario1 = Funcionario("Maria", "Alves", 1995)
usuario2 = Funcionario("Susi", "Marques", 2009)

#print(usuario1.nome_completo())
#print(usuario2.nome)
print(Funcionario.nome_completo(usuario2))
print(Funcionario.idade_funcionario(usuario1))
#criar os parametros

'''usuario1.nome = "Rosi"
usuario1.sobrenome = "Sarrazin"
usuario1.data_nas = "25/10/23"

usuario2.nome = "Bia"
usuario2.sobrenome = "Falcao"
usuario2.data_nas = "15/12/23"

#print

print(usuario1.nome)
print(usuario2.nome)'''
        
     
        









