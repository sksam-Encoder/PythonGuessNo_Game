# Tuples are used to store multiple items in a single variable.
# Tuple is one of 4 built-in data types in Python used to store collections of data
# Tuple items are ordered, unchangeable, and allow duplicate values.


a = (5, 4, 3, 2, 1)
print(type(a))
for i in range(len(a)):
    for j in range(0, 5):
        no = int(input("guess a no"))
        if a[i] < no:
            print("guess smaller than", no)
        elif a[i] > no:
            print("guess greater than", no)
        else:
            print("correct guess you Win the game")
            break
    print("want to leave press 0 if not press 1 /t")
    ch = int(input("enter for leave"))
    if ch == 0:
        break
    else:
        continue
