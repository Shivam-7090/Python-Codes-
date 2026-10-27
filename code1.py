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


# Marks = int(input("Enter your marks: "))
# match Marks:
#     case 85|86|87|88|89|90|91|92|93|94|95|96|97|98|99|100:
#         print("Grade A")
#     case 70|71|72|73|74|75|76|77|78|79:
#         print("Grade B")
#     case 60|61|62|63|64|65|66|67|68|69:
#         print("Grade C")
#     case 35|36|37|38|39|40|41|42|43|44|45|46|47|48|49|50|51|52|53|54|55|56|57|58|59:
#         print("Grade D")
#     case _:
#         print("Grade F")


# A = 25
# B = 30
# operator = input("Enter operator (+, -, *, /): ")
# match operator:
#     case "+":
#         C = A + B
#         print("The sum of A and B is:", C)
#     case "-":
#         C = A - B
#         print("The Subtraction of A and B is:", C)
#     case "*":
#         C = A * B
#         print("The Multiplication of A and B is:", C)
#     case "/":
#         C = A / B
#         print("The quotient of A and B is:", C)


# vowels = input("Enter a string: ")
# match vowels:
#     case "a" | "e" | "i" | "o" | "u":
#         print("The string contains a vowel.")
#     case _:
#         print("The string does not contain a vowel.")



# name = input("Enter your name: ")

# vowels = "aeiou"
# found = []

# for letter in name.lower():
#     if letter in vowels and letter not in found:
#         found.append(letter)

# if found:
#     print("Vowels present in your name:", ", ".join(found))
#     print("Total unique vowels:", len(found))
# else:
#     print("No vowels found in your name.")


# name = input("Enter your name: ")

# for i in "aeiou":
#     if i in name.lower():
#         print(i)