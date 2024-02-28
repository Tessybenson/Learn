from operations import Addition, Minus

def Calculator():
    number_1 = input("what is the first number? ")
    number_2 = input("what is the second number? ")

    Anything = int(number_1)
    Samename = int(number_2)

    Additionresults = Addition(Anything, Samename)
    Minusresults = Minus(Anything, Samename)

    print(f"the Addition is {Additionresults}")
    print(f"the Minus is {Minusresults}")

Calculator()

