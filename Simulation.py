import random
import numpy
from CardCombs import CardCombs
from ObjectiveFunction import Utility

def FirstR(hand1,hand2,c):
    H_n = []
    H_n = hand2
    
    return H_n

def MainLoop(deck):
    deck = ['6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣', 'A♣',\
            '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦', 'A♦',\
            '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥', 'A♥',\
            '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠', 'A♠']    
    card_comb = CardCombs(deck)
    random.shuffle(card_comb)
    Trump = random.choice(deck) 
    U = [[[0]*len(card_comb)]*len(card_comb)]*6
    
    for i in range(len(card_comb)):
        hand1 = card_comb[i]    
        u0 = Utility(hand1,Trump)
        for j in range(len(card_comb)):
            if j==i :
                break
            else:
                hand2 = card_comb[j]
                for k in range(len(hand1)):
                    hand1_new = FirstR(hand1,hand2,k)
                    u1 = Utility(hand1_new,Trump)
                    U[i][j][k] = (u0-u1)/u0