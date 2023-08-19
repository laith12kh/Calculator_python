logo = """
  .----------------.  .----------------.  .----------------.  .----------------. 
 | | .--------------. || .--------------. || .--------------. || .--------------. |
   | |     ______   | || |      __      | || |   _____      | || |     ______   | |
 | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
 | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
 | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
 | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
 | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
 | | |              | || |              | || |              | || |              | |
 | | '--------------' || '--------------' || '--------------' || '--------------' |
 |  '----------------'  '----------------'  '----------------'  '----------------'


"""
print(logo)

# add function
def add(first,second):
    return first + second

#sub function
def subtract(first,second):
    return first - second

#mult function
def multiply(first,second):
    return first * second

#div function 
def divide(first,second):
    return first / second

# the dict of the operations
operations_dict = { "+" : add , "-" : subtract , "*" : multiply , "/" : divide }

# we need to recive 2 numbers and the operation bettwen them

firstNum = int(input("What is the first number\t"))
secondNum = int(input("What is the second number\t"))
operation = input("What operation you want to calculate\t")

calc_func = operations_dict[operation]
total = calc_func(firstNum,secondNum)

print(f"{firstNum} {operation} {secondNum} = {total}")