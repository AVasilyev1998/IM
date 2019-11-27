import datetime
import threading

from film import Film


class CinemaHall(object):
    """
    Зал
    - наименование
    - вместительность
    """

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def __repr__(self):
        return f'name: {self.name} | capacity: {self.capacity}'


if __name__ == '__main__':
    print('CinemaHall')

