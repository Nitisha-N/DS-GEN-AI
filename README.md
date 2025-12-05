# HackerRank Python Solutions

A collection of Python solutions for basic HackerRank problems.  
Each script follows clean coding practices and works with standard input/output as required by HackerRank.

---

## 📚 Table of Contents

1. [Weird or Not Weird](#1-weird-or-not-weird)
2. [Arithmetic Operators](#2-arithmetic-operators)
3. [Division](#3-division-integer--float)
4. [Loops – Print Squares](#4-loops--print-squares)
5. [Leap Year Function](#5-leap-year-function)
6. [Print Sequence Without Spaces](#6-print-sequence-without-spaces)

---

## 1️⃣ Weird or Not Weird
**Link:** https://www.hackerrank.com/challenges/py-if-else/problem

```python
n = int(input())

if n % 2 == 1:
    print("Weird")
else:
    if 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")
2️⃣ Arithmetic Operators
Link: https://www.hackerrank.com/challenges/python-arithmetic-operators/problem

python
Copy code
def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y

a = int(input())
b = int(input())

print(add(a, b))
print(subtract(a, b))
print(multiply(a, b))
3️⃣ Division (Integer & Float)
Link: https://www.hackerrank.com/challenges/python-division/problem

python
Copy code
def integer_division(a, b):
    return a // b

def float_division(a, b):
    return a / b

a = int(input())
b = int(input())

print(integer_division(a, b))
print(float_division(a, b))
4️⃣ Loops – Print Squares
Link: https://www.hackerrank.com/challenges/python-loops/problem

python
Copy code
def print_squares(n):
    for i in range(n):
        print(i * i)

n = int(input())
print_squares(n)
5️⃣ Leap Year Function
Link: https://www.hackerrank.com/challenges/write-a-function/problem

python
Copy code
def is_leap(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

year = int(input())
print(is_leap(year))
6️⃣ Print Sequence Without Spaces
Link: https://www.hackerrank.com/challenges/python-print/problem

python
Copy code
def print_sequence(n):
    result = ""
    for i in range(1, n + 1):
        result += str(i)
    print(result)

n = int(input())
print_sequence(n)
Short alternative:

python
Copy code
n = int(input())
print(*range(1, n + 1), sep="")
▶️ How to Run
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/yourrepo.git
Navigate into the folder:

bash
Copy code
cd yourrepo
Run any Python file:

bash
Copy code
python filename.py
