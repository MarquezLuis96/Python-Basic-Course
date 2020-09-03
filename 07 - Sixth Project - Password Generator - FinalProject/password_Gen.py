import random


def generate():
    caps = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    mins = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    symb = ['+','-','*','/','#','.','_','-',',','@','&','$','(',')','[',']','{','}']
    numb = ['0','1','2','3','4','5','6','7','8','9']

    chars = caps + mins + symb + numb
    passw = []
    for i in range(15):
        char_rand = random.choice(chars)
        passw.append(char_rand)
    
    passw = ''.join(passw)
    return passw


def run():
    password = generate()
    print("Your new password is: " + password)


if __name__ == "__main__":
    run()