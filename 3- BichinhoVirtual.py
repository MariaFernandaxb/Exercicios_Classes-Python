# Classe Bichinho Virtual:Crie uma classe que modele um Tamagotchi
# (Bichinho Eletrônico): Atributos: Nome, Fome, Saúde e Idade b.
# Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome,
# Saúde e Idade Obs: Existe mais uma informação que devemos levar
# em consideração, o Humor do nosso tamagotchi, este humor é uma
# combinação entre os atributos Fome e Saúde, ou seja, um campo
# calculado, então não devemos criar um atributo para armazenar esta
# informação por que ela pode ser calculada a qualquer momento

import time

class BichinhoVirtual:
    def __init__ (self):
        self.nome = input('Digite o nome do seu Tamagotchi: ')
        while True: 
            try: 
                self.fome =  int(input(f'Digite o status da fome do(a) {self.nome}: '))
                break
            except ValueError:   #mensadem de erro na tela. 
                print(f'Valor inválido ! Digite um número inteiro para identificar o status.')
        while True: 
            try: 
                self.saude = int(input(f'Digite o status de saúde do(a) {self.nome}: '))
                break
            except ValueError:   #mensadem de erro na tela. 
                print(f'Valor inválido ! Digite um número inteiro para identificar o status.')
        while True: 
            try: 
                self.idade =  int(input(f"Digite a idade do(a) {self.nome} :  "))
                break
            except ValueError:   #mensadem de erro na tela. 
                print(f'Valor inválido ! Digite um número inteiro para identificar o status.')
    
    def status_fome(self):       
        #fome  = 0 , inicial 0, considere acima de 100 prejudicial
            if self.fome >= 65 and self.fome <= 99:
                print(f'Alimentação do(a) {self.nome} Ok!')
                self.menu()
            elif self.fome > 100:
                print(f'Não exagere na alimentação do(a) {self.nome} !')
                self.menu()
            elif self.fome <= 64 : 
                print(f'Alimente o(a) {self.nome} !')  
                self.menu() 
           
    def status_saude(self):
            #saude = 100 , considere a metade do valor e acima implicando a saude. 
            if self.saude  <= 59 : 
                print(f'{self.nome} precisa de cuidados ! Fique atento ! ')
                self.menu()
            elif self.saude >= 60 and self.saude <= 99:
                print(f'Saúde do(a) {self.nome} estável')
                self.menu()
            elif self.saude > 100:
                print(f'Cuidados com exageros para não implicar a saúde do(a) {self.nome} ')
                self.menu()
 
    def status_idade(self):
        #idade inicial = 0 ,dia na terra equivale a um ano para o Tamagotchi e ele vive por aproximadamente 25 a 28 dias.  
            if self.idade == 0:
                print(f'Vamos dar início aos cuidados do(a) {self.nome}')
                self.menu()
            elif self.idade >= 1 and self.idade <= 27: 
                print(f'Está indo bem com o(a) {self.nome}, fique atento aos cuidados !')
                self.menu()
            elif self.idade == 28: 
                print(f'O(a) {self.nome} morreu. ') 
                self.menu()
            elif self.idade > 28: 
                print( 'Tempo excedido ! Faça 1 minuto de silêncio e reinicie o jogo')
                self.menu()
      
    def status_humor(self):
        # combinação entre Fome e Saúde
            humor = (self.saude + self.fome )/ 2
            print(humor)
            if humor <= 29: 
                print(f'Cuide do(a) {self.nome}, ele parece triste ! ')
                self.menu()
            elif humor >= 30 and humor <= 99:
                print(f'O(a) {self.nome} está feliz ! Continue vigiando')
                self.menu()
            elif humor > 100:
                print(f'Cuide do(a) {self.nome} ele parece estressado !')
                self.menu()

    def alterar_nome(self):
        self.nome = input('Digite o nome do seu Tamagotchi: ')
        print(f'Nome do tamagotchi alterar para : {self.nome}')
        alt = int(input('Deseja alterar algo mais ? :\n 1- Sim \n 2- Não '))
        if alt == 1: 
            self.novos_dados()
        else:
            self.sair()        

    def alterar_fome(self):
        while True: 
            try: 
                self.fome =  int(input(f'Digite o status da fome do(a) {self.nome}: '))
                self.status_fome()
                break
            except ValueError:   #mensadem de erro na tela. 
                print(f'Valor inválido ! Digite um número inteiro para identificar o status.')
      
    def alterar_saude(self):
        while True: 
            try: 
                self.saude = int(input(f'Digite o status de saúde do(a) {self.nome}: '))
                self.status_saude()
                break
            except ValueError:   #mensadem de erro na tela. 
                print(f'Valor inválido ! Digite um número inteiro para identificar o status.')
                

    def alterar_idade(self):
        while True: 
            try: 
                self.idade =  int(input(f"Digite a idade do(a) {self.nome} :  "))
                self.status_idade()
                break
            except ValueError:   #mensadem de erro na tela. 
                print(f'Valor inválido ! Digite um número inteiro para identificar o status.')
                

    def novos_dados(self):
        opcao = int(input('Escolha a opção que deseja alterar \n 1- Novo nome:  \n 2- Status da Fome:  \n 3- Status da Idade: \n 4- Status da Saude:  \n 0- Sair \n'))
        if opcao == 1:
            self.alterar_nome()
        elif opcao == 2:
            self.alterar_fome()
        elif opcao == 3:
            self.alterar_idade()
        elif opcao == 4:
            self.alterar_saude()
        else:
            self.sair()
           
    def sair(self):
        print('Saindo em ... ')
        for t in range(3,0,-1):
            print(t)
            time.sleep(1)
        print('Bye Bye ! ')
        quit() #encerra um programa ao ser executada

    def menu(self): #Menu de todas as funções.
        opcao = int(input(f'\n Menu do(a) {self.nome} \n  Escolha as Opções: \n 1- Status da Fome \n 2- Status da Idade \n 3- Status da Saúde \n 4- Status do Humor  \n 5- Alterar dados  \n 0- Sair \n'))
        if opcao == 1:
            self.status_fome()
        elif opcao == 2:
            self.status_idade()
        elif opcao == 3:
            self.status_saude()
        elif opcao == 4:
            self.status_humor()
        elif opcao == 5:
            self.novos_dados()
        else:
            self.sair()


#chamando a Classe          
tamagotchi = BichinhoVirtual()
                                    
#chamando a função menu
tamagotchi.menu()

