from utils.random_mod import random_with_chance


class Client(object):
    """
    Клиент
    - денег достаточно на все хотелки, остальное не важно
    - предпочтения по фильмам (3 фильма) list[]
    - предпочтения по закускам -> boolean  1 or 0
    - предпочтения по напиткам -> boolean 1 or 0
    """
    def __init__(self, films):
        # self.id = hash()
        if isinstance(films, list):
            self.films = films
        else:
            raise TypeError
        self.food_preference = random_with_chance(30) * 0.4
        self.drink_preference = random_with_chance(40) * 0.6
        self.id = str(self.__hash__())
        self.statistics = {}

    def __repr__(self):
        return f'client:{self.id}\n films:{self.films} \n food: {self.food_preference} \n drink: {self.drink_preference}\n'


if __name__ == '__main__':
    unique_clients = set()
    films = ['1', '2', '3']
    for i in range(1000000):
        tmp_cl = Client(films)
        unique_clients.add(tmp_cl.id)
        print(tmp_cl.id)
    print(len(unique_clients))
