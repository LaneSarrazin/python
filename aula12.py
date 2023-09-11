class Carro:
    def __init__(self, velMax, ligado, cor):
        self.velMax= velMax
        self.ligado = ligado
        self.cor = cor
        
    def Mostrar(self):
        print('velocidade maxima: ' +str(self.velMax))
        print('cor...........: ' + self.cor)  
        
        estado = "sim" if self.ligado else "nao"
        print('ligado ...............: '+ estado)
        print("********************************")
        
        
c1 = Carro(200, False , "preto")
c2 = Carro(120, False, "Rosa")
c3 = Carro(300, True, "Roxo")
        
c1.Mostrar()
c2.Mostrar()
c3.Mostrar()
        
        
