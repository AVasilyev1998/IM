from utils.random_mod import random_with_chance
from random import choice, randint


class Client(object):
    """
    Клиент

    films - предпочтения по фильмам (3 фильма) list[] предпочтения по фильмам по очереди приоритета
    food_preference - предпочтения по закускам -> время покупки закусок (если 0 то покупка не совершается)
    drink_preference - предпочтения по напиткам -> время покупки напитков (если 0 то покупка не совершается)
    id - уникальный идентификатор пользователя

    """
    def __init__(self, client_films):
        if len(client_films) > 3:
            self.films = []
            while len(self.films) < 3:
                tmp_film = choice(client_films)
                if tmp_film not in self.films:
                    self.films.append(tmp_film)
        else:
            self.films = client_films

        #  2 множитель ниже - продолжительность операции в условных еденицах
        self.food_preference = random_with_chance(30) * 0.4
        self.drink_preference = random_with_chance(40) * 0.6
        self.id = hash(randint(0, 10000000) + self.drink_preference + 
                self.food_preference + randint(0, 10000000))
        self.statistics = {
            'id': self.id,
            'went to cinema': None,
            'bought ticket': False,
            'bought snacks': False, 
            'ticket buying time': None,
            'snacks buying time': None,
            'film': None,
            'hall': None,
            'session begining time': None
        }

    def __repr__(self):
        return f'client:{self.id}\nstatistic:{self.statistics}\n' \
               f' films:{[film.name for film in self.films]}' \
               f' \n food: {self.food_preference}' \
               f' \n drink: {self.drink_preference}\n'


if __name__ == '__main__':
    unique_clients = set()
    films = ['1', '2']
    for i in range(100):
        tmp_cl = Client(films)
        unique_clients.add(tmp_cl.id)
        print(tmp_cl.id)
    print(len(unique_clients))
