from collections import deque
import datetime

from session import Session
from film import Film
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

    def __init__(self, film_count, hall_count):
        # произвольное количество фильмов и кинозалов,
        # чтобы было, где смотреть "Крымский мост"
        self.films_list = []
        self.halls_list = []
        tmp_film_names = []
        tmp_hall_names = []
        tmp_film = None
        tmp_hall = None
        while len(self.films_list) != film_count:
            tmp_film = Film()
            if tmp_film.name not in tmp_film_names:
                self.films_list.append(tmp_film)
                tmp_film_names.append(tmp_film.name)
        while len(self.halls_list) != hall_count:
            tmp_hall = CinemaHall()
            if tmp_hall.name not in tmp_hall_names:
                self.halls_list.append(tmp_hall)
                tmp_hall_names.append(tmp_hall.name)

        # время закрытия кинотеатра
        self.close_time = datetime.datetime.combine(datetime.date.today(),
                                    datetime.time(2, 0)) + datetime.timedelta(hours=24)

        self.queues = []  # список всех сеансов по всем залам
        for k in range(hall_count):
            self.queues.append(deque())

        self.create_schedule()

    def create_schedule(self):
        next_film_number = 0
        next_hall_number = 0
        tmp_film = Film()
        films_list_len = len(self.films_list)
        halls_list_len = len(self.halls_list)
        if films_list_len == 0 or halls_list_len == 0:
            raise Exception('Ошибка формирования расписания: список фильмов и(или) список залов пуст')

        # заполняем расписание сеансами, пока не упремся в 2-00 следующего дня
        while True:
            # выбираем следующий зал с минимальным временем окончания предыдущего фильма
            tmp_dict = dict([(self.halls_list[l].last_film_end_time, l) for l in range(halls_list_len)])  # { datetime: i, ...}
            next_hall_number = tmp_dict[min(tmp_dict.keys())]  # d[min(datetime)] - i

            tmp_film = self.films_list[next_film_number]
            next_film_number += 1
            if next_film_number == films_list_len:
                next_film_number = 0

            if self.halls_list[next_hall_number].last_film_end_time +\
                    datetime.timedelta(minutes=tmp_film.duration)\
                    + datetime.timedelta(minutes=45) > self.close_time:
                for k in range(films_list_len):
                    if self.halls_list[next_hall_number].last_film_end_time +\
                            datetime.timedelta(minutes=self.films_list[k].duration) +\
                            datetime.timedelta(minutes=45) < self.close_time:
                        tmp_film = self.films_list[k]
                else:
                    return self

            # формирование сеанса
            tmp_session = Session(self.halls_list[next_hall_number], tmp_film)
            self.queues[next_hall_number].append(tmp_session)
            
            # изменение времени окончания последнего фильма у соответствующего зала
            self.halls_list[next_hall_number].last_film_end_time = tmp_session.end_time

    def __repr__(self):
        ret_str = ''
        for i in range(len(self.halls_list)):
            ret_str += f'{i+1}-й зал:\n'
            ret_str += f'{self.halls_list[i]}\n'
            for j in range(len(self.queues[i])):
                ret_str += f'{self.queues[i][j]}\n'
            ret_str += '\n'
        return ret_str


if __name__ == "__main__":
    films_count = 7
    halls_count = 3
    # наполнение тестового расписания фильмами и залами а затем составление расписания

    test_schedule = Schedule(films_count, halls_count)
    # вывод тестового расписания по залам
    print(test_schedule)