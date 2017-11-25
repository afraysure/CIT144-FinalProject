##############################
# PROLOG SECTION
# CIT144-Python Final Project
# This is a guest log entry form
# 11/24/2017
# Thomas Schueler
# Andrew Fraysure
# Jerry Alsbrooks
# Possible future enhancements: State Selection and Answer to question should both be a drop down menu
# Unresolved bugs:
##############################

#import tkinter to make a gui
from tkinter import *


class MainProgram:
 

        def __init__(self):
                window = Tk()
                window.title("Guest Book")
                
                #Create the label for the guests first name
                label = Label(window, text = "First Name", width = 10,justify = RIGHT).grid(row = 1, column = 1)
                #Entry box for the guests name
                self.firstname = StringVar()
                Entry(window, textvariable = self.firstname, justify = LEFT).grid(row = 1, column = 2, sticky = W)

                #Create the label for the guests last name
                label = Label(window, text = "Last Name", width = 9,justify = RIGHT).grid(row = 1, column = 3, columnspan = 2)
                #Entry box for the guests name
                self.lastname = StringVar()
                Entry(window, textvariable = self.lastname, justify = LEFT).grid(row = 1, column = 4, columnspan = 2, sticky = W)
                
                # Create label for birthdate
                label = Label(window, text = "Birthdate", width = 9, justify = RIGHT).grid(row = 2, column = 1)
                # Entry box for birthdate
                self.birthdate = StringVar()
                Entry(window, textvariable = self.birthdate, width = 10, justify = LEFT).grid(row = 2, column = 2, sticky = W)
                
                # Create label for phone number
                label = Label(window, text = "Phone Number", width = 9, justify = RIGHT).grid(row = 2, column = 3)
                # Entry box for phone number
                self.phone = StringVar()
                Entry(window,textvariable = self.phone, width = 12, justify = LEFT).grid(row = 2, column = 4, sticky = W)

                #Create the label for the guests street
                label = Label(window, text = "Street", width = 7, justify = RIGHT).grid(row = 3, column = 1)
                #entry box for the guests street
                self.street = StringVar()
                Entry(window, textvariable = self.street, justify = LEFT).grid(row = 3, column = 2, columnspan = 3, sticky = W+E)

                #Create the label for the guests city
                label = Label(window, text = "City", width = 7, justify = RIGHT).grid(row = 4, column = 1)
                #entry box for the guests city
                self.city = StringVar()
                Entry(window, textvariable = self.city, justify = LEFT).grid(row = 4, column = 2, sticky = W)
                
                #Create the label for the guests state
                label = Label(window, text = "State", width = 5, justify = RIGHT).grid(row = 4, column = 3)
                #entry box for guests state
                self.state = StringVar()
                Entry(window, textvariable = self.state, width = 2, justify = LEFT).grid(row = 4, column = 4, sticky = W)
                
                #Create the label for the guests zipcode
                label = Label(window, text = "Zip Code", width = 8, justify = RIGHT).grid(row = 4, column = 5)
                #entry box for guests zip code
                self.zipcode = StringVar()
                Entry(window, textvariable = self.zipcode, width = 5, justify = LEFT).grid(row = 4, column = 6, sticky = W)
                
                # Create label for email address
                label = Label(window, text = "Email Address", width = 9, justify = RIGHT).grid(row = 5, column = 1)
                # Entry box for email address
                self.email = StringVar()
                Entry(window, textvarible = self.email, justify = LEFT).grid(row = 5, column = 2, sticky = W)

                # Create label for question
                label = Label(window, text = "How did you find out about us?", width = 8, justify = RIGHT).grid(row = 6, column = 1)
                # Entry box for question
                self.question = StringVar()
                Entry(window, textvariable = self.question, justify = LEFT).grid(row = 6, column = 2,  sticky = W)

                # Create label for comments
                label = Label(window, text = "Comments", width = 9, justify = RIGHT).grid(row = 7, column = 1, columnspan = 6)
                # Entry box for comments
                self.comments = StringVar()
                Entry(window, textvariable = self.comments, justify = LEFT).grid(row = 8, column = 1, columnspan = 6, sticky = W+E)

                #insert the image           
                #logo.grid(row = 1, column = 2, columnspan = 2, rowspan = 2, sticky = W+E+N+S, padx=1, pady =1)

                #Button(window, text = "Save", command = self.Save) is what it should look like when commands are built
                button = Button(window, text = "Save").grid(row = 8, column = 1, columnspan = 6)


                window.mainloop()


                
        
MainProgram()
