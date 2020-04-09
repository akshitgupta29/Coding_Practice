# Kaggle exercise for Python - external libraries and other codes
# Link: https://www.kaggle.com/akshitgupta29/exercise-working-with-external-libraries/edit
# @author: Akshit Gupta


#Problem 3
def blackjack_hand_greater_than(hand_1, hand_2):
    """
    Return True if hand_1 beats hand_2, and False otherwise.
    
    In order for hand_1 to beat hand_2 the following must be true:
    - The total of hand_1 must not exceed 21
    - The total of hand_1 must exceed the total of hand_2 OR hand_2's total must exceed 21
    
    Hands are represented as a list of cards. Each card is represented by a string.
    
    When adding up a hand's total, cards with numbers count for that many points. Face
    cards ('J', 'Q', and 'K') are worth 10 points. 'A' can count for 1 or 11.
    
    When determining a hand's total, you should try to count aces in the way that 
    maximizes the hand's total without going over 21. e.g. the total of ['A', 'A', '9'] is 21,
    the total of ['A', 'A', '9', '3'] is 14.
    
    Examples:
    >>> blackjack_hand_greater_than(['K'], ['3', '4'])
    True
    >>> blackjack_hand_greater_than(['K'], ['10'])
    False
    >>> blackjack_hand_greater_than(['K', 'K', '2'], ['3'])
    False
    """
    h1_sum = 0
    h2_sum = 0
    
    for card1 in hand_1:
        if card1 in ['J', 'Q', 'K']:
            h1_sum +=10
        elif card1 != 'A':
            h1_sum += int(card1)
        
        if card1 == 'A':
            if h1_sum < 10 :
                h1_sum += 11
            else:
                h1_sum += 1
        
    for card2 in hand_2:
        if card2 in ['J', 'Q', 'K']:
            h2_sum +=10
        elif card2 != 'A':
            h2_sum += int(card2)
            
        if card2 == 'A':
            if h2_sum < 10:
                h2_sum += 11
            else:
                h2_sum += 1
    
    if (h1_sum <= 21) and (h1_sum > h2_sum or h2_sum > 21):
        return True
    return False
           
    
    
if __name__ == "__main__":
    hand_1=['2', '8', '3']
    hand_2=['A', '4', '4', '7']
    result = blackjack_hand_greater_than(hand_1, hand_2)
    print (result)