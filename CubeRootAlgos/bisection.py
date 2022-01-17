cube = 27000
epsilon = 0.01
low = 0
high = cube
num_guess = 0
guess = (high + low)/2.0
while abs(guess**3 - cube) >= epsilon:
    if guess**3 > cube:
        high = guess
    else:
        low = guess
    guess = (high + low)/2.0
    num_guess += 1
print("Number of guess =", num_guess)
print(guess, "is close to the cube root of", cube)
