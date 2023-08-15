class CACHORRO: 
    def __init__(self, nome, raca, comprimento, peso):
        self.nome = nome
        self.raca = raca 
        self.comprimento = comprimento
        self.peso = peso

    def latir(self):
        print(f"au au , eu sou o cachorro {self.nome}")
        
    def pesos(self):
        print(f'eu peso: {self.peso}KG')
        
scooby = CACHORRO(nome='scooby',raca='pinscher', comprimento= 10.5, peso= 5)
print(scooby.latir())
print(scooby.pesos())