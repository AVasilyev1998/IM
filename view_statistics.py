import pickle


def view():
    with open('sim.pickle', 'rb') as reader:
        data = pickle.load(reader)

    return data


if __name__ == '__main__':
    data = view()
    print(data[120])