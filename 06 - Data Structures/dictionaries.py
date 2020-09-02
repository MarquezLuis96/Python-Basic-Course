def fx():
    dictionary = {
        'key1':1,
        'key2':2,
        'key3':3,
    }

    print(dictionary['key1'])



def countries():
    population = {
        'Argentina': 44938712,
        'Venezuela': 28067000,
        'Mexico': 132820000,
        'Brazil': 209500000,
        'Uruguay': 3487000,
    }

    for country in population.keys():
        print(country)


def countries_and_pop():
    population = {
        'Argentina': 44938712,
        'Venezuela': 28067000,
        'Mexico': 132820000,
        'Brazil': 209500000,
        'Uruguay': 3487000,
    }

    for country, popu in population.items():
        print(country + " : " + str(popu) + " people")


def run():
    countries_and_pop()


if __name__ == "__main__":
    run()