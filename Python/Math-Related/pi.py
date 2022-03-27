from mpmath import *
import random as rand

mp.pretty = True
mp.dps = 100
coprimes=0
total=0

def pi(coprimes, total):
    for _ in range(100000):
        r1 = rand.randint(1,1000000000)
        r2 = rand.randint(1,1000000000)

        while(r2):
            r1, r2 = r2, r1 % r2

        total+=1
        if r1 == 1:
            coprimes+=1

    x = mpf(coprimes)/mpf(total)
    print(f"Pi is approx {sqrt(6/x)}")

while True:
    pi(coprimes, total)

    if input("Try again? y/n (will start from last approxamation): ").lower() == 'n':
        break
