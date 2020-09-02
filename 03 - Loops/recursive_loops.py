def run(n, to):
    raised_to = n
    if raised_to == 0:
        raised_to += 1
        run(raised_to, to)
    elif raised_to <= to:
        n = str(n)
        print('' + n + '\n')
        raised_to = raised_to * 2
        run(raised_to, to)


if __name__ == '__main__':
    print("Printing powers of 2 up to 1000")
    run(0, int(input("Type an power 2 aproximation: ")))