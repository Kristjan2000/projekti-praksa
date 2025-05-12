import random

def play_game():
    choices = ["kamn", "škarje", "papir"]
    user_choice = input("Izberi si eno od orožij! (kamn, škarje, papir): ").lower()
    
    if user_choice not in choices:
        print("Neveljavna izbira! Prosimo, izberite kamn, škarje ali papir.")
        return

    computer_choice = random.choice(choices)
    print("Izbor računalnika je:", computer_choice)

    if user_choice == computer_choice:
        print("Izenačeno!")
    elif (user_choice == "kamn" and computer_choice == "škarje") or \
         (user_choice == "škarje" and computer_choice == "papir") or \
         (user_choice == "papir" and computer_choice == "kamn"):
        print("Izgubil si!")
    else:
        print("Premagal si računalnika!")

if __name__ == "__main__":
    play_game()