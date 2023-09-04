'''class Pessoa:
    def __init__(self, nome , idade):
        self.nome = nome
        self.idade = idade'''
        
'''class funcionarios:
    nome = "Rosi"
    sobrenome ="Sarrazin"
    
usuario1 = funcionarios()

print(usuario1.nome)'''

#criar classe

class Funcionario:
    def __init__(self,nome,sobrenome,data_nas):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nas = data_nas
        
    def nome_completo(self):
        return self.nome + " " + self.sobrenome
        


#criar um objeto

usuario1 = Funcionario("Maria", "Alves", "20/08/23")
usuario2 = Funcionario("Susi", "Marques", "06/10/22")

print(usuario1.nome_completo())
print(usuario2.nome)
print(Funcionario.nome_completo(usuario2))
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
        
     
        









