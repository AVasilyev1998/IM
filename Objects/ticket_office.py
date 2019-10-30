import datetime
from Objects.film import Film


class Ticket(object):
    def __init__(self, ticket_film: Film, price):
        self.film = ticket_film
        self.price = price

    def __repr__(self):
        return f'ticket to {self.film.name} with price {self.price}'


class TicketOffice(object):
    def __init__(self, tickets: list):
        self.tickets = tickets

    def __repr__(self):
        return f'{len(self.tickets)} tickets on sale'


if __name__ == '__main__':
    time = datetime.datetime.now()
    film = Film('33 разбойника', time.strftime('%D'), '1:20')
    print(film)
    ticket = Ticket(film, 120)
    print(ticket)
    ticket_list = list()
    ticket_list.append(ticket)
    office = TicketOffice(ticket_list)
    print(office)
