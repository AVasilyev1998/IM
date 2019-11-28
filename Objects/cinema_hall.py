import datetime
from random import choice

from film import Film


class CinemaHall(object):
    """
    Зал
    - наименование
    - вместительность
    """

    def __init__(self):
        self.name = ""
        self.capacity = 0
        self.last_film_end_time = datetime.datetime.combine(datetime.date.today(), datetime.time(7, 30))

    def create_hall(self):
        halls_names = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        halls_capacities = [5, 7, 10, 16, 25, 27, 32, 44, 49, 55, 64, 81, 88, 100, 125, 256]
        self.capacity = choice(halls_capacities)
        self.name = choice(halls_names)
        return self

    def __repr__(self):
        return f'name: {self.name} | capacity: {self.capacity} | last_film_end_time: {self.last_film_end_time}'


if __name__ == '__main__':
    print('CinemaHall')

