from collections import deque
from Objects.film_creator import FilmCreator
from Objects.film import Film


class FilmQueue:
    """
        Очередь фильмов
    """
    def __init__(self):
        self.__deque = deque()

    def add_film(self, film: Film):
        self.__deque.append(film)

    def get_film(self) -> Film:
        return self.__deque.popleft()

    def __repr__(self):
        return f'{self.__deque}'


if __name__ == "__main__":
    films = []
    with open('Objects/films.txt', 'r') as reader:
        for film in reader:
            tmp_film = film.strip('\n')
            films.append(tmp_film)
    creator = FilmCreator(names=films)

    film_queue = FilmQueue()
    film_queue.add_film(creator.create_film())
    film_queue.add_film(creator.create_film())
    print(film_queue)
    print(film_queue.get_film())
    print(film_queue)
    film_queue.add_film(creator.create_film())
    print(film_queue)