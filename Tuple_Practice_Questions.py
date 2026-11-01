# 1. Create a tuple containing five integers
t = (10, 20, 30, 40, 50)
print(t)


# 2. Create a tuple with different data types
t = ("Shivam", 20, 65.5, True)
print(t)


# 3. Create a single-element tuple and verify datatype
t = (10,)
print(t)
print(type(t))


# 4. Print first, middle, and last elements
t = (10, 20, 30, 40, 50)
print(t[0])
print(t[2])
print(t[-1])


# 5. Reverse a tuple using slicing
t = (10, 20, 30, 40, 50)
print(t[::-1])


# 6. Print every second element
t = (10, 20, 30, 40, 50, 60)
print(t[::2])


# 7. Count how many times 25 occurs
t = (25, 10, 25, 30, 25, 40)
print(t.count(25))


# 8. Find the index of a given element
t = (10, 20, 30, 40, 50)
print(t.index(30))


# 9. Calculate sum and average
t = (10, 20, 30, 40, 50)
total = sum(t)
average = total / len(t)
print("Sum:", total)
print("Average:", average)


# 10. Count even and odd numbers
t = (10, 15, 20, 25, 30, 35)
even = 0
odd = 0

for i in t:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even:", even)
print("Odd:", odd)


# 11. Find maximum and minimum values
t = (10, 50, 20, 40, 30)
print("Maximum:", max(t))
print("Minimum:", min(t))


# 12. Check whether a value exists
t = (10, 20, 30, 40, 50)

if 30 in t:
    print("Value exists")
else:
    print("Value does not exist")


# 13. Convert a list into a tuple
lst = [10, 20, 30, 40, 50]
t = tuple(lst)
print(t)


# 14. Unpack a tuple into four variables
t = (10, 20, 30, 40)
a, b, c, d = t
print(a)
print(b)
print(c)
print(d)


# 15. Swap two variables using tuple unpacking
a = 10
b = 20
a, b = b, a
print("a =", a)
print("b =", b)


# 16. Access a value from a nested tuple
t = ((10, 20), (30, 40), (50, 60))
print(t[1][0])


# 17. Remove duplicate values while preserving order
t = (10, 20, 10, 30, 20, 40)
result = tuple(dict.fromkeys(t))
print(result)


# 18. Find the second-largest distinct number
t = (10, 50, 30, 50, 20, 40)
t = sorted(set(t))
print(t[-2])


# 19. Sort a tuple in ascending order
t = (50, 20, 40, 10, 30)
result = tuple(sorted(t))
print(result)


# 20. Create a tuple of student names and marks
students = (
    ("Shivam", 85),
    ("Rahul", 90),
    ("Amit", 80)
)

for name, marks in students:
    print("Name:", name)
    print("Marks:", marks)