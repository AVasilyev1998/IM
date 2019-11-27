from collections import deque
from film_creator import FilmCreator
import datetime

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

    def __init__(self, hall: CinemaHall, film: Film, ticket_price,
                 start_time=datetime.datetime.combine(datetime.date.today(), datetime.time(8, 0))):
        self.filmName = film.name
        self.hallName = hall.name
        self.start_time = start_time
        self.end_time = self.start_time + datetime.timedelta(minutes=self.film.duration) + datetime.timedelta(minutes=15)
        self.ticket_price = ticket_price

    def __repr__(self):
        return f'{self.film.name} | starts at: {self.start_time.strftime("%H:%M")} | ends at: {self.end_time.time().strftime("%H:%M")} |' \
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
    def __init__(self):
        """
            хардкод 3х очередей фильмов (если меняется количество залов то следует менять)
        """
        self.queue_x = deque()
        self.queue_m = deque()
        self.queue_l = deque()

        self.creator = film_creator.FilmCreator()

    def set_session(self, hall: CinemaHall, ticket_price):
        session = Session(hall=hall, film=self.creator.create_film(), start_time=datetime.datetime.now(), ticket_price=ticket_price)
        if hall.name == 'x':
            self.queue_x.append(session)
        elif hall.name == 'm':
            self.queue_m.append(session)
        elif hall.name == 'l':
            self.queue_l.append(session)
        else:
            raise Exception('Incorrect hall name exception')

    def __repr__(self):
        return f'сеансов в залах x:{len(self.queue_x)} | m:{len(self.queue_m)} | l:{len(self.queue_l)}'

    def current_session(self, hall: CinemaHall) -> Session:
        if hall.name == 'x' and self.current_x is not None:
            return self.current_x
        elif hall.name == 'm' and self.current_m is not None:
            return self.current_m
        elif hall.name == 'l' and self.current_l is not None:
            return self.current_l
        else:
            raise Exception('Getting session error')

    def run_session(self, hall: CinemaHall):
        if hall.name == 'x' and len(self.queue_x) > 0:
            self.current_x = self.queue_x.popleft()
        elif hall.name == 'm' and len(self.queue_m) > 0:
            self.current_m = self.queue_m.popleft()
        elif hall.name == 'l' and len(self.queue_l) > 0:
            self.current_l = self.queue_l.popleft()


if __name__ == "__main__":
    print('Session-Schedule')
