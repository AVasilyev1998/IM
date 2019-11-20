from Objects.film_creator import FilmCreator
from Objects.film_queue import FilmQueue

FILE_WITH_FILMS = 'Objects/films.txt'


def simulate(debug=True):
    # --------------------------------- Создаем очередь фильмов ------------------------------
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
    # --------------------------------- Создаем очередь фильмов ------------------------------



if __name__ == "__main__":
    simulate(debug=True)
