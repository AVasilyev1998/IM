import pickle
import matplotlib.pyplot as plt


def get_statistics():
    with open('sim.pickle', 'rb') as reader:
        data = pickle.load(reader)

    return data


def take_films_halls_statistics(statistic: dict) -> dict:
    statistic_vals = {'films': {}, 'halls': {}}
    for i in range(len(statistic)):
        #  amount of gone people
        if statistic[i]['film'] is None and statistic[i]['hall'] is None:
            statistic_vals['gone'] = statistic_vals.setdefault('gone', 0) + 1
        # amount of bought food
        if statistic[i]['bought snacks'] is True:
            statistic_vals['bought food'] = statistic_vals.setdefault('bought food', 0) + 1
        # halls statistic
        if len(statistic[i]['hall']) > 0:
            name = statistic[i]['hall']['name']
            if statistic_vals['halls'].get(name):
                statistic_vals['halls'][name]['count'] += 1
                statistic_vals['halls'][name]['sumTickets'] += statistic[i]['spend money']
            else:
                statistic_vals['halls'][name] = dict()
                statistic_vals['halls'][name]['capacity'] = statistic_vals['halls'][name].setdefault('capacity', statistic[i]['hall']['capacity'])
                statistic_vals['halls'][name]['count'] = 0
                statistic_vals['halls'][name]['sumTickets'] = 0
        if statistic[i]['film'] is not None:
            statistic_vals['films'][statistic[i]['film']] = statistic_vals['films'].setdefault(
                str(statistic[i]['film']), 0) + 1
        maximum = 0
        for k, v in statistic_vals['films'].items():
            if v > maximum:
                pop_film = k
                maximum = v
        statistic_vals['most popular film'] = pop_film if pop_film != 0 else None
    return statistic_vals


def bought_tickets_to_film(stat_dict, film_cat='films'):
    x_films = []
    y_films = []
    for k, v in stat_dict[film_cat].items():
        x_films.append(k)
        y_films.append(v)
    plt.bar(x_films, y_films)
    plt.grid(b='on')
    plt.yticks()
    plt.tick_params(axis='y',  # Применяем параметры к обеим осям
                   which='minor',
                   length=3,  # Длинна делений
                   width=1,  # Ширина делений
                   color='m',  # Цвет делений
                   pad=10,  # Расстояние между черточкой и ее подписью
                   labelsize=15,  # Размер подписи
                   labelcolor='r',  # Цвет подписи
                   left=True)
    plt.minorticks_on()
    plt.ylabel('Проданные билеты')
    plt.xticks(rotation=75)
    plt.show()


def halls_graphics(stat_dict, hall_cat='halls'):
    x_halls = []
    y_halls = []
    for k, v in stat_dict[hall_cat].items():
        x_halls.append(k)
        y_halls.append(v['count'])
    plt.pie(y_halls, labels=x_halls, explode=[0.04, 0.04, 0.04, 0.04, 0.04],
            shadow=True, autopct='%1.1f%%')
    plt.xticks(rotation=75)
    plt.title('Посещение залов')
    plt.show()


def halls_profit_by_capacity(stat_dict, capacity_cat='capacity', halls_cat='halls'):
    x_halls = []
    y_halls = []
    for k, v in stat_dict[halls_cat].items():
        x_halls.append(k)
        print(k, v)


if __name__ == '__main__':
    statistic_values = get_statistics()
    # print([i for i in statistic_values[1].keys()])
    # print(statistic_values[1]['hall'])
    stat_values = take_films_halls_statistics(statistic_values)
    # print(stat_values)
    # bought_tickets_to_film(stat_values)
    # halls_graphics(stat_values)
    halls_profit_by_capacity(stat_values)





