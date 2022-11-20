import random


def main():
    print("Hello welcome to the Number Guessing game!")
    print("This game will select a random number from 1-100 and you have to guess the number.(Hints will be provided)")
    choice = input("\nSelect Difficulty: (Easy   Medium   Hard   Impossible): ")
    diffOption = {'easy': 10, 'medium': 8,'hard': 5, 'impossible': 3}
    lives = diffOption[choice.lower()]
    print("You have "+ str(lives) +" lives based on your difficulty selection.")
    answer = random.uniform(0,100)
    answer = int(answer)
    while True:
       lives = play(answer,lives)
       if lives == 0:
           print("Game Over! You ran out of lives.")
           quit()
    

def play(a,b):
    x = input("Number Choice:")
    x = int(x)
    if x == a:
        print("Correct you won with " + str(b) + " lives left!")
        quit()
    elif x > a:
        b = b - 1
        print("Lives Left:" + str(b))
        print("The number you entered is incorrect try guessing lower.")
        return b
    elif x < a:
        b = b - 1
        print("Lives Left:" + str(b))
        print("The number you entered is incorrect try guessing higher.")
        return b
        


if __name__ == "__main__":
    main()




