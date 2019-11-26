import simpy

from Objects.client import Client
from Objects.film_creator import FilmCreator
from Objects.schedule import Session, Scheduler


films = []
with open('Objects/films.txt', 'r') as reader:
    for film in reader:
        tmp_film = film.strip('\n')
        films.append(tmp_film)
creator = FilmCreator(names=films)


def client(environment, resource, clnt: Client):
    # Request ticketOffice
    print(f'{clnt.id} requesting ticket Office')
    clnt.statistics['ticketOfficeRequest'] = environment.now
    with bcs.request() as req:
        # если сейчас есть билеты на фильмы которые он хочет посмотреть и сеансы вообще начинаются менее чем через 60 минут
        yield req

    # Buying ticket
    print(f'{clnt.id} buying ticket at time {round(environment.now, 3)}')
    clnt.statistics['ticketBought'] = environment.now
    yield env.timeout(clnt.food_preference + clnt.drink_preference)


env = simpy.Environment()
bcs = simpy.Resource(env, capacity=2)

print('as')
NUM_OF_CLIENTS = 100
clients = []
for i in range(NUM_OF_CLIENTS):
    films = [creator.create_film() for i in range(3)]
    tmp_client = Client(films)
    clients.append(tmp_client)

print(clients)
for i in range(NUM_OF_CLIENTS):
    tmp_clnt = clients[i]
    env.process(client(environment=env, resource=bcs, clnt=tmp_clnt))
    env.run()

print(clients[30].statistics)