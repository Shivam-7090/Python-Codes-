input_year = int(input("Enter a year: "))

if (input_year % 400 == 0):
    print("Leap Year")
elif (input_year % 100 == 0):
    print("Not a Leap Year")
elif (input_year % 4 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")