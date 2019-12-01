from collections import deque
import datetime
from random import random

from session import Session
from film_creator import FilmCreator
from cinema_hall import CinemaHall

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
        self.films_list = []
        self.halls_list = []
        tmp_film_names = []
        tmp_hall_names = []
        tmp_film = 0
        tmp_hall = 0
        while len(self.films_list) != f:
            tmp_film = FilmCreator().create_film()
            if tmp_film.name not in tmp_film_names:
                self.films_list.append(tmp_film)
                tmp_film_names.append(tmp_film.name)
        while len(self.halls_list) != h:
            tmp_hall = CinemaHall().create_hall()
            if tmp_hall.name not in tmp_hall_names:
                self.halls_list.append(tmp_hall)
                tmp_hall_names.append(tmp_hall.name)

        # время закрытия кинотеатра
        self.close_time = datetime.datetime.combine(datetime.date.today(), datetime.time(2, 0)) + datetime.timedelta(hours=24)

        self.queues = [] # список всех сеансов по всем залам
        for i in range(h):
            self.queues.append(deque())

    def create_schedule(self):
        fi = 0
        hi = 0
        tmp_film = FilmCreator().create_film()
        f = len(self.films_list)
        h = len(self.halls_list)
        if f == 0 or h == 0:
            return self

        # заполняем расписание сеансами, пока не упремся в 2-00 след.дня
        while True:

            # выбираем следующий зал с минимальным временем окончания предыдущего фильма
            min_t = self.halls_list[0].last_film_end_time
            hi = 0
            for i in range(h):
                if self.halls_list[i].last_film_end_time < min_t:
                    min_t = self.halls_list[i].last_film_end_time
                    hi = i

            # выбираем фильм для зала
            # если выбор всех возможных фильмов продлевает жизнь кинотеатра за self.close_time,
            # то мы заканчиваем формирование дневного расписания и выдаем его
            tmp_film = self.films_list[fi]
            fi += 1
            if fi == f:
                fi = 0

            if self.halls_list[hi].last_film_end_time + datetime.timedelta(minutes=tmp_film.duration) + datetime.timedelta(minutes=45) > self.close_time:
                for i in range(f):
                    if self.halls_list[hi].last_film_end_time + datetime.timedelta(minutes=self.films_list[i].duration) + datetime.timedelta(minutes=45) < self.close_time:
                        tmp_film = self.films_list[i]
                else:
                    return self

            # формирование сеанса
            tmp_session = Session(self.halls_list[hi], tmp_film)
            self.queues[hi].append(tmp_session)
            
            # изменение времени окончания последнего фильма у соответствующего зала
            self.halls_list[hi].last_film_end_time = tmp_session.end_time


    def __repr__(self):
        return f'сеансов в залах:\n s:{len(self.queue_s)} | m:{len(self.queue_m)} | l:{len(self.queue_l)}'


if __name__ == "__main__":
    films_count = 7
    halls_count = 3
    
    # наполнение тестового расписания фильмами и залами
    test_schedule = Schedule(films_count, halls_count)

    # составление расписания
    test_schedule = test_schedule.create_schedule()

    # вывод тестового расписания по залам
    for i in range(halls_count):
        print(f'\n{i+1}-й зал:')
        print(test_schedule.halls_list[i])
        for j in range(len(test_schedule.queues[i])):
            print(test_schedule.queues[i][j])

