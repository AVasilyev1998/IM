import pickle
import matplotlib.pyplot as plt


def get_statistics():
    with open('sim.pickle', 'rb') as reader:
        data = pickle.load(reader)

    return data


def take_films_halls_statistics(statistic: dict) -> dict:
    statistic_vals = {'films': {}, 'halls': {}, 'average time in queue': 0, 'clients amount': 0, 'revenue': 0}
    for i in range(len(statistic)):
        # revenue and clients amount
        if statistic[i]['bought ticket']:
            statistic_vals["revenue"] += statistic[i]['spend money']
            statistic_vals['clients amount'] += 1
        #  amount of gone people
        if statistic[i]['film'] is None and statistic[i]['hall'] is None:
            statistic_vals['gone'] = statistic_vals.setdefault('gone', 0) + 1
        # amount of bought food
        if statistic[i]['bought snacks'] is True:
            statistic_vals['bought food'] = statistic_vals.setdefault('bought food', 0) + 1
        # time in queue statistic
        if statistic[i]['bought ticket']:
            statistic_vals['average time in queue'] += (statistic[i]['ticket buying time'] - statistic[i]['went to cinema'])
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
    statistic_vals['average time in queue'] = statistic_vals['average time in queue'] // len(statistic)
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
                   labelcolor='r',  # Цвет подписи
                   left=True)
    plt.minorticks_on()
    plt.ylabel('Sold tickets')
    plt.title('Tickets to films')
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
    plt.title('Halls visiting')
    plt.show()


def halls_profit_by_capacity(stat_dict, capacity_cat='capacity',sum_cat='sumTickets', halls_cat='halls'):
    x_halls = []
    y_halls = []
    for k, v in stat_dict[halls_cat].items():
        x_halls.append(f'{k} with capacity: {v[capacity_cat]}')
        y_halls.append(round(v[sum_cat] / v[capacity_cat], 2))
    plt.bar(x_halls, y_halls)
    plt.xticks(rotation=75)
    plt.ylabel('Profit')
    plt.title('Profit of hall by hall capacity')
    plt.show()
    print(x_halls, y_halls)


def time_in_queue(statistics):
    y_user = []
    x_user = []
    for i in range(len(statistics)):
        if statistics[i]['bought ticket'] is True:
            y_user.append(int(statistics[i]['ticket buying time'] - statistics[i]['went to cinema']))
            x_user.append(i)
    # plt.plot(x_user, y_user)
    # plt.xlabel('Client')
    # plt.ylabel('Time in queue')
    # plt.grid(b='on')
    # plt.minorticks_on()
    # plt.title('Dependence betweeen time and number of client')
    # plt.show()
    fig, ax = plt.subplots()

    ax.scatter(x_user, y_user,
               c='b')

    ax.set_facecolor('white')  # цвет области Axes
    ax.set_title('Время в очереди')  # заголовок для Axes

    fig.set_figwidth(8)  # ширина и
    fig.set_figheight(8)
    plt.show()


if __name__ == '__main__':
    statistic_values = get_statistics()
    print(statistic_values[200])  # TODO: comment this before commit
    gone = 0
    for i in statistic_values:
        if i['bought ticket'] is False:
            gone += 1
    print(f'gone: {gone}')
    stat_values = take_films_halls_statistics(statistic_values)
    print(f'Average time in queue: {stat_values["average time in queue"]}\n'
          f'Most popular film: {stat_values["most popular film"]}\n'
          f'Amount of clients: {int(stat_values["clients amount"])}\n'
          f'Revenue per day: {stat_values["revenue"]}')
    # bought_tickets_to_film(stat_values)
    # halls_graphics(stat_values)
    # halls_profit_by_capacity(stat_values)
    # time_in_queue(statistic_values)




