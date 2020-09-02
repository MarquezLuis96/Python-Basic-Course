def verify(cont):
    if cont == 2:
        return True
    else:
        return False


def console_print(n, fl):
    if fl == True:
        print("The number " + str(n) + " is prime")
    else:
        print("The number " + str(n) + " is not prime")


def div(n):
    cont=0
    for i in range(1, n+1):
        rest = n%i
        if rest == 0:
            cont += 1
        else:
            continue
    
    return verify(cont)


def prime():
    n = cap_number()
    console_print(n, div(n))



def cap_number():
    n = int(input("Write a number to know if it is a prime number or not: "))
    return n


def run():
    prime()


if __name__ == "__main__":
    run()