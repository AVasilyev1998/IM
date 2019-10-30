import datetime


class Film(object):
    """
    Фильм
    - name -  название
    - end_date - дата окончания проката DD-MM-YY
    - duration - продолжительность HH-MM
    """
    def __init__(self, name, end_date, duration):
        self.name = name if isinstance(name, str) else None
        self.end_date = end_date if isinstance(end_date, str) else None
        self.duration = duration if isinstance(duration, str) else None
        # TODO: дописать поля статистики

    def __repr__(self):
        return f'{self.name}  - {self.duration}  -  {self.end_date}'


if __name__ == '__main__':
    film = Film('Рембо 3', datetime.datetime.now().strftime('%d/%m/%y'), '1:32')
    print(film)
