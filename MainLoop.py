import random
from CardCombs import CardCombs
from ObjectiveFunction import Utility

def MainLoop(deck):
    deck = ['6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣', 'A♣',\
            '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦', 'A♦',\
            '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥', 'A♥',\
            '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠', 'A♠']    
    card_comb = CardCombs(deck)
    random.shuffle(card_comb)
    Trump = random.choice(deck) 
    S = 0
    for i in range(len(card_comb)):
        hand1 = card_comb[i]    
        k = Utility(card_comb[i],Trump)
        S = S+k
    
    Ave = S/len(card_comb)
        
    print(card_comb[1])
    print(Ave)
    print(S)
    print(Trump)