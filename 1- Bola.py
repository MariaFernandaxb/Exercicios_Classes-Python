# Classe Bola: Crie uma classe que modele uma bola: Atributos: Cor,
# circunferência, material
# Métodos: trocaCor e mostraCor

class Bola:
    def __init__ (self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, nova_cor):
        self.cor = nova_cor
      

    def mostraCor(self):
       return self.cor
    

bola01 = Bola(cor='vermelha', circunferencia= '10', material='plastico' )
print("Cor da bola: ",bola01.mostraCor())
bola01.trocaCor('azul')
print("Nova cor da bola: ",bola01.mostraCor()) 
