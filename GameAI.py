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
        print('1')#compile!!!!!!!!!!!!!
        
        attacker = self.players[0] #attacker is first in the turn order
        defender = self.players[1] #defender is next
        
        print(attacker.card_ind)#compile!!!!!!!!!!!!!
        print(defender.card_ind)#compile!!!!!!!!!!!!!

        
        inPlay = [] #cards that have been played this bout
        attackCount = 0
        maxAttackCount = min(len(defender.hand), 6) #maximum number of attacks is either 6 or the number of cards the defender has, whichever is smaller
        attacker.changeCardInd(card_ind) #setup index of the starting card
        print(attacker.card_ind)  #compile!!!!!!!!!!!!!      
        
        attack = attacker.promptFirstAttack(defender)
        inPlay.append(attack) #add card to field
        attackCount += 1
        defence = defender.promptDefence(attacker, attack, self.trump)

        while defence != "" and attack != "":
            inPlay.append(defence)
            print(defender.name + " has defended with a " + defence + ". The cards currently in play are:")
            print(inPlay)
            
            """            attack = attacker.promptFollowupAttack(defender, inPlay, attackCount, maxAttackCount)
            if attack == None: #if the attacker has chosen to let others attack
                assist = ""
                for assistant in self.players[2:]: #other players get a chance to attack, in turn order
                    assist = assistant.promptAssistAttack(attacker, defender, inPlay, attackCount, maxAttackCount)
                    if assist != "": #first other player in turn order to make an attack is the assistant
                        inPlay.append(assist) #add card to field
                        attackCount += 1
                        defence = defender.promptDefence(assistant, assist, self.trump)
                        break
                attack = assist
            elif attack != "": #if the attacker attacked
                inPlay.append(attack) #add card to field
                attackCount += 1
                defence = defender.promptDefence(attacker, attack, self.trump)
            """
        
        if defence == "": #defender has chosen not to defend
            print(defender.name + " has conceded the attack.")
            
            """            for player in [self.players[0]]+self.players[2:]:
                dumpedCards = player.promptDumpExtraCards(defender, inPlay, attackCount, maxAttackCount)
                inPlay += dumpedCards
                attackCount += len(dumpedCards)
            print("The following cards have been added to " + defender.name + "'s hand:")
            """
        
            print(inPlay)
            defender.hand += inPlay #if the defender concedes, add cards in play to their hand
            for player in self.players: #all players draw cards until they have 6, starting at the attacker, so long as there are cards in the deck
                if len(player.hand) < 6:
                    for _ in range(min(6 - len(player.hand), len(self.deck))):
                        player.addCard(self.drawCard())
            print("Your cards are now: ", attacker.hand)

        if attack == "": #attacker has chosen to stop attacking
            print("The attack has ended. the following cards have been removed from play:")
            print(inPlay)
            for player in self.players: #all players draw cards until they have 6, starting at the attacker, so long as there are cards in the deck
                if len(player.hand) < 6:
                    for _ in range(min(6 - len(player.hand), len(self.deck))):
                        player.addCard(self.drawCard())
            print("Your cards are now: ", attacker.hand)
            returnHand(attacker)

    def drawCard(self):
        """Removes the last card in the deck and returns its value"""
        if self.deck != []:
            dealtCard = self.deck[-1]
            self.deck = self.deck[:-1]
            return dealtCard

    def returnHand(player):
        return player.hand
