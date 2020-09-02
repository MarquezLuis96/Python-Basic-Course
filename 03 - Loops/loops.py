#cont = 0
#
#print("(2)^(" + str(cont) + ") = " + str(2**cont))
LIMIT = 1000


def power_2(cycles):
    cont = 0
    while cont < cycles:
        print("(2)^(" + str(cont) + ") = " + str(2**cont))
        cont += 1


def run():
    cycles = int(input("Type the number of cycles you want to do: "))
    power_2(cycles)


if __name__ == '__main__':
    run()