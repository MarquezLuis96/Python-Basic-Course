#HEADER: Here you will find the necessary values for the program to run
#Values of the currency
value_colombia = 3875
value_venezuela = 311000
value_euro = 1.1847
value_uk = 1.31

#Welcome - Home
welcome = """
    Welcome to the currency converter 💰💸💲🤑

    Choose an option: 
        1 - Colombian Pesos (COP)
        2 - Venezuelan Bolivars (VES)
        3 - Euros (EUR)
        4 - UK Pound (GBP)

Option: 
"""
#Capturing option value
option = int(input(welcome))

#Question
dollars = input("How many dollars do you have?: $")
dollars = float(dollars)

#Selecting/Convertion
if option == 1:
    #Colombian Pesos
    colombian_pesos = dollars * value_colombia
    colombian_pesos = round(colombian_pesos, 2)
    colombian_pesos = str(colombian_pesos)
    #Printing
    dollars = round(dollars, 2)
    dollars = str(dollars)
    print("You have $" + dollars + " USD    ---->   " + colombian_pesos + " COP")
elif option == 2:
    #Venezuelan Bolivar
    venezuelan_bolivars = float(dollars * value_venezuela)
    venezuelan_bolivars = round(venezuelan_bolivars, 2)
    venezuelan_bolivars = str(venezuelan_bolivars)
    #Printing
    dollars = round(dollars, 2)
    dollars = str(dollars)
    print("You have $" + dollars + " USD    ---->   " + venezuelan_bolivars + " VES")
elif option == 3:
    #Euros
    euros = float(dollars / value_euro)
    euros = round(euros, 2)
    euros = str(euros)
    #Printing
    dollars = round(dollars, 2)
    dollars = str(dollars)
    print("You have $" + dollars + " USD    ---->   " + euros + " EUR")
elif option == 4:
    #UK Pounds
    uk_pounds = float(dollars / value_uk)
    uk_pounds = round(uk_pounds, 2)
    uk_pounds = str(uk_pounds)
    #Printing
    dollars = round(dollars, 2)
    dollars = str(dollars)
    print("You have $" + dollars + " USD    ---->   " + uk_pounds + " GBP")
else:
    print("Type a correct option")