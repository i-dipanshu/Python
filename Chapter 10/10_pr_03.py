class Sample :
    a = "Class Attributes"

obj = Sample()
# It will not update the class attributes but only override it.
obj.a = "Instance Attributes"
print(obj.a)

# It will update the class attributes.
Sample.a = "Updated Class Attributes"
print(Sample.a)
