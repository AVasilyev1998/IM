"""
    Фильм
    - название
    - дата окончания проката DD-MM-YY
    - продолжительность HH-MM
"""
class Film():
    def __init__(name, end_date, duration):
        self.name = name
        self.end_date = end_date
        self.duration = duration
