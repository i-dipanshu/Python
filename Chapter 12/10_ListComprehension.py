a = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# b = []
# for item in a:
#     if item % 2 == 0:
#         b.append(item)
# print(b)

b = [i for i in a if i%2==0]  # shortcut for above function.
print(b)