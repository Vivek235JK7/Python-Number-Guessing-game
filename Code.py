import random

choice = random.randint(1, 100)
your_point = 100

print("Starting points:", your_point)

while True:
    guess = int(input("Enter your guess (1-100): "))

    if guess == choice:
        print("You guessed it right!!")
        print("You win 🎉")
        print("Your points left:", your_point)
        break

    your_point -= 10

    if guess > choice:
        print("Too High")
    else:
        print("Too Low")

    print("Your points left:", your_point)

    if your_point == 0:
        print("You lost 💀")
        print("Correct number was:", choice)
        break
