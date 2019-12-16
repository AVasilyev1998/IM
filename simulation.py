import simpy
from client import Client
import pickle
from scheduler import Schedule
import datetime
from random import randint

FILMS_COUNT = 7
HALLS_COUNT = 5
CLIENT_GEN_TIMEOUT = 0.5
TICKET_SHOP_CAPACITY = 3
FOOD_SHOP_CAPACITY = 2


class ClientSim(object):
    def __init__(self, env, films_list: list, schedule: Schedule):
        self.client = Client(films_list)
        self.client.statistics['hall'] = {}
        self.action = env.process(self.run())
        self.env = env
        self.schedule = schedule
        self.client.statistics['schedule'] = schedule
        self.available_sessions = []
        


    def run(self):
        if len(ticket_shop.queue) *1.5 <= len(food_shop.queue):  # TODO: передать ticket и food кассы в класс при инициализации
            with ticket_shop.request() as req:
                self.client.statistics['went to cinema'] = self.env.now
                yield req
                yield self.env.process(self.buy_ticket())
            if self.client.drink_preference + self.client.food_preference != 0:
                with food_shop.request() as req:
                    yield req
                    yield self.env.process(self.buy_snacks())
        else:
            if self.client.food_preference + self.client.drink_preference != 0:
                with food_shop.request() as req:
                    yield req
                    yield self.env.process(self.buy_snacks())
            with ticket_shop.request() as req:
                self.client.statistics['went to cinema'] = self.env.now
                yield req
                yield self.env.process(self.buy_ticket())


    def get_available_sessions(self) -> list:
        now = self.new_now(self.env.now)
        now_minus_30min = now - datetime.timedelta(minutes=30)
        now_plus_1hour = now + datetime.timedelta(hours=1)
        sessions = []
        for i in range(len(self.schedule.queues)):
            for j in range(len(self.schedule.queues[i])):
                start_time = self.schedule.queues[i][j].start_time
                free_sits = self.schedule.queues[i][j].free_sits
                if now_minus_30min < start_time < now_plus_1hour and free_sits > 0\
                        and self.schedule.queues[i][j].available is True:
                    sessions.append(self.schedule.queues[i][j])
        return sessions

    def choise_session(self):
        for i in self.client.films:
            session_dict = dict([(session.film_name, session) for session in self.available_sessions])
            session_films = [session.film_name for session in self.available_sessions]
            if i.name in session_films:
                return session_dict[i.name]
        return None         # возвращаем пустоту, если для клиента нет подходящего фильма

    def new_now(self, now):
        return datetime.datetime.combine(datetime.date.today() +
            datetime.timedelta(days=(8 + round(now) // 60) // 24),  # точный день
            datetime.time((8 + round(now) // 60) % 24, round(now) % 60)
        )

    def buy_ticket(self):
        # TODO: когда кончаются билеты удалить сессию из расписания (сделать недоступной)
        self.available_sessions = self.get_available_sessions()
        self.chosen_session = self.choise_session()
        if self.chosen_session is not None:
            self.chosen_session.free_sits -= 1
            if self.chosen_session.free_sits == 0:
                self.chosen_session.available = False
            self.client.statistics['bought ticket'] = True
            self.client.statistics['film'] = self.chosen_session.film_name
            self.client.statistics['hall']['capacity'] = self.chosen_session.capacity
            self.client.statistics['hall']['name'] = self.chosen_session.hall_name
            now = self.new_now(self.env.now)
            self.client.statistics['ticket buying time'] = self.env.now
            self.client.statistics['session begining time'] = self.chosen_session.start_time
            self.client.statistics['spend money'] = self.chosen_session.ticket_price +\
                (self.client.food_preference + self.client.drink_preference)*250
            print(f'{self.client.id} bought ticket at {now}')
            print(f'на фильм {self.chosen_session.film_name} осталось'
                f' {self.chosen_session.free_sits} билетов')
            yield self.env.timeout(0.5)
        else:
            self.client.statistics['bought ticket'] = False
            self.client.statistics['ticket buying time'] = None
            print(f'{self.client.id} didnt find needed film and went away')

    def buy_snacks(self):
        now = self.new_now(self.env.now)
        self.client.statistics['snacks buying time'] = now
        timeout_snacks = self.client.drink_preference + self.client.food_preference
        self.client.statistics['bought snacks'] = timeout_snacks
        print(f'{self.client.id} bought snacks at {now}')
        yield self.env.timeout(timeout_snacks)


daily_schedule = Schedule(FILMS_COUNT, HALLS_COUNT)
print(daily_schedule)


#
films_for_choice = daily_schedule.films_list


env = simpy.Environment()
ticket_shop = simpy.Resource(env, capacity=TICKET_SHOP_CAPACITY)
food_shop = simpy.Resource(env, capacity=FOOD_SHOP_CAPACITY)

clients = []
def client_creating(env, clients):
    for i in range(3500):
        client = ClientSim(env, films_for_choice, daily_schedule)
        clients.append(client)
        yield env.timeout(CLIENT_GEN_TIMEOUT)
env.process(client_creating(env, clients))
env.run(until=990)

# Перенос статистики в файл
statistic = []
for i in range(clients.__len__()):
    statistic.append(clients[i].client.statistics)
with open('sim.pickle', 'wb') as writer:
    pickle.dump(statistic, writer)
