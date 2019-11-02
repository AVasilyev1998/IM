import datetime
from Objects.film import Film


class CinemaHall(object):
    """
    Зал
    - id - это идентификатор сеанса
    - id сотрудника - номер сотрудника, который сейчас работает в зале (добавить)
    - вместительность
    - наименование
    - время начала след фильма
    """

    def __init__(self, name, capacity, next_film_name, next_film_time):
        self.name = name
        self.capacity = capacity
        try:
            self.next_film_name = next_film_name
        except Exception('Сеанс без фильма!') as e:
            print(e)
        # Принтуем ошибку, если у сеанса не оказалось фильма.
        try:
            self.next_film_time = next_film_time
        except Exception('Сеанс без времени начала фильма!') as e:
            print(e)
        # Принтуем ошибку, если у сеанса не оказалось фильма.
        
    def __repr__(self):
        return f'name: {self.name} | capacity: {self.capacity} | next_film_time: {self.next_film_time}'


if __name__ == '__main__':
    # Задать очередь фильмов, благодаря которой можем загружать сеансы 
    # пока добавил только 1 фильм
    film = Film('33 разбойника', datetime.datetime.now().strftime('%d/%m/%y'), '1:20')
    # hall = CinemaHall('S', 20, film.name, datetime.datetime.now().strftime('%d/%m/%y, %H:%M'))
    hall = CinemaHall('S', 20, '', '')

    print(hall)
