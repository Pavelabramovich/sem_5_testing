import random
from main_decorator import main


@main
def main():
    print("Hello, world!")
    print("Andhiagain!")
    print('!' * random.randint(5, 50))


