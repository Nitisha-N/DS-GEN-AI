#print str

def print_sequence(n):
    result = ""
    for i in range(1,n+1):
        result += str(i)
    print(result)
    
n = int(input())
print_sequence(n)
