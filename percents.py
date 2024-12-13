"""These are all the names, in order, of the cards that can be drawn from booster packs. Namee can only be revealed once."""
cards = [
    "Fish", "Duck", "Horse", "Dog", "Cat", "Chicken", "Pig", "Squirrel", "Donkey", "Rabbit",
    "Monkey", "Jaguar", "Lion", "Penguin", "Iguana", "Owl", "Kangaroo", "Scorpion", "Gorilla", "Whale",
    "Anaconda", "Panther", "Grizz Bear", "Octopus", "Shark", "T-Rex", "Tardigrade", "Yeti", "Alien", "Human"
]
"""These are the numbers for the proper probabilitity of different rows or groups of cards"""
probs = (
    [0.05] * 10 +  # Cards 0 through 9


    [0.04] * 10 +  # Cards 10 through 19


    [0.03] * 5 +   # Cards 20 through 24


    [0.02] * 5     # Cards 25 through 29
)
"""This is needed because without it the probability will not be equaled to 0"""
ProbTotal = sum(probs)
RealProbabilities = [p / ProbTotal for p in probs]