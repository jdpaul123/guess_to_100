#Guessing number game
print("Welcome to Guess the Secret Number. Guess a number between 1 to 100. You have 10 guesses!")
import random
num_to_guess = random.randint(1, 100)
iterate = 10
answer_list = [ ]


for i in range(iterate):
    
    answer = input("Please guess a number: ")
    answer = int(answer)
    answer_list.append(answer)
    seen = set()
    if answer > num_to_guess:
        print("Too big - try a smaller number")
    if answer == num_to_guess:
        print("Correct you won in ", i+1 , " guesses")
        print(answer_list)
        break
    if answer < num_to_guess:
        print("Too small - try a bigger number")
