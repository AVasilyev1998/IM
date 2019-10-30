import random


class Client(object):
    """
    Клиент
    - деньги ?
    - предпочтения по фильмам (3 фильма) list[]
    - предпочтения по закускам -> boolean  1 or 0
    - предпочтения по напиткам -> boolean 1 or 0
    """
    def __init__(self, id, films, food_preferense, drink_preference):
        # self.id = hash()
        if isinstance(films, list):
            self.films = films
        else:
            raise TypeError

        self.food_preferense = random.randint(0, 100)
        self.drink_preference = random.randint(0, 100)

    def __repr__(self):
        return f' films:{self.films} / food: {self.food_preferense} / drink: {self.drink_preference}'

if __name__ == '__main__':
    client = Client(1, ['1', '2', '3'], 1,2)
    print(client)