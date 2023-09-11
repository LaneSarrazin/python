#criar uma classe

class Computador:
    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram =  memoria_ram
        self.placa_de_video = placa_de_video
        
    def ExibirInformacoes(self):
        print(self.memoria_ram, self.memoria_ram, self.placa_de_video)
        
    def Desligar(self):
        print("estou desligando")
        
        
        #criar objeto
        
computador1 = Computador('Asus', '16gb', 'Samsung')
    
computador1.ExibirInformacoes()
computador1.Desligar()

#exercicios 

#criem uma class chamada automoveis com parametros = marca ano
#objetos locadora1, locadora2 , locadora3 e imprima valores e marca

class Automoveis:
    def __init__(self,marca, ano):
        
        self.marca = marca
        self.ano = ano
        
        
locadora1 = Automoveis("Gol", "1889")
locadora2 = Automoveis("Fiat", "1995")
locadora3 = Automoveis("Chevrolet", "2005")

print("a marca do meu carro e : " + locadora1.marca + " e o ano e : " + locadora1.ano)  
print("a marca do meu carro e : " + locadora2.marca + " e o ano e : " + locadora2.ano) 
print("a marca do meu carro e : " + locadora3.marca + " e o ano e : " + locadora3.ano)    
            
