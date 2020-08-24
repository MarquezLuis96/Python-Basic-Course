def palindrome(word):
    word = word.replace(" ", "")
    word = word.lower()
    inverse_word = word[::-1]

    if word == inverse_word:
        return True
    else:
        return False



def run():
    word = input("Write a word to find out if that word is palindrome:\n")
    is_palindrome = palindrome(word)
    if is_palindrome == True:
        print("The word is a palindrome word")
    else:
        print("The word isn't a palindrome word")


if __name__ == '__main__':
    run()