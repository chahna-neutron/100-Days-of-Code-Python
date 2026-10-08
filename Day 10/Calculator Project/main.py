import art
print(art.logo)

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}


def calci():
    global first_num
    first_num = float(input("What's the first number?: "))


    calculate=True
    while calculate:


     print("+\n-\n*\n/\n")
     op=input("Pick an operation: ")

     second_num = float(input("What's the second number?: "))
     answer=operations[op](first_num, second_num)
     print(f"{first_num} {op} {second_num} = {answer}")

     decision=input(f"Type 'y' to continue with {answer} or type 'n' to start a new calculation.").lower()
     if decision=="y":
        first_num=answer
     else:
         calculate=False
         print("\n"*100)
         calci()
calci()