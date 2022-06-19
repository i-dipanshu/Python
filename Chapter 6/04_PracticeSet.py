# # Problem 1
# from operator import truediv


# num1 = int(input("Enter number 1: "))
# num2 = int(input("Enter number 2: "))
# num3 = int(input("Enter number 3: "))
# num4 = int(input("Enter number 4: "))
# # Using Nested If
# if num1 > num2:
#     if num1 > num3:
#         if num1 > num4:
#             print("Num1 is greatest.")
# if num2 > num1:
#     if num2 > num3:
#         if num2 > num4:
#             print("Num2 is greatest.")
# if num3 > num2:
#     if num3 > num1:
#         if num3 > num4:
#             print("Num3 is greatest.")
# if num4 > num2:
#     if num4 > num3:
#         if num4 > num1:
#             print("Num4 is greatest.")

# # Using If else ladder
# if num1 > num2 and num1 > num3 and num1 > num4 :
#     print(num1, "is greatest")
# elif num2 > num1 and num2 > num3 and num2 > num4 :
#     print(num2, "is greatest")
# elif num3 > num2 and num3 > num1 and num3 > num4 :
#     print(num3, "is greatest")
# elif num4 > num2 and num4 > num3 and num4 > num1 :
#     print(num4, "is greatest")
# else :
#     print("All of them are equal")

# # Problem 2 
# sub1 = int(input("Enter 1st subject Marks: "))
# sub2 = int(input("Enter 2nd subject Marks: "))
# sub3 = int(input("Enter 3rd subject Marks: "))
# sub4 = int(input("Enter 4th subject Marks: "))

# sum = sub1 + sub2 + sub3

# if sub1 < 33 or sub2 < 33 or sub3 < 33 or sub4 < 33 :
#     print("You've failed because you've less than 33 one of subject.")
# elif sum/4 < 40 :
#     print("You've failed because your %marks is less than 40")
# else :
#     print("Congratulation!, You've passed the exam.")

# # Problem 3
# text = input("Enter the text: ")
# if "make a lot money" in text :
#     spam = True
# elif "buy now" in text:
#     spam = True
# elif "subscribe this" in text:
#     spam = True
# elif "click this" in text:
#     spam = True
# else :
#     spam = False

# if spam :
#     print("This text is spam")
# else :
#     print("This text not spam")

