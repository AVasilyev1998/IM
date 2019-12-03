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
        Кол-во свободных мест (изначально равно кол-ву мест в самом кинозале)
        Время конца
    Длительность сеанса помогает вычислить время окончания соответствующего сеанса
        Она равна длительности фильма + 15 минут (типа рекламу покрутим в это время)
    Время окончания сеанса = время начала + длительность
    """

    def __init__(self, hall: CinemaHall, film: Film):
        self.film_name = film.name
        self.hall_name = hall.name
        self.free_sits = hall.capacity
        self.start_time = hall.last_film_end_time + datetime.timedelta(minutes=30)
        self.end_time = hall.last_film_end_time + datetime.timedelta(minutes=film.duration)\
                        + datetime.timedelta(minutes=45)
        self.ticket_price = int(random()*200 + 100) # генератор цены билета от 100 до 300

    def __repr__(self):
        # не нравится мне эта реализация, но лень менять, поэтому ок)))
        return f'hall: {self.hall_name} | ' \
                f'film: {self.film_name} | starts at: {self.start_time.strftime("%H:%M")} | ends at: {self.end_time.time().strftime("%H:%M")} | ' \
                f'price: {self.ticket_price}'


if __name__ == "__main__":
    print('Session')