
import random

print("Welcome to the program to generate random number generator. Enjoy!!!")
min = int(input("Write minimal number for number generator: "))
max = int(input("Write maximal number for number generator: "))
random_number = random.randint(min, max)
print(random_number)
