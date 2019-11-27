import datetime

from cinema_hall import CinemaHall
from film import Film
from scheduler import Schedule, Session


class Ticket(object):
    """
    Билет
    - фильм (по названию)
    - цена билета
    """
    def __init__(self, ticket_session: Session):
        try:
            self.session = ticket_session
        except Exception('Билет без сеанса!') as e:
            print(e)
        # Принтуем ошибку, если у билета не оказалось сеанса.

    def __repr__(self):
        # return f'ticket to {self.hall.next_film_name} with price {self.price}'
        return f"""Film: {self.session.filmName}\n
                    Hall: {self.session.hallName}\n
                    Start: {self.session.start_time}\n
                    Price: {self.session.ticket_price}"""


class TicketOffice(object):
    """
    Касса
    - id сотрудника, который сейчас работает (добавить)
    - билеты, которые продала касса, просто накопитель - стата будущая
    """
    def __init__(self, tickets: list):
        self.tickets = tickets

    def __repr__(self):
        return f'{len(self.tickets)} tickets on sale'

    def sale_ticket(self, film: Film):
        iter = 0
        for ticket in self.tickets:
            pass


if __name__ == '__main__':
    # film = Film('33 разбойника', datetime.datetime.now().strftime('%d/%m/%y'), '1:20')
    # print(film)
    # ticket = Ticket(film, 120)
    # print(ticket)
    # ticket_list = list()
    # ticket_list.append(ticket)
    # office = TicketOffice(ticket_list)
    # print(office)
    print('Ticket-TicketOffice')