# Some Python Notes 🐍
## `range()`
The `range()` method just merely genrates an arithmatic progression. It inherently has nothing to do with `for` loops. 
```
range(begin_with, go_until, common_difference )
```
## Deep copy vs Shallow copy 
- A shallow copy constructs a new compound object and then (to the extent possible) inserts references into it to the objects found in the original.

- A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original.

## `else` in loops 
The `break` statement, like in C, breaks out of the innermost enclosing `for` or `while` loop.

Loop statements may have an `else` clause; it is executed when the loop terminates through exhaustion of the iterable (with for) or when the condition becomes false (with while),**but not when the loop is terminated by a break statement.**

```py
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
```

## `match` statements 
A `match` statement takes an expression and compares its value to successive patterns given as one or more case blocks. This is superficially similar to a switch statement in C, Java or JavaScript (and many other languages), but it can also extract components (sequence elements or object attributes) from the value into variables.
```py
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
```
## Functions and procedures 
Generally functional block of code without a `return` statement is called a *procedure* and with one is called a *function*. 

But, in python, even functions without a `return` statement do return a value, albeit a rather boring one. This value is called `None` (it’s a built-in name). Writing the value `None` is normally suppressed by the interpreter if it would be the only value written.

## Default values in function parameters 
The default values are *evaluated at the point of function definition* in the defining scope, so that: 
```py 
i = 5

def f(arg=i):
    print(arg)

i = 6
f() #prints 5
```
>**Important warning**: The default value is evaluated only once. This makes a difference when the default is a mutable object such as a list, dictionary, or instances of most classes. For example, the following function accumulates the arguments passed to it on subsequent calls:
```py 
def f(a, L=[]):
    L.append(a)
    return L

print(f(1)) # [1]
print(f(2)) # [1,2]
print(f(3)) # [1,2,3]
``` 
If you don’t want the default to be shared between subsequent calls, you can write the function like this instead:

```py
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
```
## Some λ-Calculus with python! 

Let's say we want to make a list of squares. We can do it like this: 
```py 
squares = []
for x in range(10): 
    squares.append(x**2)
print(squares) 
```
But this is a rather noob way of doing what can be elegantly done with some λ-calculus! 
The function expression for a square would be -> `λ x.x^2`
So we can rewite the above piece of code like this: 
```py
squares(map(lambda x:x**2, range(10))) 
```
or we can do: 
```py 
squares(x**2 for x in range(10))
```
Both of these ways are good for avoiding side effects as in the first method we are overwriting the vaiable `x`, and even after the loop ends, the variable still exists! 

> Read: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions

## Tuple Unpacking 📤
```py 
myTuple = 'hello', 'world', 'hola' #packing
x, y, z = myTuple #unpacking 
print(x) # 'hello' 
print(y) # 'world' 
print(z) # 'hola' 
```

## The Walrus 🦭 Opearator `:=` 
Basically overglorified assignment operator for expressions that was added with v3.8

## Executing modules as scripts 
Interetsting read: https://docs.python.org/3/tutorial/modules.html#executing-modules-as-scripts

## Errors and Exxceptions 
Read through when needed: https://docs.python.org/3/tutorial/errors.html
Basically -> 
- `SyntaxError`: When you type some shit code and the interpreter detects it 
- `Exeption`: Detected when your code actually runs. Stuff like `ZeroDivisionError`, `TypeError`. You can program your scrip to handle and raise exceptions. 
- 