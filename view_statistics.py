import pickle
import matplotlib.pyplot as plt


def get_statistics():
    with open('sim.pickle', 'rb') as reader:
        data = pickle.load(reader)

    return data


def take_films_halls_statistics(statistic: dict) -> dict:
    statistic_vals = {'films': {}, 'halls': {}, 'average time in queue': 0, 'clients amount': 0, 'revenue': 0, 'gone': 0}
    for i in range(len(statistic)):
        # revenue and clients amount
        if statistic[i]['bought ticket']:
            statistic_vals["revenue"] += statistic[i]['spend money']
            statistic_vals['clients amount'] += 1
        else:
            statistic_vals['gone'] += 1
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
        y_halls.append(round(v['count'], 2))
    explode = [ 0.04 for i in range(len(stat_dict[hall_cat].items()))]
    plt.pie(y_halls, labels=x_halls, explode=explode,
            shadow=True, autopct='%1.1f%%')
    plt.xticks(rotation=75)
    plt.title('Halls visiting')
    plt.show()
    print(y_halls)
    print(x_halls)
    sum = 0
    for i in y_halls:
        sum += i
    print( y_halls[0] / sum * 100)

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
    # print(x_halls, y_halls)


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
    ax.set_title('Time in queue')  # заголовок для Axes

    fig.set_figwidth(8)
    fig.set_figheight(8)
    plt.show()


def free_sits_on_session(statistics):
    halls = statistics[0]['schedule'].queues
    halls_x = []
    halls_y = []
    for hall in halls:
        name = hall[0].hall_name

        for ses in hall:
            # print(ses)
            halls_x.append(f'{ses.start_time} | hall {name} | capacity: {ses.capacity}')
            halls_y.append(ses.free_sits)
    fig = plt.figure(figsize=(8, 6))
    plt.bar(halls_x, halls_y)
    plt.xticks(rotation=90)
    plt.ylabel('Free sits')
    plt.title('Free sits on sessions')
    plt.show()


if __name__ == '__main__':
    statistic_values = get_statistics()
    stat_values = take_films_halls_statistics(statistic_values)
    # print(stat_values)
    print(f'Average time in queue: {stat_values["average time in queue"]}\n'
          f'Most popular film: {stat_values["most popular film"]}\n'
          f'Amount of clients: {int(stat_values["clients amount"])}\n'
          f'Revenue per day: {stat_values["revenue"]}\n'
          f'Gone clients: {stat_values["gone"]}')
    bought_tickets_to_film(stat_values)
    halls_graphics(stat_values)
    halls_profit_by_capacity(stat_values)
    time_in_queue(statistic_values)
    free_sits_on_session(statistic_values)



