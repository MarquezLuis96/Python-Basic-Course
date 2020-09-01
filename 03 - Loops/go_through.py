def ask_name():
    name = input("Write your name: ")
    return name


def go_through(name):
    for i in name:
        print(i)
    print("\n")


def go_Through_(name):
    for i in name:
        print(i.upper())
    
    print("\n")


def run():
    n = ask_name()
    go_through(n)
    go_Through_(n)


if __name__ == "__main__":
    run()