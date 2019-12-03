import simpy
from client import Client
import random
from scheduler import Schedule

class ClientSim(object):
    def __init__(self, env, name):
        self.client = Client()
        self.action = env.process(self.run())
        self.env = env
        self.name = random.randint(1000, 9999)

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

    def buy_ticket(self):
        yield self.env.timeout(0.5)
        print(f'{self.name} bought ticket at {round(self.env.now, 2)}')

    def buy_snacks(self):
        timeout_snacks = self.client.drink_preference + self.client.food_preference
        yield self.env.timeout(timeout_snacks)
        print(f'{self.name} bought snacks at {round(self.env.now, 2)}')


daily_schedule = Schedule(7, 3)
print(daily_schedule)

films_for_choice = daily_schedule.films_list

for i in range(10):
    c = Client(films_for_choice)
    print(c)

# env = simpy.Environment()
# ticket_shop = simpy.Resource(env, capacity=2)
# food_shop = simpy.Resource(env, capacity=1)
#
# all_clients = 500
# for part_of_clients in range(all_clients // 10):
#     for i in range(50):
#         ClientSim(env, i)
#
# env.run(until=1000)

