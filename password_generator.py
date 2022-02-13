import random as rand

characters = ["1234567890", "abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "!@#$%^&*()-=_+~`[];:'"]

length = int(input("enter password length here: "))

password = ""

for i in range(length):
    char_type = rand.choice([0, 1, 2, 3])

    password += rand.choice(characters[char_type])

print(password)