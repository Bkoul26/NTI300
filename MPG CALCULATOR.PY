#Bogdan.Koul
#3/11/19
#This program, remembers vehicle specs, calcualtes MPG and total of refueling and displays all specs along with an option to fill up the gast tank at the price of $2.78 per gallon
#Declarations:
input("Hi, to run application press any key\n") #starting program by getting user input of any key
#--------------------------------------
#======================================
#=================MAIN=================
#=================MAIN=================
def main():
    answer =1
    Car = 0
    Type =0
    Engine = 0
    CarColor = 0
    Distance = 0
    MPG = 0
    Gallons = 0
    GAS =0
    Total = 0
#------------------------------------------------
#==============MODULAR/INPUT=====================
Car = (input("What make of car do you drive?\n")) #Creates input for car make
Type = (input("What type of car is it?\n")) #Creates input for type of car
Engine = float(input("What size of engine in L?\n")) #Input for engine size in Liters
CarColor = (input("Color?\n"))#Allows user input car color
Distance = float(input("Plese type in miles traveled\n"))#float input used for decimal notations of distance traveled 
Gallons = float(input("Please type in gallons used?\n"))#float in put used for decimal measurement of number of gallons of gas used
MPG = Distance / Gallons ## function calculates MPG
GAS = 2.78 * Gallons ##function calcualates amount of $ dollars one needs to spend with the current volume of tank to fill it up fully
#=================================================
#-------------------------------------------------
#=================================================
print("Your vehicle of make", Car, "\nof model", Type,"\n Has engine size of",Engine,"L,\n The car is of color",CarColor,"\nThe Mpg for your car is\n", MPG)#prints/outputs car make, type, engine in Liters, color, miles traveled and the calculation is displayed
answer = int(input("Fill up full tank at $2.78 per gallon?\n, 1 for yes 0 for no\n"))
if  answer == 1: # conditional if statement that allows user to choose whether he/she wants to fuel up their tank at a certain price per gallon
    print("The total cost for gas is\n $", GAS, "\n for", Gallons, "gallons at the price of $2.78 per gallon\nThank you for using my Accounting/ MPG/ GAS application\n")

#end main()
