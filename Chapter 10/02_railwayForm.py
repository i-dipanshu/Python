class RailwayForm:
    formtype = "RailwayForm"
    # Declaring a method to print data
    def printData(self):
        print(f"Name is {self.name}.\nTrain is {self.train}")
        print(f"Age is {self.age}.\nPin is {self.pin}")
        print(f"Preference is {self.pref}.")


# Object instantiation
passengerApplication = RailwayForm()
# Adding Data to the Form 
passengerApplication.name = 'Sanjiv'
passengerApplication.age = 34
passengerApplication.train = 'Garib Rath'
passengerApplication.pin =  848207
passengerApplication.pref ='Lower'
passengerApplication.printData() # Method call using object