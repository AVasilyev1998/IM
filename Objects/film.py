import datetime
import random


class Film(object):
    """
    Фильм
    - name -  название
    - end_date - дата окончания проката DD-MM-YY
    - duration - продолжительность hh-mm
    Film() сам сгенерирует фильм
    в противном случае следует задать все параметры, иначе выпадет TypeError
    """
    def __init__(self, name=0, end_date=0, duration=0):
        if not name and not end_date and not duration:
            self.create_film()
        elif name and duration:
            self.name = name if isinstance(name, str) else None
            self.end_date = end_date if isinstance(end_date, str) else (
                        datetime.datetime.now() + datetime.timedelta(days=14)).strftime('%d/%m/%y')
            self.duration = duration if isinstance(duration, int) else None
            self.statistics = {}  # для сбора статистики
        else:
            raise TypeError

    def create_film(self, filename='films.txt'):
        with open(filename, 'r', encoding='utf-8') as reader:
            film_names_list = []
            for film in reader:
                film_names_list.append(film.strip('\n'))
            self.end_date = datetime.datetime.now() + datetime.timedelta(days=14)
            self.duration = int(random.random() * 110 + 70)
            self.name = random.choice(film_names_list)
            self.statistics = {}

    def __repr__(self):
        return f' name: {self.name}\n duration (minutes): {self.duration}\n end_date: {self.end_date}\n'


if __name__ == '__main__':
    f = Film()  # generated film
    print(f)

    f = Film(name='Путешествие Гуливера', duration=135)
    print(f)

    try:
        f = Film(name='TestNameTypeErrorRaisingFilm')
    except TypeError:
        print('Возможен ввод только всех параметров сразу: TypeError')

