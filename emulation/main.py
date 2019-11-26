import random
from collections import deque

from Objects import schedule
from Objects.cinema_hall import CinemaHall
from Objects.client import Client
from Objects.film_creator import FilmCreator
from Objects.film_queue import FilmQueue
from Objects.ticket_office import TicketOffice, Ticket

FILE_WITH_FILMS = 'Objects/films.txt'
NUM_OF_CLIENTS = 20

def simulate(debug=True,):
    # --------------------------------- Создаем прокат фильмов ------------------------------
    films = []
    with open(FILE_WITH_FILMS, 'r') as reader:
        for film in reader:
            tmp_film = film.strip('\n')
            films.append(tmp_film)
    creator = FilmCreator(names=films)
    films_in_distribution = []
    for i in range(7):
        films_in_distribution.append(creator.create_film())
    print(f'фильмы в прокате:\n {films_in_distribution}') if debug else None
    # --------------------------------- Создаем прокат фильмов ------------------------------

    scheduler = schedule.Scheduler()
    x = CinemaHall('x', 20)
    m = CinemaHall('m', 40)
    l = CinemaHall('l', 60)
    scheduler.set_session(x, 230)
    scheduler.set_session(l, 340)
    scheduler.run_session(x)
    scheduler.run_session(l)
    tickets_x = []
    for i in range(x.capacity):
        tickets_x.append(Ticket(x, scheduler.current_session(x).ticket_price))
    tickets_l = []
    for i in range(l.capacity):
        tickets_l.append(Ticket(l, scheduler.current_session(l).ticket_price))

    TicketOffice(tickets=tickets_x.extend(tickets_l))

    clients_queue = deque()
    for i in range(NUM_OF_CLIENTS):
        clients_queue.append(Client(films=[random.choice(films_in_distribution) for i in range(3)]))

    time_iter = 480  # time in minutes
    while time_iter < 2400:
        client = clients_queue.popleft()
        TicketOffice


if __name__ == "__main__":
    simulate(debug=True)
