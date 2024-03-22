import random
secert_num = random.randint(0, 100)
attempts = 0

while True:
    guess = int(input("Guess the number between 1 to 100:"))
    attempts += 1
    if guess == secert_num:
        print("Congrats! You guess the number", secert_num, "correctly in attempts", attempts)
        break
    difference = abs(secert_num - guess)
    if difference > 10:
        print("Too", "High" if secert_num > guess else "Low")
    elif difference <= 5:
        print("Close but", "High" if secert_num > guess else "Low")
    else:
        print("Not to far, but", "High" if secert_num > guess else "Low")


