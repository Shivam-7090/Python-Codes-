Grade = input("Enter your grade: ")
match Grade:
    case "A":
        print("Excellent work!")
    case "B":
        print("Good job!")
    case "C":
        print("You passed, but need improvement")  
    case "D":
        print("You barely passed, you need to work harder")
    case "F":
        print("You failed, better luck next time")
    case _:
        print("Invalid grade entered. Please enter a valid grade (A, B, C, D, or F)")