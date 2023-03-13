#1 Наследование
# object
#
#2 Полиморфизм

#3 Инкапсуляция
# _ = защищенный
# __ = скрытый

class Bank:
    def __init__(self, name, money, key):
        self.name = name
        self.__money = money
        self._key = key
    def __str__(self):
        return f'{self.name}:{self.__money}'
    def keys(self):
        print(self._printKey())

    def _printKey(self):
        print(self._key())
user = Bank('Жаннат', 4_000_000, '12edswsdw')
# user.keys()
# user._key = '1234'
# user._printKey()
# user.keys()
# print(user._key)

user._Bank__money = 100000
# print(Bank.__money)
print(user)
print(user.__dir__())