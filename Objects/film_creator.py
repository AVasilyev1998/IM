"""
creating random objects type of Film
"""
from film import Film
import random
import datetime
from timeit import Timer


class FilmCreator:
    """
    film: name, end_date, duration
    """
    def __init__(self, file_name='films.txt'):
        film_names_list = []
        with open(file_name, 'r') as reader:
            for film in reader:
                film_names_list.append(film.strip('\n'))
        self.names = film_names_list

    def create_film(self) -> Film:
        end_date = datetime.datetime.now() + datetime.timedelta(days=14)
        gen_duration = int(random.random()*70 + 110)
        generated_film = Film(end_date=end_date, name=random.choice(self.names), duration=gen_duration)
        return generated_film


if __name__ == "__main__":
    print('FilmCreator')