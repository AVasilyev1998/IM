import datetime


class CinemaHall(object):
    """
    Зал
    - вместительность
    - наименование
    - время начала след фильма
    """

    def __init__(self, name, capacity, next_film_time):
        self.name = name
        self.capacity = capacity
        self.next_film_time = next_film_time

    def __repr__(self):
        return f'name: {self.name} | capacity: {self.capacity} | next_film_time: {self.next_film_time}'


if __name__ == '__main__':
    hall = CinemaHall('S', 20, datetime.datetime.now().strftime('%H:%M'))
    print(hall)
