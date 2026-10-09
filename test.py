import random
num=random.randint(1, 100)
count=0
print("Guess the number between 1 and 100")
guess=int(input("Enter your guess: "))
while True:
    count += 1
    if guess==num:
        print("对.")
        print(f"You guessed the number in {count} attempts.")
        break
    elif guess<num:
        print("小了.")
        guess=int(input("Enter your guess: "))
    else:
        print("大了.")
        guess=int(input("Enter your guess: "))
