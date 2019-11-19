"""
creating random objects type of Film
"""
from Objects.film import Film
import random
import datetime
from timeit import Timer

class FilmCreator:
    """
    film: name, end_date, duration
    """
    def __init__(self, names: list):
        self.names = names  # подумать над deep copy возможно

    def create_film(self) -> Film:
        end_date = datetime.datetime.now() + datetime.timedelta(days=14)
        gen_duration = int(random.random()*70 + 110)
        generated_name = Film(end_date=end_date, name=random.choice(self.names), duration=gen_duration)
        return generated_name


if __name__ == "__main__":
    films = []
    with open('Objects/films.txt', 'r') as reader:
        for film in reader:
            tmp_film = film.strip('\n')
            films.append(tmp_film)
    creator = FilmCreator(names=films)
    # t = Timer(lambda: creator.create_film) ТЕСТ ПРОИЗВОДИТЕЛЬНОСТИ
    # print(t.timeit(number=20000))
