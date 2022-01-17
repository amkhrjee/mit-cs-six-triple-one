cube = 125000
guess = 0
epsilon = 0.1
increment = 0.01
num_guess = 0

while abs(guess**3 - cube) >= epsilon and guess <= cube:
    guess += increment
    num_guess += 1
print("number of guesses", num_guess)
if abs(guess**3 - cube) >= epsilon:
    print("Failed find a cube root for", cube)
else:
    print(guess, "is the closest cube root of", cube)
