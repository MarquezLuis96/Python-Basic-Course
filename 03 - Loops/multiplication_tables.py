def table(n):
    for i in range(1,11):
        print(str(i) + "x" + str(n) + "= " + str(i*n))


def opc_cap():
    print(("Write a number between 1 and 10 to print his multiplication table"))
    opc = int(input("Write 110 to print from 1 to 10\nOr write 0 to exit: "))
    return opc
    

def all_t():
    for i in range(1,11):
        table(i)
        print("\n")


def run():
    opc = 1000000
    while opc >= 0:
        opc = opc_cap()
        if opc == 110:
            all_t()
        elif(opc != 0):
            table(opc)
        else:
            print("Bye bye!")
            exit()


if __name__ == '__main__':
    run()