from collections import deque
from film_creator import FilmCreator
import datetime
from random import random

from cinema_hall import CinemaHall
from film import Film


class Session:
    """
    Поля:
        Название зала (CinemaHall.name)
        Название фильма (Film.name)
        Начало сеанса (относительно воображаемого начала рабочего дня в минутах)
        Стоимость билета (пофиг)
        Время конца
    Длительность сеанса помогает вычислить время окончания соответствующего сеанса
        Она равна длительности фильма + 15 минут (типа рекламу покрутим в это время)
    Время окончания сеанса = время начала + длительность
    """

    def __init__(self, hall: CinemaHall, film: Film):
        self.film_name = film.name
        self.hall_name = hall.name
        self.free_sits = hall.capacity
        self.start_time = datetime.datetime.combine(datetime.date.today(), datetime.time(8, 0))
        self.end_time = self.start_time + datetime.timedelta(minutes=self.film.duration) + datetime.timedelta(minutes=15)
        self.ticket_price = gen_ticket_price()

    def gen_ticket_price(self):
        return int(random.random()*200 + 100) # генератор цены билета от 100 до 300

    def __repr__(self):
        # не нравится мне эта реализация, но лень менять, поэтому ок)))
        return f'{self.film_name} | starts at: {self.start_time.strftime("%H:%M")} | ends at: {self.end_time.time().strftime("%H:%M")} |' \
               f' price: {self.ticket_price}'


class Schedule:
    """
        управление расписанием сеансов
        Три очереди на каждый из залов
        Каждому сеансу: фильм, время начала, время конца, зал, стоимость билета (добавить в сущность)
        Время начала генерируется автоматически,
            Ставится либо через 30 минут после окончания предыдущего сеанса в зале,
            либо с самого начала рабочего дня
            (т.е. три очереди инициализируются сеансом с временем начала фильма в 8-00)
            TODO : Если длительность сеанса должна будет отсрочить окончание сеанса на 02:00 и позже,
                сеанс не назначается и берётся следующий в очереди фильмов
                (не может быть больше 02:00)
    """

    def __init__(self, f, h):
        # произвольное количество фильмов и кинозалов,
        # чтобы было, где смотреть "Крымский мост"
        self.films_list = [FilmCreator().create_film() for i in range(f)]
        self.halls_list = [CinemaHall().create_hall() for i in range(h)]

        self.queues = []
        for i in range(h):
            self.queues.append(deque())

    def __repr__(self):
        return f'сеансов в залах:\n s:{len(self.queue_s)} | m:{len(self.queue_m)} | l:{len(self.queue_l)}'


if __name__ == "__main__":
    films_count = 7
    halls_count = 3
    test_schedule = Schedule(films_count, halls_count)
    for i in range(films_count):
        print(test_schedule.films_list[i])
    for i in range(halls_count):
        print(test_schedule.halls_list[i])
    print('Session-Schedule')
