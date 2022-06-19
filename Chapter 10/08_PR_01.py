class Programmer:
    company = 'Microsoft'
    def __init__(self, Name, Product):
        self.name = Name
        self.product = Product
    def getInfo(self):
        print(f"Name = {self.name}\nProduct = {self.product}\nCompany = {self.company}\n")

Maya = Programmer("Maya", "Skype")
Victor = Programmer("Victor", "GitHUb")
Maya.getInfo()
Victor.getInfo()

        