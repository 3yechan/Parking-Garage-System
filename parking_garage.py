#ticketing machingat the beginning, prob like $10, system in the works
# if module == 0: #if parking lot is full. 10/10 spots available
#     print("Parking Lot is full.") 
#     break

# if valet.spot full: 
#     print("All parking spaces have been taken, \n> all parking spots have been taken")

from unicodedata import name
from IPython.display import clear_output

# valet
# basic
# leave garage
# pay ticket


class Garage(): 
    def __init__(self):
        self.dict = {}
        self.spots = 10 
        self.valetspots = 8
        self.money = []

    def valet():
            if self.valetspots >= 0:
                print(f"There are still {self.valetspots} spots available for valet service")
                service_type_v = (input("Which service would you like? (Valet/ Premium Valet: "))
                if service_type_v.lower().strip() == "valet" and self.valetspots >= 0 and self.valetspots <=8:
                    self.valetspots -= 1
                    self.variable['name'] = [service_type_v]
                elif service_type_v.lower().strip() == "premium valet" and self.valetspots >= 1 and self.valetspots <=8:
                    self.valetspots -= 1
                    self.variable['name'] = [service_type_v]
                else:
                    print("Invalid choice. Please Try Again.")
            elif self.valetspots == 0:
                print(f'There are no more Valet spots available. Please see Basic spot availability.')
                
    def basic(): 
        clear()
        cost = 0
    
        if self.spots > 0:
            print(f"There are still {self.spots} spots available")
            service_type = input("Which service would you like? (basic/ valet) ")
            if service_type.lower().strip() == "basic" and self.spots >= 0 and self.spots <= 10:
                self.spots -= 1
                self.variable['name'] = [service_type]
                cost += 10
            elif service_type.lower().strip() == "valet":
                self.valet()
            else:
                print("Invalid choice. Please Try Again.")
        elif self.spots == 0:
            print(f"There are no more Basic spots available. Sorry!")

    def LeaveGarage():
        clear()
        cost = {} #access from variable dict should we delete lines 58 through 60?
        exit_response = input("Which service did you use? (Basic/ Valet/ Premium Valet: ") 
        response = input("What was your ticket number?: ")
        for name, dict in variable.item():
            if name == response: #reference dictionary
                if paid == True:
                    self.LeaveGarage()
                else:
                    print("Pay your ticket cost")
                if valet == True:
                    cost +=10
        # quantity = f'{self.spots}, {self.valetspots}
        if exit_response.lower().strip() == "Basic":
            self.spots += 1
            print("10 dollas")
        elif exit_response.lower().strip() == "Valet":
            self.valetspots += 1
            print("12 dollas")
        elif exit_response.lower().strip() == "Premium":
            self.valetspots += 1
            print("15 dollaz baby") 
        else: 
            print("That's not one of the options. Please Try Again")

    def pay_ticket():
        clear()
        balance = self.dict(name[1])
        input("Please pay" {self.dict(name[1])}:)
        if input >= balance:
            balance -= input
            if balance <= 0:
                print("Thanks for paying!")
                print("Thank you for choosing CT Parking")
                print("Please remember to leave in 15 mins")
        elif input < balance:
            balance -= input
            if balance > 0:
                f"Your balance remaining is {balance}"
                input("Please pay remaining balance:")

    def Admin(self):
        money = []
        money = cost #access from dict
        money_for_the_day = sum(money)  
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -      
class Main():
    def showInstructions():                              
        print("""
Welcome to CT Parking
Options:
[1] Basic - $10
[2] Valet - $12
[3] Premium Valet (includes CarWash) = $15
[4] Admin Functions
[5] Quit
        """)

    def run():
        Main.showInstructions()
        my_car = Garage()

        while True:
            choice = input("What service would you like")
            if choice == '1':
                if self.dict == {}:
                    print("Selected: Basic")
                    print("Thank you for choosing CT Parking)
                    self.dict.add(["basic": 10])
                    pass
            elif choice == '2':
                if self.dict == {}:
                    print("Selected: Valet")
                    print("Thank you for choosing CT Parking)
                    self.dict.add(["valet": 12])
            elif choice == '3':
                if my_cart.items == {}:
                    print("Selected: Premium Valet")
                    print("Thank you for choosing CT Parking)
                    self.dict.add(["premium valet": 15])
            elif choice == '4':
                    input("Enter password: ")
                    f"Today you made {self.money}"
            elif choice == '5':
                    my_car.pay_ticket
            else:
                print("invalid input... please try again.")




#-------------------------------------------SCRATCH CODE ------------------------------------------------

    #def Dict():

    # B8= dict()
    # B8[basic] = 10
    # B8[valet] = 12
    # B8[premium] = 15

    

    # self.variable = ()
    # self.spots = ()
    # self.valetspots = ()

#----------------------------------------Reference Code from Shopping List Example------------------------
 
        #     discard = input("What would you like to discard?")
        # quantity = int(input("How many would you like to remove?"))
        # try:
        #     self.items[discard] -= quantity
        #     if self.items[discard] <= 0:
        #         del self.items[discard]
        #     print(f'{quantity} {discard}(s) have been removed.')
        # except:
        #     print(f'{discard} was not in your cart!')
        # self.show()    
#----------------------------------------Reference Code from Shopping List Example------------------------
 
 # type = int(input(f'How many {new_item}(s) do you want to add? (insert number).'))
        # if new_item not in self.items.keys():
        #     self.items[new_item] = quantity
        # else:
        #     self.items[new_items] += quantity
        # print(f'{quantity} {new_item}(s) is/are in the cart.')


        # quantity = type
        # if quantity.lower() == "basic":
        #     #value in dict = price 
        # elif quantity.lower() == "valet":
        #     #value in dict = price 
        # elif quantity.lower() == "premium":
        #     #value in dict = price 

# - - - - - - - - - - - - - - MO Reference Code - - - - - - - - - - - - - - - - - - - - - - - - 
# #control flow
# class Main:
#     def print_landing():
#     print_landing() = Garage()
#         print("""
# Welcome to Chris & Teddie's Parking Garage~
# Options:
# [1] Basic - $10
# [2] Valet - $12
# [3] Premium Valet (includes CarWash) = $15
# [4] Quit
# [5] Admin Functions
#         """)
#     if option = 5:
#         input("Enter password: ")
#         f"Today you made {self.money}"

# def showInstructions():
#         print("""
#         Welcome to ALDI alliance!
#         Options:
#         [1] Show Current Cart
#         [2] Add Item
#         [3] Remove Item
#         [4] Quit
#         [5] Show  Instructions
#         """)

#     def print_landing(): # this is our valet/basic 
#     print_landing() = Garage()
#         print_landing()
#         while True:
#             choice = input("What would you like to do? ")
#             if choice == '1':
#                 if my_cart.items == {}:
#                     print('Your cart is empty... start shopping')
#                 else:
#                     my_cart.show()
#             elif choice == '2':
#                 my_cart.add()
#             elif choice == '3':
#                 if my_cart.items == {}:
#                     print('your cart is empty... add something before you remove it')
#                 else:
#                     my_cart.remove()
#             elif choice == '4':
#                 my_cart.checkout()
#                 break

#             elif choice == '5':
#                 Main.showInstructions()

#             else:
#                 print("invalid input... please try again.")




#   while True:
#             choice = input("What would you like to do? ")
#             if choice == '1':
#                 if my_cart.items == {}:
#                     print('Your cart is empty... start shopping')
#                 else:
#                     my_cart.show()
#             elif choice == '2':
#                 my_cart.add()
#             elif choice == '3':
#                 if my_cart.items == {}:
#                     print('your cart is empty... add something before you remove it')
#                 else:
#                     my_cart.remove()
#             elif choice == '4':
#                 my_cart.checkout()
#                 break
#             elif choice == '5':
#                 Main.showInstructions()
#             else:
#                 print("invalid input... please try again.")
