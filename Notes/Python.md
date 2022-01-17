# Some Python Notes 🐍
## `range()`
The `range()` method just merely genrates an arithmatic progression. It inherently has nothing to do with `for` loops. 
```
range(begin_with, go_until, common_difference )
```
## Deep copy vs Shallow copy 
-A shallow copy constructs a new compound object and then (to the extent possible) inserts references into it to the objects found in the original.

-A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original.

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