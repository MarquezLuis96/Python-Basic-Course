#HEADER: Here you will find the necessary values for the program to run
#Values of the currency
value_colombia = 0.000265
value_venezuela = 0.000003215
value_euro = 1.19
value_uk = 1.32

#Welcome - Home
welcome = """
    Welcome to the currency converter 💰💸💲🤑

    Choose an option: 
        1 - Colombian Pesos (COP)
        2 - Venezuelan Bolivars (VES)
        3 - Euros (EUR)
        4 - UK Pound (GBP)

Option: """

#Casting to int
def str_to_int(message):
    message = int(message)
    return message

#Casting to float
def str_to_float(message):
    message = float(message)
    return message

#Casting to str
def x_to_str(message):
    message = str(message)
    return message

def exchange_multiplying(to_currency):
    to_currency = dollars * to_currency
    return round(to_currency, 2)

def exchange_dividing(to_currency):
    to_currency = dollars / to_currency
    return round(to_currency, 2)

#Exchange
def exchange(to_currency):
    return exchange_dividing(to_currency)

#Capturing option value
option = str_to_int(input(welcome))

#Question
def question():
    dollars = str_to_float(input("How many dollars do you have?: $"))
    dollars = round(dollars, 2)
    return dollars

#Selecting/Convertion
if option == 1:
    dollars = question()
    #Colombian Pesos
    colombian_pesos = exchange(value_colombia)
    #Printing
    colombian_pesos = x_to_str(colombian_pesos)
    dollars = x_to_str(dollars)
    print("You have $" + dollars + " USD    ---->   " + colombian_pesos + " COP")
elif option == 2:
    dollars = question()
    #Venezuelan Bolivar
    venezuelan_bolivars = exchange(value_venezuela)
    #Printing
    venezuelan_bolivars = x_to_str(venezuelan_bolivars)
    dollars = x_to_str(dollars)
    print("You have $" + dollars + " USD    ---->   " + venezuelan_bolivars + " VES")
elif option == 3:
    dollars = question()
    #Euros
    euros = exchange(value_euro)
    #Printing
    euros = x_to_str(euros)
    dollars = x_to_str(dollars)
    print("You have $" + dollars + " USD    ---->   " + euros + " EUR")
elif option == 4:
    dollars = question()
    #UK Pounds
    uk_pounds = exchange(value_uk)
    #Printing
    uk_pounds = x_to_str(uk_pounds)
    dollars = x_to_str(dollars)
    print("You have $" + dollars + " USD    ---->   " + uk_pounds + " GBP")
else:
    print("Type a correct option")