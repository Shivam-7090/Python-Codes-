A = 25
B = 30
operator = input("Enter operator (+, -, *, /): ")
match operator:
    case "+":
        C = A + B
        print("The sum of A and B is:", C)
    case "-":
        C = A - B
        print("The Subtraction of A and B is:", C)
    case "*":
        C = A * B
        print("The Multiplication of A and B is:", C)
    case "/":
        C = A / B
        print("The quotient of A and B is:", C)