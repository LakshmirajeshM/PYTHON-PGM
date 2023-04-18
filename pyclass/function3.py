def add (value1,value2):
    return int(value1)+int(value2)

def multiply (value1 ,value2):
    return int(value1)*int (value2)

operation = input("enter the operation:")
value1 = input("enter value1 :")
value2 = input("enter value2 :")
if operation == "+":
    answer = add(value1,value2)
    print(answer)
elif operation =="*":
    answer1= multiply(value1,value2)
    print(answer1)
else:
    print("not found")


#answer = add(value1 ,value2)
#answer1 = multiply (value1,value2)
 
 