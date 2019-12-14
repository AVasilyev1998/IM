import datetime
from random import choice


class CinemaHall(object):
    """
    Зал
    name - наименование
    capacity - вместительность
    last_film_end_time - время окончани последнего фильма
    """

    def __init__(self, last_film_end_time = datetime.datetime.combine(datetime.date.today(),datetime.time(8, 0)),
                 name=0, capacity=0):
        if not name and not capacity:
            self.last_film_end_time = last_film_end_time
            self.create_hall()  # выбираем название и вместительность зала
        elif name and capacity:
            self.last_film_end_time = last_film_end_time
            self.name = name
            self.capacity = capacity
            # self.statistics = {}  # для сбора статистики по залу (возможно не понадобится)
        else:
            raise TypeError

    def create_hall(self):
        halls_names = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        halls_capacities = [5, 7, 10, 16, 25, 27, 32, 44, 49, 55, 64, 81, 88, 100, 125, 256]
        self.capacity = choice(halls_capacities)
        self.name = choice(halls_names)
        # self.statistics = {}  # для сбора статистики по залу (возможно не понадобится)
        return self

    def __repr__(self):
        return f'name: {self.name}\n' \
               f' capacity: {self.capacity}\n' \
               f' last_film_end_time: {self.last_film_end_time}\n'


if __name__ == '__main__':
    hall = CinemaHall()
    print(hall)

    hall2 = CinemaHall(name='XL', capacity=200)
    print(hall2)

    try:
        a = CinemaHall(name='XL', last_film_end_time=1)
    except TypeError:
        print('Возможен ввод только всех параметров сразу: TypeError')
