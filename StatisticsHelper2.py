#take fixed hand and number of card in it

import GameAI
import random
#hand - hand to attack; card_ind - number of the card to attack
def runFirstRoundWithFixedHand(hand_attack=[],card_ind=None):
    deck = ['6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣', 'A♣',\
            '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦', 'A♦',\
            '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥', 'A♥',\
            '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠', 'A♠']
    deck = list(filter(lambda x: not x in hand_attack,deck)) #remove cards in hand from deck
    random.shuffle(deck) #shuffle deck
    g = GameAI.Game(deck,hand_attack,card_ind)#initialize game with rigged deck
    g.runFirstRound() #run first round