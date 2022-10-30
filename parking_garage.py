class Garage():
    def __init__(self):
        self.dict = {}
        self.spots = 10
        self.valetspots = 8
        self.money = []
    def valet(self):
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
    def basic(self):
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
    def leave_garage(self):
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
    def pay_ticket(self):
        clear()
        balance = self.dict(name[1])
        input(f"Please pay {balance}: ")
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
    def admin(self):
        money = []
        money = cost #access from dict
        money_for_the_day = sum(money)
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Main():
    def showInstructions():
        print("""
Welcome to CT Parking
Options:
[basic] -  Basic: $10
[valet] - Valet: $12
[premium] - Premium Valet (includes CarWash): $15
[admin] - Admin Functions
[quit] - Quit
        """)
    def run():
        Main.showInstructions()
        self = Garage()
        while True:
            choice = input("What service would you like? ")
            if choice.lower() == 'basic':
                print("Selected: Basic")
                print("Thank you for choosing CT Parking")
                self.dict.update( {"basic": 10} )
                print( "Total parking cost is $10. Pay before leaving.")
                pass
            elif choice.lower() == 'valet':
                print("Selected: Valet")
                print("Thank you for choosing CT Parking")
                self.dict.update( {"valet": 12})
                print( "Total parking cost is $12. Pay before leaving.")

            elif choice.lower() == 'premium':
                print("Selected: Premium Valet")
                print("Thank you for choosing CT Parking")
                self.dict.update( {"premium valet": 15} )
                print( "Total parking cost is $15. Pay before leaving.")
            elif choice.lower() == 'admin':
                input("Enter password: ")
                f"Today you made {self.money} dollars"
            elif choice.lower == 'quit':
                print("Thank you for being a valued customer at CT Parking! *bow*")
                print()

                break
            else:
                print("invalid input... please try again.")
Main.run()























