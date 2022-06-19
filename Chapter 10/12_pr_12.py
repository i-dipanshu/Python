class Train:
    def __init__(self, name, seats, fare):
        self.name = name
        self.seats = seats
        self.fare = fare

    def getStatus(self):
        print("****************")
        print(f"The name of train is {self.name}.")
        print(f"The number seats in train is {self.seats}.")
        print("****************")

    def getFareInfo(self):
        print(f"The fare is {self.fare}")

    def bookTicket(self):
        if self.seats > 0 :
            print(f"Your ticket has been booked! Your seat number is {self.seats}.") 
            self.seats -= 1
        else:
            print(f"The train is full.\nKindly try in Tatkal Kota.")

    def cancelTicket(self):
        pass

intercity = Train("Intercity Express", 1000, 'Rs 120')
intercity.getStatus()
intercity.getFareInfo()
# Call method to book ticket.
intercity.bookTicket()
intercity.getStatus()

