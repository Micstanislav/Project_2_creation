import tkinter as tk

""" This starts the main bit of programming, it will make a window called the 'Creature Finder'"""
root = tk.Tk()
root.title("Creature Finder")
"""This gives the window its title and then creates 30 card spots in a grid"""
LabelsCard = []
for i in range(30):
    label = tk.Label(root, text="", width=10, height=2, relief="solid", bg="white")
    label.grid(row=i // 10, column=i % 10, padx=5, pady=5)
    LabelsCard.append(label)

ButtonPullPack = tk.Button(root, text="Pull Pack")
ButtonPullPack.grid(row=3, column=0, columnspan=8, pady=10)

AmountCards = tk.Label(root, text="Discovered 0/30 unique cards!")
AmountCards.grid(row=4, column=0, columnspan=8)

LabelOfBooster = tk.Label(root, text="Packs Opened: 0", fg="blue")
LabelOfBooster.grid(row=3, column=8, columnspan=2, padx=10)