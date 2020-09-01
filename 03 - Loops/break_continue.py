MAX = 1000000


def all_to(n):
    for i in range(MAX):
        if i == n+1:
            break
        else:
            print(i)


def even(n):
    for i in range(n+1):
        if i % 2 == 0:
            print(i)
        else:
            continue


def odd(n):
    for i in range(n+1):
        if i % 2 == 0:
            continue
        else:
            print(i)


def question():
    obj = int(input("Print:\n1)Even to n\n2)Odd to n\n3)All to n\n"))
    return obj


def question2():
    obj = int(input("Type n= "))
    return obj


def election(op, n):
    if op == 1:
        even(n)
    elif op == 2:
        odd(n)
    else:
        all_to(n)


def cut_to_O():
    string= input("Write a String:\n->")
    to = input("Write a letter to which you want to cut the string: ")

    for letter in string:
        if letter == to:
            break
        else:
            print(letter)


def run():
    opc = question()
    n = question2()
    election(opc,n)
    cut_to_O()



if __name__ == "__main__":
    run()