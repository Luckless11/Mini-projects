import random as rand
import string

length = int(input("enter password length here: "))

password = ""

for _ in range(length):
    password += rand.choice(string.ascii_letters + string.digits + string.punctuation)

print(password)