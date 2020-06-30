import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 
        'Three':3, 
        'Four':4, 
        'Five':5, 
        'Six':6, 
        'Seven':7, 
        'Eight':8, 
        'Nine':9, 
        'Ten':10, 
        'Jack':11,
        'Queen':12, 
        'King':13, 
        'Ace':14}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:
    def __init__(self):
        self.all_cards = []  
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)
    
    def __str__(self):
        deck_comp = ''  # start with an empty string
        for card in self.deck:
            deck_comp += '\n '+card.__str__() # add each Card object's print string
        return 'The deck has:' + deck_comp

    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []
    
    def remove_one(self):
        return self.all_cards.pop(0)
    
    def add_cards(self, new_cards):
        if type(new_cards) == type ([]):
            #list of multiple card obj
            self.all_cards.extend(new_cards)
        else:
            #for a sigle card obj
            self.all_cards.append(new_cards)
    
    def __str__(self):
        return f'player {self.name} has {len(self.all_cards)} cards.'

# new_deck = Deck()
# new_deck.shuffle()

# for card_object in new_deck.all_cards:
#     new_deck.shuffle()

# mycard = new_deck.deal_one()
# print(mycard)
# #print(len(new_deck.all_cards))

# new_player = Player('CPU1')
# print(new_player)
# new_player.add_cards(mycard)
# print(new_player)
# print(new_player.all_cards[0])
# new_player.add_cards([mycard, mycard, mycard])
# print(new_player)

# new_player.remove_one()
# print(new_player)

#create players
player_one = Player('One')
player_two = Player('Two')

#create deck and shuffle it
new_deck = Deck()
new_deck.shuffle()

#split deck between two players
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True
round_num = 0

while game_on:
    round_num += 1
    print(f'round {round_num}')
    
    if len(player_one.all_cards) == 0:
        print('Player 1, out of cards. Player 2 wins')
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print('Player 2, out of cards. Player 1 wins')
        game_on = False
        break
    
    # cards on table
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    # while at war
    at_war = True
    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            at_war = False
        
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)

            at_war = False

        else:
            print('WAR !!!')
            if len(player_one.all_cards) < 5:
                print('Player 1 cant play anymore !')
                print('Player 2 wins')
                game_on = False
                break

            elif len(player_two.all_cards) < 5:
                print('Player 2 cant play anymore !')
                print('Player 1 wins')
                game_on = False
                break

            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())

game_on()