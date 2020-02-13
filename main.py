from tkinter import *

mainWindow = Tk()
mainWindow.title("Calculator")

mainFrame = Frame(mainWindow, width=300, height=300)
mainFrame.pack(fill=BOTH)

leftFrame = Frame(mainFrame)
leftFrame.grid(column=0, row=0)

leftEntryVar = StringVar()
leftEntryVar.set("Number")
leftEntry = Entry(leftFrame, textvariable=leftEntryVar)
leftEntry.pack()

centerFrame = Frame(mainFrame)
centerFrame.grid(column=1, row=0)

plusButton = Button(centerFrame, text="+")
plusButton.pack(side=TOP, padx=40)
minusButton = Button(centerFrame, text="-")
minusButton.pack(side=TOP, padx=40)
multButton = Button(centerFrame, text="*")
multButton.pack(side=TOP, padx=40)
divButton = Button(centerFrame, text="/")
divButton.pack(side=TOP, padx=40)
modButton = Button(centerFrame, text="%")
modButton.pack(side=TOP, padx=40)

rightFrame = Frame(mainFrame)
rightFrame.grid(column=2, row=0)

rightEntryVar = StringVar()
rightEntryVar.set("Number")
rightEntry = Entry(rightFrame, textvariable=rightEntryVar)
rightEntry.pack()

#varTitle = StringVar()
#varTitle.set("Calculator")

#labelTitle = Label(mainFrame, textvariable=varTitle, padx=10, pady=10)
#labelTitle.pack()

mainWindow.mainloop()

