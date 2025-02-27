import random


def dice(i):
    roll = random.randint(1, i)
    return roll
i = 0
while i < 10:
    print(dice(6))
    i = i + 1
