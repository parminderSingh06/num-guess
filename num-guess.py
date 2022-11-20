import random

def main():
    print("Hello welcome to the Number Guessing game!")
    print("This game will select a random number from 1-100 and you have to guess the number.(Hints will be provided)")
    print(generate())

def generate():
    x = random.uniform(0,100)
    return x

if __name__ == "__main__":
    main()




