from utils.random_mod import random_with_chance


class Client(object):
    """
    Клиент
    - деньги ?
    - предпочтения по фильмам (3 фильма) list[]
    - предпочтения по закускам -> boolean  1 or 0
    - предпочтения по напиткам -> boolean 1 or 0
    """
    def __init__(self, id, films):
        # self.id = hash()
        if isinstance(films, list):
            self.films = films
        else:
            raise TypeError
        self.food_preference = random_with_chance(30)
        self.drink_preference = random_with_chance(40)

    def __repr__(self):
        return f' films:{self.films} / food: {self.food_preference} / drink: {self.drink_preference}'


if __name__ == '__main__':
    client = Client(1, ['1', '2', '3'])
    print(client)