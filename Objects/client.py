from utils.random_mod import random_with_chance


class Client(object):
    """
    Клиент
    - денег достаточно на все потребности -> их не учитываем
    - предпочтения по фильмам (3 фильма) list[]
    - предпочтения по закускам -> boolean  1 or 0
    - предпочтения по напиткам -> boolean 1 or 0
    """
    def __init__(self, films):
        if isinstance(films, list):
            self.films = films
        else:
            raise TypeError
        
        #  2 множитель ниже - продолжительность операции в условных еденицах
        self.food_preference = random_with_chance(30) * 0.4
        self.drink_preference = random_with_chance(40) * 0.6
        
        self.id = str(self.__hash__())  # для идентификации клиентв
        self.statistics = {}  # TODO: собирать статистику по клиенту сюда

    def __repr__(self):
        return f'client:{self.id}\n films:{self.films} \n food: {self.food_preference} \n drink: {self.drink_preference}\n'


if __name__ == '__main__':
    unique_clients = set()
    films = ['1', '2', '3']
    for i in range(10):
        tmp_cl = Client(films)
        unique_clients.add(tmp_cl.id)
        print(tmp_cl.id)
    print(len(unique_clients))
