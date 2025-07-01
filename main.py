# building an calculator
try:
    a = int(input("Enter the First number:"))
    b = int(input("Enter the Second number:"))

    print("What kind of operation do you want to perform. Press + for an additon\nPress - for subtraction\nPress / for division\nPress * for an Multiplication")


    o = input("Enter Operation: ")
    match o:
        case "+":
            print(f"The result is {a + b}")
        case "-":
            print(f"The result is {a - b}")
        case "/":
            print(f"The result is {a / b}")
        case "*":
            print(f"The result is {a * b}")
        case default:
            print(f"There is an Error")


except Exception as e:
    print("Enter an valid value of a and b")

