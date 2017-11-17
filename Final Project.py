##############################
# PROLOG SECTION
# CIT144-Python Final Project
# This is a guest log entry form
# 11/17/2017
# Thomas Schueler
# Andrew Fraysure
# Jerry Alsbrooks
# Possible future enhancements: State Selection should be a drop down menue
# Unresolved bugs:
##############################

#import tkinter to make a gui
from tkinter import *


class MainProgram:
 

        def __init__(self):
                window = Tk()
                window.title("Guest Book")
                
                #Create the label for the guests first name
                label = Label(window, text = "First Name", width = 10,justify = LEFT).grid(row = 1, column = 1)
                #Entry box for the guests name
                self.name = StringVar()
                Entry(window, textvariable = self.name, justify = LEFT).grid(row = 1, column = 2, sticky = W)

                #Create the label for the guests last name
                label = Label(window, text = "Last Name", width = 9,justify = LEFT).grid(row = 1, column = 3, columnspan = 2)
                #Entry box for the guests name
                self.name = StringVar()
                Entry(window, textvariable = self.name, justify = LEFT).grid(row = 1, column = 5, columnspan = 2, sticky = W)

                #Create the label for the guests street
                label = Label(window, text = "Street", width = 7, justify = LEFT).grid(row = 2, column = 1)
                #entry box for the guests street
                self.street = StringVar()
                Entry(window, textvariable = self.street, justify = LEFT).grid(row = 2, column = 2, columnspan = 5, sticky = W+E)

                #Create the label for the guests city
                label = Label(window, text = "City", width = 7, justify = LEFT).grid(row = 3, column = 1)
                #entry box for the guests city
                self.city = StringVar()
                Entry(window, textvariable = self.city, justify = LEFT).grid(row = 3, column = 2, sticky = W)
                
                #Create the label for the guests state
                label = Label(window, text = "State", width = 5, justify = LEFT).grid(row = 3, column = 3)
                #entry box for guests state
                self.state = StringVar()
                Entry(window, textvariable = self.state, width = 2, justify = LEFT).grid(row = 3, column = 4, sticky = W)
                
                #Create the label for the guests zipcode
                label = Label(window, text = "Zip Code", width = 8, justify = LEFT).grid(row = 3, column = 5)
                #entry box for guests zip code
                self.zipcode = StringVar()
                Entry(window, textvariable = self.zipcode, width = 5, justify = LEFT).grid(row = 3, column = 6, sticky = W)

                #Create the label for the comments
                label = Label(window, text = "Comments", width = 8, justify = LEFT).grid(row = 4, column = 1, columnspan = 6)
                #entry box for guests zip code
                self.comments = StringVar()
                Entry(window, textvariable = self.comments, justify = LEFT).grid(row = 5, column = 1, columnspan = 6,  sticky = W+E)

                

                #insert the image           
                #logo.grid(row = 1, column = 2, columnspan = 2, rowspan = 2, sticky = W+E+N+S, padx=1, pady =1)

                #Button(window, text = "Save", command = self.Save) is what it should look like when commands are built
                button = Button(window, text = "Save").grid(row = 8, column = 1, columnspan = 6)


                window.mainloop()
        
MainProgram()
