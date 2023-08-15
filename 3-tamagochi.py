# Classe Bichinho Virtual:Crie uma classe que modele um Tamagotchi
# (Bichinho Eletrônico): Atributos: Nome, Fome, Saúde e Idade b.
# Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome,
# Saúde e Idade Obs: Existe mais uma informação que devemos levar
# em consideração, o Humor do nosso tamagotchi, este humor é uma
# combinação entre os atributos Fome e Saúde, ou seja, um campo
# calculado, então não devemos criar um atributo para armazenar esta
# informação por que ela pode ser calculada a qualquer momento


class BichinhoVirtual:
    def __init__ (self,nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    
    def status_fome(self):       
        #fome  = 0 , inicial 0, considere acima de 100 prejudicial
        try:
            comida = int(input(f'Digite o status de alimentação do(a) {self.nome}: '))
            if comida >= 65 and comida <= 99:
                print(f'Alimentação do(a) {self.nome} Ok!')
                criandotamagotchi.menu()
            elif comida > 100:
                print(f'Não exagere na alimentação do(a) {self.nome} !')
                criandotamagotchi.menu()
            elif comida <= 64 : 
                print(f'Alimente o(a) {self.nome} !')  
                criandotamagotchi.menu() 
        except ValueError as e:   #mensadem de erro na tela. 
            print(f'Opção inválida ! Digite números para identificar o status \n Detalhes: {e}')
            criandotamagotchi.menu()       

    def status_saude(self):
            #saude = 100 , considere a metade do valor e acima implicando a saude.
        try: 
            cuidados = int(input(f'Digite o status de saúde do(a) {self.nome}: '))
            if cuidados  <= 59 : 
                print(f'{self.nome} precisa de cuidados ! Fique atento ! ')
                criandotamagotchi.menu()
            elif cuidados >= 60 and cuidados <= 99:
                print(f'Saúde do(a) {self.nome} estável')
                criandotamagotchi.menu()
            elif cuidados > 100:
                print(f'Cuidados com exageros para não implicar a saúde do(a) {self.nome} ')
                criandotamagotchi.menu()
        except ValueError as e:   #mensadem de erro na tela. 
            print(f'Opção inválida ! Digite números para identificar o status \n Detalhes: {e}')
            criandotamagotchi.menu()    

    def status_idade(self):
        #idade inicial = 0 ,dia na terra equivale a um ano para o Tamagotchi e ele vive por aproximadamente 25 a 28 dias.
        try: 
            dias = int(input(f"Digite a idade do(a) {self.nome} :  "))
            if dias == 0:
                print(f'Vamos dar início aos cuidados do(a) {self.nome}')
                criandotamagotchi.menu()
            elif dias >= 1 and dias <= 27: 
                print(f'Está indo bem com o(a) {self.nome}, fique atento aos cuidados !')
                criandotamagotchi.menu()
            elif dias == 28: 
                print(f'O(a) {self.nome} morreu. ') 
                criandotamagotchi.menu()
            elif dias > 28: 
                print( 'Tempo excedido ! Faça 1 minuto de silêncio e reinicie o jogo')
                criandotamagotchi.menu()
        except ValueError as e:   #mensadem de erro na tela. 
            print(f'Opção inválida ! Digite números para identificar o status \n Detalhes: {e}')
            criandotamagotchi.menu()   


    def status_humor(self):
        # combinação entre Fome e Saúde
        try:
            humor = (self.saude + self.fome )/ 2
            print(humor)
            if humor <= 29: 
                print(f'Cuide do(a) {self.nome}, ele parece triste ! ')
                criandotamagotchi.menu()
            elif humor >= 30 and humor <= 99:
                print(f'O(a) {self.nome} está feliz ! Continue vigiando')
                criandotamagotchi.menu()
            elif humor > 100:
                print(f'Cuide do(a) {self.nome} ele parece estressado !')
                criandotamagotchi.menu()
        except ValueError as e:   #mensadem de erro na tela. 
            print(f'Opção inválida ! Digite números para identificar o status \n Detalhes: {e}')
            criandotamagotchi.menu()   
            
    def sair(self):
        print('Saindo ... ')
        quit() #encerra um programa ao ser executada

    def menu(self): #Menu de todas as funções.
        opcao = int(input(f'\n Menu do(a) {self.nome} \n Escolha as Opções: \n 1- Alimentar\n 2- Idade \n 3- Saúde \n 4- Humor \n 5- Sair \n'))
        if opcao == 1:
          criandotamagotchi.status_fome()
        elif opcao == 2:
            criandotamagotchi.status_idade()
        elif opcao == 3:
            criandotamagotchi.status_saude()
        elif opcao == 4:
            criandotamagotchi.status_humor()
        else:
            criandotamagotchi.sair()

                    #status inciais:  #nome , fome , saude , idade
criandotamagotchi = BichinhoVirtual(input('Digite o nome do seu bichinho: '), 0 ,100,0)
                                    
#chamando a função menu
criandotamagotchi.menu()

