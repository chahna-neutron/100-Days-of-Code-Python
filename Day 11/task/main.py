import random
import art

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    r_card=random.choice(cards)
    return r_card


def compare( us_score, co_score):

        if us_score == co_score:
            return "DRAW!!"
        elif co_score == 0:
            return "YOU LOSE"
        elif us_score == 0:
            return "YOU WIN"
        elif us_score > 21:
            return "YOU LOSE"
        elif co_score > 21:
            return "YOU WIN"
        elif us_score > co_score:
            return "YOU WIN"
        else:
            return "YOU LOSE"
def play_game():
    print(art.logo)
    user_cards=[]
    computer_cards=[]
    user_score=-1
    computer_score=-1
    game_over=False



    def calculate_score(cards):
        if 11 in cards and 10 in cards and len(cards)==2:# if sum(cards)==21 and len(cards)==2
           return 0
        if 11 in cards and sum(cards)>21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)

    for i in range(2):
     user_cards.append(deal_card())
     computer_cards.append(deal_card())

    while game_over==False:
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)
        print(f"your cards are: {user_cards}, current score is {user_score}")
        print(f"computer's first card is {computer_cards[0]}")

        if user_score==0 or computer_score==0 or user_score>21:
             game_over=True
        else:
            game_over=False
            answer=input("Type 'y' to get another card or Type 'n' to pass on .").lower()
            if answer=='y':
                user_cards.append(deal_card())
            else:
                game_over=True

    while computer_score!=0 and computer_score<17:
        computer_cards.append(deal_card())
        computer_score=calculate_score(computer_cards)
    print(f"your final cards are: {user_cards}, final score is {user_score}")
    print(f"computer's card are {computer_cards}, final score is {computer_score}")
    print(compare(user_score,computer_score))


while input("You wanna start the game ? (y/n)").lower()=='y':

    print("\n" * 50)
    play_game()

