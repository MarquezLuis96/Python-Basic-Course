#Entering age
age = int(input("Write your age: "))

#Checking if the person is of legal age
if (age >= 18):
    print("You're of age\n")
else:
    print("You're under the age allowed\n")

#Learning how to use elif:
number = int(input("Write a number to know if it is ||>5|| , ||<5|| or ||=5||: "))

if(number == 5):
    print("The number is five\n")
elif number >5:
    print("The number is greater than five\n")
else:
    print("Yhe number is lower than five\n")