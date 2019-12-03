import simpy
from client import Client
import random
from scheduler import Schedule
import datetime


class ClientSim(object):
    def __init__(self, env, films_list: list, schedule: Schedule):
        self.client = Client(films_list)
        self.action = env.process(self.run())
        self.env = env
        self.name = random.randint(1000, 9999)
        self.schedule = schedule
        # self.available_sessions = self.get_available_sessions()

    def run(self):
        while True:
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
        now = datetime.datetime.combine(datetime.date.today(), datetime.time(8, round(self.env.now)))
        now_minus_30min = now - datetime.timedelta(minutes=30)
        now_plus_1hour = now + datetime.timedelta(hours=1)
        sessions = []
        for i in range(len(self.schedule.queues)):
            for j in range(len(self.schedule.queues[i])):
                start_time = self.schedule.queues[i][j].start_time
                free_sits = self.schedule.queues[i][j].free_sits
                # print(now_minus_30min, start_time, now_plus_1hour)  # TODO: delete before merge to master
                if now_minus_30min < start_time < now_plus_1hour and free_sits > 0:
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
            print(f'{self.name} bought ticket to {choiced_session.film_name} at {round(self.env.now, 2)}')
            print(f'на фильм {choiced_session.film_name} осталось'
                  f' {choiced_session.free_sits} билетов')
            yield self.env.timeout(0.5)

        else:
            print(f'{self.name} didnt find needed film and went away')

    def buy_snacks(self):
        timeout_snacks = self.client.drink_preference + self.client.food_preference
        yield self.env.timeout(timeout_snacks)
        print(f'{self.name} bought snacks at {round(self.env.now, 2)}')


daily_schedule = Schedule(7, 3)
print(daily_schedule)


#
films_for_choice = daily_schedule.films_list


env = simpy.Environment()
ticket_shop = simpy.Resource(env, capacity=2)
food_shop = simpy.Resource(env, capacity=1)


for i in range(40):
    ClientSim(env, films_for_choice, daily_schedule)

env.run(until=20)

