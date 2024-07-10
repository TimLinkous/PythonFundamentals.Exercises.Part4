from random import randrange

def give_me_a_num():
    #print("Give a number between 1 and 10\n")
    player_num = input("Give a number between 1 and 10\n")
    return int(player_num)

def random_num():
    return randrange(1,10)
    
    
case_one = give_me_a_num()
case_two = random_num()


while case_one != case_two:
    if case_one > case_two:
            print("Your guess is too high\n")
    elif case_one < case_two:
            print("Your guess is too low\n")
            
    case_one = give_me_a_num()

print("Congrats! You guessed the number!")
        


