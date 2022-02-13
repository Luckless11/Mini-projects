import random as rand

numbers = "1234567890"
letters = "abcdefghijklmnopqrstuvwxyz"
symbols = "!@#$%^&*()-=_+~`[];:'"

length = int(input("enter password length here: "))

password = ""

for i in range(length):
    char = rand.choice([numbers, letters, symbols])

    password += rand.choice(char)

print(password)