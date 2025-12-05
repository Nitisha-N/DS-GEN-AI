#Task The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:

#The first line contains the sum of the two numbers.
#The second line contains the difference of the two numbers (first - second).
#The third line contains the product of the two numbers.




def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
    
a = int(input())
b = int(input())

operations = [add,subtract,multiply]

for op in operations:
    print(op(a,b))
