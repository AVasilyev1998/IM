from collections import deque
from client import Client


class FoodShop(object):
    """
    Ларёк
    - id сотрудника, который сейчас работает за кассой (добавить)
    - время покупки еды
    - время покупки воды
    """
    def __init__(self, food_time, drink_time):
        self.queue = deque()
        self.food_buy_time = food_time
        self.drink_buy_time = drink_time

    def __repr__(self):
        return f'Shop queue: {self.queue.__len__()}'

    def buy_food(self):
        return self.food_buy_time

    def buy_drink(self):
        return self.drink_buy_time

    def add_to_queue(self, client: Client):
        self.queue.append(client)

    def pop_from_queue(self) -> int:
        tmp_client = self.queue.popleft()
        if tmp_client.food_preference and tmp_client.drink_preference:
            return self.buy_drink() + self.buy_food()
        elif tmp_client.food_preference:
            return self.buy_food()
        elif tmp_client.drink_preference:
            return self.buy_drink()
        return 0


if __name__ == '__main__':
    fsh = FoodShop(90, 70)
    for i in range(3):  # смотрю кто сколько ждал в очереди
        cl = Client(['1', '2', '3'])
        fsh.add_to_queue(cl)
    print(fsh)
    from_queue = fsh.pop_from_queue()
    print(from_queue)
    print(fsh)

