class ChangeAttr:
    id = 43
    # Changing value of class attributes by dunder method
    def changevalue1(self,cng):
        self.__class__.id = cng
    # Changing value of class attributes by class method
    
    @classmethod  # Class decorator
    def changeValue2(cls, cng):
        cls.id = cng

num = ChangeAttr()
print(num.id)

# Calling to change value of class attribute
num.changevalue1(455)
print(num.id)

num.changeValue2(433)
print(num.id)