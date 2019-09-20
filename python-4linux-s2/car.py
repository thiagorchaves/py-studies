class Car():
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.combustivel = 'gasolina'
    def acelerar(self):
        print('Vrummmm...')
    def freiar(self):
        print('Freiando...')

class Car_eletric(Car):
    def __init__(self, marca, modelo, ano):
        super().__init__(marca, modelo, ano)
        self.combustivel = 'eletrico'
    def acelerar(self):
        print('shifffffff...')


car1 = Car('Renault', 'Sandero', '2019')
car2 = Car_eletric('Chevrolet', 'Bolt', '2020')

print(car1.modelo, car1.combustivel)
car1.acelerar()

print(car2.modelo, car2.combustivel)
car2.acelerar()