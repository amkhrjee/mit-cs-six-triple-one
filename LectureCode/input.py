# num = int(input("Type a number..."))
# print(num*5)

# by default python takes all user inputs as string

# bad legend of zelda bootleg ->

count = 1
while count >= 1:
    n = input(
        "You are in the forest\n 🌳🌳🌳🌳🌳🌳\n🌳🌳🌳🌳🌳🌳\n 😦 \n 🌳🌳🌳🌳🌳\n🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳\n Go left or right? ")
    while(n == "right" or n == "Right"):
        if(count > 2):
            n = input(
                "You are in the forest\n 🌳🌳🌳🌳🌳🌳\n🌳🌳🌳🌳🌳🌳\n🥶🥶 \n 🌳🌳🌳🌳🌳\n🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳\n Go left or right? ")
        else:
            n = input(
                "You are in the forest\n 🌳🌳🌳🌳🌳🌳\n🌳🌳🌳🌳🌳🌳\n😭😭 \n 🌳🌳🌳🌳🌳\n🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳\n Go left or right? ")
        count += 1
    else:
        print("You are out of the forest 🎉")
    count += 1
