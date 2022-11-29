import art
from replit import clear

def add(a, b):
  return a + b

def substract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  return a / b

operations = {
  "+": add,
  "-": substract,
  "*": multiply,
  "/": divide
}


def cal():
  print(art.logo)
  firstNum = float(input("What's the first number?: "))

  for op in operations:
    print(op)

  end_cal = True
  while end_cal:
    operation = input("Pick an operation: ")
    cal_function = operations[operation]
    nextNum = float(input("What's the next number?: "))
    res = cal_function(firstNum, nextNum)
    
    print(f"{firstNum} {operation} {nextNum} = {res}")

    continues = input(f"Type 'y' to continue calculating with {res}, or type 'n' to start a new calculation: ")

    if continues == 'y':
      firstNum = res
    elif continues == 'n':
      end_cal = False
      clear()
      cal()
cal()