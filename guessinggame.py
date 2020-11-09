import random


def get_integer(prompt):
    """
    Gets an integer from Standard Input (stdin).
    The function will continue looping, and prompting
    the user, until a valid `int` is entered.

    :param prompt: The String that the user will see, when
        they are prompted to enter the value.
    :return: The integer that the user enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        # else: as soon as the return statement is triggered the while loop will be exited
        print("{} is not a valid number".format(temp))


# help(get_integer)

highest = 1000
answer = random.randint(1, highest)
# print(answer)  # TODO: Remove after testing

print("Please guess number between 1 and {}: ".format(highest))
guess = get_integer(": ")

while guess < 1 or guess > highest:
    print("Invalid number! Please guess a number between 1 and {}: ".format(highest))
    guess = get_integer(": ")
if guess == answer:
    print("You got it first time!")
while guess != answer:
    if guess < answer:
        print("Please guess higher!")
        guess = get_integer(": ")
        continue
    elif guess > answer:
        print("Please guess lower!")
        guess = get_integer(": ")
        continue

print("You got it right!")


