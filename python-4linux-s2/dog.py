class Dog():
    '''Tentando abstrair um cachorro!'''
    def __init__(self, nome, raca, idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade
        self.energia = 10
        self.sede = 10
        self.fome = 10
    def latir(self):
        self.sede -= 1
        print('Latindo...')
    def andar(self):
        self.energia -= 1
        self.fome -= 1
        self.sede -= 1
        print('Andando...')
    def comer(self):
        self.fome = 10
        print('Comendo...')
    def beber(self):
        self.sede = 10
        print('Bebendo...')
    def dormir(self):
        self.energia = 10
        print('Dormindo...')

dog1 = Dog('Bilu', 'poodle', 2)

for x in range(5):
    dog1.andar()
    dog1.latir()
    dog1.beber()

print(dog1.nome, '''
    energia {}
    fome {}
    sede {}
'''.format(dog1.energia, dog1.fome, dog1.sede), sep='\n')

