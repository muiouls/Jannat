people = (
    "Батырхан 15 лет",
    "Абил 14 лет",
    "Эмир 17 лет",
    "Даниель 16 лет",
    "Улан 19 лет",
    "Жаннат 19 лет",
    "Арген 18 лет",
    "Жетиген 18 лет",
    "Адыл online",
    "Бекболот 18 лет"
)


kat = 'Бека'

def may(a):
    print(a, 'мяукает')

#may(kat)


print(type(kat))

# коробка для создания данных
# все функции внутри класса называются -- методами
class Kat:
    hvost = True
    usiki = True

    # конструктор класса
    # магический метод
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def m(self):
        self.may()

    def may(self):
        print(self.name,'may')

    def __len__(self):
        return len(f'{self.name}')

    def __str__(self):
        return f'my name is {self.name}\n' \
               f'age is {self.age}\n' \
               f'i am a cat \n'\
               f'{self.hvost}\n'\
               f'#########'
kat2 = Kat('Aрген',4, 'оранжевый' )
kat2.name = 'Адыл'
kat3 = Kat('Эмир',2, 'красный' )
kat2.m()

print(len(kat2))
print(kat2)
print(kat3)
