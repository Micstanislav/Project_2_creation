import random
from percents import cards, RealProbabilities
""""This is just setting up my imports then CardsOfDiscovery = False means how many not discovered yet. 
Then we establish our global with our counter resetting and making sure we are starting at 0."""
CardsOfDiscovery = [False] * 30
BoosterCount = 0

def CardRand():
    """This is where we set our probability and it will attach to each card in the order that the grid is created,
    the function makes a probability list that is cumulative based on the probabilities i give it and thenpicks a card by making a number between 0 and 1 and brings that card name up,
    below is the way that it queries the probabilities"""
    cumulative = []
    total = 0
    for prob in RealProbabilities:
        total += prob
        cumulative.append(total)

    rand = random.random()
    """Learned enumerate will iterate over a sequence, so experimented to get this to create the a working function, the index (i) of the gui element number 0 through 29, is 
     attached to a 'threshold', if the random # is smaller than the threshold then the card that associated with the index 'i' will attach there and because we return cards[-1]
     then it will cycle around"""
    for i, threshold in enumerate(cumulative):
        if rand < threshold:
            return cards[i]
    return cards[-1]

def BoosterPack(LabelsCard, AmountCards, LabelOfBooster):
    """This function will simulate drawing 5 cards or a "Booster Pack" as it is known in trading cards. It uses 'not in' to make sure the card rand number is not already selected
    and if not then it will append that number to the list, it will then update the count for the pack, then display the status of card collection if it is fulfilled.
    If it is full then will return '30 cards have been discovered'"""
    global CardsOfDiscovery, BoosterCount

    pack = []
    while len(pack) < 5:
        card = CardRand()
        if card not in pack:
            pack.append(card)

    for card in pack:
        index = cards.index(card)
        if not CardsOfDiscovery[index]:
            CardsOfDiscovery[index] = True
            LabelsCard[index].config(text=card, bg="lightgreen")

    BoosterCount += 1
    LabelOfBooster.config(text=f"Packs Opened: {BoosterCount}")

    CountOfDiscovery = sum(CardsOfDiscovery)
    if CountOfDiscovery == 30:
        AmountCards.config(text="Success! Collection Complete!", fg="red")
        return True
    else:
        AmountCards.config(text=f"You have found {CountOfDiscovery}/30 cards that are unique!")
        return False