import datetime


class Film(object):
    """
    Фильм
    - name -  название
    - end_date - дата окончания проката DD-MM-YY
    - duration - продолжительность hh-mm
    """
    def __init__(self, name, end_date, duration):
        # self.id = hash()
        self.name = name if isinstance(name, str) else None
        self.end_date = end_date if isinstance(end_date, str) else (datetime.datetime.now()+datetime.timedelta(days=14)).strftime('%d/%m/%y')
        self.duration = duration if isinstance(duration, int) else None
        # Фильм - ключевая сущность, независимая от других, в том числе и от Зала:
        # удалил self.hall
        # TODO: дописать поля статистики

    def __repr__(self):
        return f'{self.name}  -  {self.duration}  -  {self.end_date}'


if __name__ == '__main__':
    film = Film('Рембо 3', datetime.date(2019, 12, 13).strftime('%d/%m/%y'), '1:32')
    print(film)

