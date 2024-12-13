from gui import root, ButtonPullPack, LabelsCard, AmountCards, LabelOfBooster
from functions import BoosterPack
"""This will begin the imports and then establish what function will fire with button presses and in this case BoosterPull will command the button, as seen in line 6 of main  """
def BoosterPull():
    BoosterPack(LabelsCard, AmountCards, LabelOfBooster)
ButtonPullPack.config(command=BoosterPull)
"""Lets the GUI know to run the main loop so that the main window is displayed"""
root.mainloop()