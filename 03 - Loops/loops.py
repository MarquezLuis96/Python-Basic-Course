#cont = 0
#
#print("(2)^(" + str(cont) + ") = " + str(2**cont))
LIMIT = 1000


def power_2():
    cont = 0
    powr_2 = 2**cont
    while powr_2 < LIMIT:
        print("(2)^(" + str(cont) + ") = " + str(powr_2) + "\n")
        cont = cont + 1
        powr_2 = cont**2


def run():
    power_2()


if __name__ == '__main__':
    run()