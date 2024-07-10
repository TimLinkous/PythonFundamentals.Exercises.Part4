from random import randrange

def give_me_a_num():
    #print("Give a number between 1 and 10\n")
    player_num = input("Give a number between 1 and 10\n")
    return int(player_num)

def random_num():
    return randrange(1,10)
    
def evaluate_numbers():
    one = give_me_a_num()
    two = random_num()

    for i in range(1, 5):
        if one == two:
            print("Congratulations!! You guessed the correct number!")
        elif one > two:
            print("Your guess is too high\n")
            give_me_a_num() 
        elif one < two:
            print("Your guess is too low\n")
            give_me_a_num()
        

evaluate_numbers()