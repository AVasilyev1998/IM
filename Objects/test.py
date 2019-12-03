import simpy
from client import Client
import random
from scheduler import Schedule
import datetime

# push test
class ClientSim(object):
    def __init__(self, env, films_list: list, schedule: Schedule):
        self.client = Client(films_list)
        self.action = env.process(self.run())
        self.env = env
        self.name = self.client.id
        self.schedule = schedule
        self.available_sessions = []

    def run(self):
        if len(food_shop.queue) // 2 < len(ticket_shop.queue):  # TODO: передать ticket и food кассы в класс при инициализации
            # print(f'{self.name} buying food first')
            if self.client.food_preference + self.client.drink_preference != 0:
                with food_shop.request() as req:
                    yield req
                    yield self.env.process(self.buy_snacks())
            with ticket_shop.request() as req:
                yield req
                yield self.env.process(self.buy_ticket())
        else:
            # print(f'{self.name} buying tickets first')
            with ticket_shop.request() as req:
                yield req
                yield self.env.process(self.buy_ticket())
            if self.client.drink_preference + self.client.food_preference != 0:
                with food_shop.request() as req:
                    yield req
                    yield self.env.process(self.buy_snacks())

    def get_available_sessions(self) -> list:
        now = datetime.datetime.combine(datetime.date.today() + datetime.timedelta(days=int((8 + round(self.env.now)) // 1440)),
                                                                                datetime.time((8 + round(self.env.now // 60) % 24),
                                                                                                 round(self.env.now) % 60))
        now_minus_30min = now - datetime.timedelta(minutes=30)
        now_plus_1hour = now + datetime.timedelta(hours=1)
        sessions = []
        for i in range(len(self.schedule.queues)):
            for j in range(len(self.schedule.queues[i])):
                start_time = self.schedule.queues[i][j].start_time
                free_sits = self.schedule.queues[i][j].free_sits
                # print(now_minus_30min, start_time, now_plus_1hour)  # TODO: delete before merge to master
                if now_minus_30min < start_time < now_plus_1hour and free_sits > 0\
                        and self.schedule.queues[i][j].available is True:
                    sessions.append(self.schedule.queues[i][j])
        # print(sessions)
        return sessions

    def choise_session(self):
        for i in self.client.films:
            # { film_name : session }  dict([(,) for i in ...])
            session_dict = dict([(session.film_name, session) for session in self.available_sessions])
            # print(session_dict, self.client.films)
            session_films = [session.film_name for session in self.available_sessions]
            if i.name in session_films:
                return session_dict[i.name]
        return None         # возвращаем пустоту, если для клиента нет подходящего фильма

    def buy_ticket(self):
        # TODO: когда кончаются билеты удалить сессию из расписания (сделать недоступной)
        self.available_sessions = self.get_available_sessions()
        choiced_session = self.choise_session()
        if choiced_session is not None:
            choiced_session.free_sits -= 1
            if choiced_session.free_sits == 0:
                choiced_session.available = False
            self.client.statistics['ticket buying'] = [choiced_session.film_name,
                                                       choiced_session.hall_name,
                                                       self.env.now]
            minute = -1
            if 0 < self.env.now % 60 < 10:
                minute = f'0{int(self.env.now) % 60}'
            elif self.env.now == 0:
                minute = '00'
            print(
                f'{self.name} bought ticket at {int(self.env.now) // 60 + 8}:'
                f'{int(self.env.now) % 60 if minute == -1 else minute}'
            )
            print(f'на фильм {choiced_session.film_name} осталось'
                  f' {choiced_session.free_sits} билетов'
                  )
            yield self.env.timeout(0.5)
        else:
            self.client.statistics['ticket buying'] = 'client went away'
            print(f'{self.name} didnt find needed film and went away')

    def buy_snacks(self):
        timeout_snacks = self.client.drink_preference + self.client.food_preference
        self.client.statistics['snacks buying'] = (self.env.now, self.client.id)
        minute = -1
        if 0 < self.env.now % 60 < 10:
            minute = f'0{int(self.env.now) % 60}'
        elif self.env.now == 0:
            minute = '00'
        print(f'{self.name} bought snacks at {int(self.env.now) // 60 + 8}:{int(self.env.now) % 60 if minute == -1 else minute}')
        yield self.env.timeout(timeout_snacks)



daily_schedule = Schedule(7, 3)
print(daily_schedule)


#
films_for_choice = daily_schedule.films_list


env = simpy.Environment()
ticket_shop = simpy.Resource(env, capacity=2)
food_shop = simpy.Resource(env, capacity=1)

clients = []
for i in range(3000):
    client = ClientSim(env, films_for_choice, daily_schedule)
    clients.append(client)
env.run(until=1080)



