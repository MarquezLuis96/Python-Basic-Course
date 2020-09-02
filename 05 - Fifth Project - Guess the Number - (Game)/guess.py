import random


def think():
    rand = random.randint(1, 100)
    return rand


def run():
    rand_n = think()
    typed_n = int(input("Type a number between 1 & 100: "))
    
    while typed_n != rand_n:
        if typed_n < rand_n:
            typed_n = int(input("Try a bigger number: "))
        elif typed_n > rand_n:
            typed_n = int(input("Try a smaller number: "))
    
    print("Congratulations! You Win\nThe number was :" + str(rand_n))


if __name__ == "__main__":
    run()