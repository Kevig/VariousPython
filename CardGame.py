import random

# Deque implementation to act as a card deck
# Cards can be removed from the front (top)
# Cards added to the deck will be inserted at the Rear(bottom) of the stack
class Deque:

        def __init__(self):
                self.items =[]

        def isEmpty(self):
                return self.items == []

        def add(self, item):
                self.items.append(item)

        def remove(self):
                return self.items.pop()

        def size(self):
                return len(self.items)

# getValue function, implements a dictionary with key "card name"
# allows card 'values' to be set
# Receives card name, returns card value
# For development will let method return a value equal to the card name
# so that game type can be changed / modded at later stages
# Could possibly be part of card class, will decide in later stages
def getValue(name):

        cardValues = {'2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8' \
                        ,'9':'9','10':'10','Jack':'10','Queen':'10','King':'10','Ace': '11'}

        if name in cardValues:
                value = cardValues.get(name)
                return (value)

def getTotalValue(whom, deckName):
        tValue = 0
        for key, value in deckName.dealtCards.items():
                cObj = value
                if (cObj.location == whom):
                        cName = cObj.cardName

                        tValue += int(getValue(cName))
        return(tValue)
                               
# Class Card, creates an instance for every individual card
# stores card name, suit and card's location (ie - in deck, in player hand etc)
class Card:

	# Initialise card, card name / suit will be passed in from deck upon
	# shuffle
	# Card will get its value from getValue, based on its name
	# Will possibly implement suit values later depending on card game type
        def __init__(self, name, suit):
                
                self.cardName = name
                self.cardSuit = suit	
                self.value = getValue(self.cardName)
                self.location = None
		
        # Allow card location to be set
        def setLocation(self, location):
                self.location = location
                
        # Get card location
        def getLocation(self):
                print ("%s is current card owner" % (self.location))

        # Get card name
        def showCard(self):
                print ("Card is %s of %s" % (self.cardName, self.cardSuit))

        # Drop a card returning it to the bottom of the deck
        def dropCard(self, deckName):
                self.location = "Deck"  #Deck reference
                deckName.addCard(self.cardName, self.cardSuit) #Call deck to pass card back
                
                getKey = None

                # Itterate dealtCards dictionary to check if value is equal to this card, if true set getKey to that reference
                for key, value in deckName.dealtCards.items():
                        if (value == self):
                                getKey = key

                # Use getKey ref to remove entry from dictionary
                if (getKey != None):
                        del deckName.dealtCards[getKey]

                self = None
        
                print ("Card returned to deck")
                

# Deck Object, holds each card, can have multiple decks
class Deck:

        # Initialise deck. cardNames contains all possible card names, cardSuits contains all possible suits.
        # self.deck creates a new "Deque" data storage structure.
        def __init__(self):
                
                self.cardNames = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"] # Define all possible card names
                self.cardSuits = ["Clubs","Diamonds","Hearts","Spades"] # Define all possible card suits

                self.deck = Deque()
                self.counter = 1
                self.card = None

                self.shuffled = "No"

                self.dealtCards = {}

        # Shuffle method:
        def shuffle(self):
                
                cardList = list()       # Two new empty lists for storing card names / suits
                suitList = list()       # each list will be length of total cards in deck - ie 52 (cardNames length * suitNames length)

                # Itterate suitList length times - In traditional cards, this would be 4 suits
                for i in self.cardSuits:
                        
                        # Nested Loop to itterate cardList length times for each suit
                        for j in self.cardNames:
                                
                                suitList.append(i)      # Append the cardName and cardSuit to the appropriate list
                                cardList.append(j)      # List order is important as it ensures that duplicate names / values of cards won't exist

                startLen = len(cardList)        # Get length of cardList and store in ref: startLen
                newLen = startLen               # Define newLen ref and set its value to startLen
                
                # Itterate startLen times, which will be the total number of cards a deck will consist of
                # Alternative loop could be "while not cardList" >>> TEST <<<
                for i in range(0,startLen):

                        # Pos = index of List to pull value from, will random roll between index's 0 and current length of cardList
                        pos = random.randrange(0, newLen)
                        self.deck.add(cardList[pos]+"-"+suitList[pos])  # Using Pos index value, pull the values of card list and suit, and place in deck

                        del cardList[pos]       # Remove the index position of pos from card list/suit
                        del suitList[pos]       # altering the size of the lists
                        
                        newLen = len(cardList)  # Get new cardList length and repeat itteration until cardList is empty

                self.shuffled = "Yes"
                print ("Deck Shuffled")

        # Add card to deck
        # Requires deck name, cardName, cardSuit, will be added to bottom of deck
        def addCard(self, name, suit):
                self.deck.add(name + "-" + suit)

        # Deal a card from deck - (remove a card from deck)
        # Requires deck name and who the card will be sent to, card will be taken from top of deck
        def dealCard(self, toWho):

                if (self.shuffled == "Yes"):
                        newCard = self.deck.remove()    # Take card from deck

                        split = newCard.split("-")      # Split string name into name / suit

                        name = split[0]                 # Store split name / suit
                        suit = split[1]                 #

                        cardRef = "card" + str(self.counter)    # String reference for dealt cards counter
                        card = Card(name,suit)                  # Create a new card object
                        card.setLocation(toWho)                 # Set the new object's location as the object that requested the creation
                        self.dealtCards[cardRef] = card         # Add the new Object under cardRef key
                        self.counter+=1                         # Increment the cardRef counter
                
                        print ("Card dealt to %s" % (toWho))
                # Catch Non shuffled Deck exception
                else:
                        print ("Deck must be shuffled before cards can be dealt")

        
                
                
                



        
