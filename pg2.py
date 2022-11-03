class Garage():
    def __init__(self):
        #these are the attributes:
        self.currentTicket = {} #dictionary where we will determine if user has paid 
        self.tickets = [] #List of tickets. key: [License plate number | cost]
        self.parkingSpaces = 10 #spaces still available

    def takeTicket(self):
        # decrease the amount of tickets available by 1  
        # decrease the amount of parkingSpaces available by 1
        if self.parkingSpaces >= 1:
            print(f"There are {self.parkingSpaces} spot(s) available.")
            confirm = input("Would you like to park? (y/n)")
            if confirm.lower() == "y":
                license.plate= input("Enter License Plate number. (This will be your ticket number) : ")
                self.currentTicket[license.plate] = "10"
                self.tickets.append(self.currentTicket)
                self.parkingSpaces -=1
                print("Please take your ticket: ")
                print(self.currentTicket)
            elif confirm.lower() == "n":
                pass
            else:
                print("Invalid choice. Please Try Again.")

    def payForParking(self):
        # display an input that waits for an amount from the user and store it in a variable
        # If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
        # This should update the "currentTicket" dictionary key "paid" to True
        # clear()
        price = 10
        ticket_num = input("What is your ticket number? : ")
        print(self.currentTicket[ticket_num])
        print(f"Your total is ${self.currentTicket[ticket_num]}")
        payment = input("Enter amount (cost is $10) :  ")
        if price >= 1:
            price -= int(payment)
            f"Balance remaining: {price} "
            if price <= 0:
                self.currentTicket[ticket_num] = 0
                self.leaveGarage()
    
    def leaveGarage(self):
        # Update tickets list to increase by 1 (meaning add to the tickets list)
        
        #if

        print("Thank you, have a nice day")
        self.parkingSpaces += 1
        x = input("What is your ticket number? : ")
        for y in range(len(self.tickets)):
            for key, value in self.tickets[y].items():
                if key == x:
                    print(f"'{x}' was removed from the system.")
                    self.tickets.pop(y)

            
        print("Please remember to leave in 15 mins!")


# - - - - - - - - - - - - - - - Main- - - - - - - - - - - - - - - - 
class Main():
    def showInstructions():
        print("""
Welcome to CT Parking
Options:
[1] Park
[2] Pay for parking
[3] Quit
        """)
    def run():
        Main.showInstructions()
        self = Garage()
        while True:
            choice = input("What service would you like? ")
            if choice.lower() == "1":
                self.takeTicket()
            elif choice.lower() == "2":
                self.payForParking()    
            elif choice.lower() == "3":
                clear()
                print("Thank you for being a valued customer at CT Parking! *bow*")
                break
            else:
                print("invalid input... please try again.")
Main.run()

