import random
import DurakRulesHelperFunctions
from Player2 import AIPlayer
class Game:
    def __init__(self, deck=[],hand_attack = [], card_ind=None):
        #initialize and shuffle deck
        numAIPlayers = 2
        
        if deck == []:
            self.deck = ['6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣', 'A♣',\
                         '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦', 'A♦',\
                         '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥', 'A♥',\
                         '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠', 'A♠']
            random.shuffle(self.deck)
        else:
            self.deck = deck
        self.trump = self.deck[0]
        #initialize 2 players
        self.players = []  
        for i in range(numAIPlayers):
            self.players.append(AIPlayer("Player " + str(i+1)))
        #deal hands
        for i in range(6):
                self.players[0].addCard(hand_attack[i]) #1st hand is fixed
                self.players[1].addCard(self.drawCard()) #defender obtains random cards
                                         
    def runFirstRound(self):
        print("Welcome to Durak. The Trump card is " + self.trump)

        print("Note: when prompted for the index of a card, the indices start at 0.")

        attacker = self.players[0] #attacker is first in the turn order
        defender = self.players[1] #defender is next
        returnHand(attacker)

    def drawCard(self):
        """Removes the last card in the deck and returns its value"""
        if self.deck != []:
            dealtCard = self.deck[-1]
            self.deck = self.deck[:-1]
            return dealtCard

    def returnHand(player):
        return player.hand
