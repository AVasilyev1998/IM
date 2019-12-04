import random


def random_with_chance(chance: int) -> bool:
    """

    :param chance: шанс выпадения 1
    :return: int  1 or 0
    """
    rand = random.randint(0, 100)
    if rand in range(0, chance+1):
        return True
    else:
        return False


if __name__ == '__main__':
    nuls = 0
    ones = 0
    for i in range(10):
        if random_with_chance(20):
            ones += 1
        else:
            nuls += 1
    print(f'nuls: {nuls} | ones: {ones}')
