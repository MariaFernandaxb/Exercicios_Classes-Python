# . Classe Pessoa: Crie uma classe que modele uma pessoa:
# Atributos: nome, idade, peso e altura
# Métodos:
# Envelhercer,
# engordar,
# emagrecer,
# crescer.
# Obs: Por padrão, a cada ano que nossa pessoa envelhece,
# sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
class Pessoa:
    def __init__ (self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        aniversario = int(input('Hoje é seu aniversário? \n 1- Sim \n 2- Não \n'))
        if aniversario == 1:
            self.idade += 1
            print(f"Parabéns ! Sua idade agora é: {self.idade}")
        else:
            print(f"Sua idade é {self.idade}")
    
    def calculo_imc(self):
        self.peso = float(input(f'Digite seu peso {self.nome}: '))
        self.altura = float(input(f'Digite sua altura {self.nome}:'))
        imc = self.peso / self.altura ** 2
        print(f'O resultado do seu IMC é de: {imc:.2f}')

        if imc < 18.5 : 
            print('MAGREZA')
        elif imc > 18.5 and imc < 24.9:
            print('NORMAL')
        elif imc > 25 and imc < 29.9:
            print('SOBREPESO')
        elif imc > 30 and imc < 39:
            print('OBESIDADE')
        else: 
            print('OBESIDADE GRAVE')

        
    def emagrecer(self):
       print(f'Verifique seu imc {self.nome}')
       pessoa_maria.calculo_imc()
       

    def engordar(self):
        print(f'Verifique seu imc {self.nome}')
        pessoa_maria.calculo_imc()
        

        
    def crescer(self):    
        self.idade = int(input(f"Digite sua idade {self.nome}: "))
        if self.idade < 21: 
            status_altura = float(input(f"Digite sua altura {self.nome}: "))
            crescimento = (self.altura + 0.05)
            print(f'A altura ideal para sua idade é {crescimento}')
        else: 
            print('idade:',self.idade,'/', 'altura:',self.altura)
    
    def sair_menu(self):
        print('Saindo ...')
        quit() #encerra um programa ao ser executada
                
    def menu(self): #Menu de todas as funções.
        opcao = int(input(f'\n Menu do(a) {self.nome} \n Escolha as Opções: \n 1- Envelhecer \n 2- Crescer \n 3- Emagrecer \n 4- Engordar \n 5- Sair \n'))
        if opcao == 1:
         pessoa_maria.envelhecer()
        elif opcao == 2:
            pessoa_maria.crescer()            
        elif opcao == 3:
            pessoa_maria.emagrecer()
        elif opcao == 4:
            pessoa_maria.engordar()
        else:
            pessoa_maria.sair_menu()
     
#criando a pessoa 
pessoa_maria = Pessoa('Maria', 26 , 75.0 , 1.63)

#chamando o menu para chamar outras funções
pessoa_maria.menu()
