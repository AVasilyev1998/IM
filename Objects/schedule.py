from collections import deque
from Objects import film_creator
import datetime


class Scheduler:
    """
        управление расписанием сеансов
        Три очереди на каждый из залов
        Каждому сеансу: фильм, время начала, время конца, зал, стоимость билета (добавить в сущность)
        Время начала генерируется автоматически,
            Ставится либо через 30 минут после окончания предыдущего сеанса в зале,
            либо с самого начала рабочего дня
            (т.е. три очереди инициализируются сеансом с временем начала фильма в 8-00)
        Длительность сеанса помогает вычислить время окончания соответствующего сеанса
            Она равна длительности фильма + 15 минут (типа рекламу покрутим в это время)
        Время окончания сеанса = время начала + длительность
            Если длительность сеанса должна будет отсрочить окончание сеанса на 02:00 и позже,
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



class Session:
    def __init__(self, film, start_time: datetime.datetime, ticket_price):
        self.film = film
        self.start_time = start_time
        minutes = self.film.duration
        hours = minutes // 60
        minutes = minutes - 60 * hours
        print(hours, minutes)
        self.end_time = self.start_time + datetime.timedelta(hours=hours, minutes=minutes)\
                        + datetime.timedelta(minutes=15)
        self.ticket_price = ticket_price

    def __repr__(self):
        return f'{self.film.name} | {self.start_time.strftime("%H:%M")} | {self.end_time.time().strftime("%H:%M")}'


if __name__ == "__main__":
    with open('Objects/films.txt', 'r') as reader:
        films = []
        for film in reader:
            films.append(film.strip('\n'))
        creator = film_creator.FilmCreator(names=films)

    start = datetime.datetime.combine(datetime.date.today(), datetime.time(8, 0))
    ses = Session(film=creator.create_film(), start_time=start, ticket_price=100)
    print(ses)
