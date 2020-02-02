"""
    nih dialog class
"""
from Tkinter import *
import tkSimpleDialog
import tkMessageBox

class dialog(tkSimpleDialog.Dialog):
    """
        DIALOG
    """
    def __init__(self, parent, title):
        tkSimpleDialog.Dialog.__init__(self, parent, title)

    def body(self, parent):

        Label(parent, text='First name: ').grid(row=0)
        Label(parent, text='Last name: ').grid(row=1)

        self.firstNameEntry = Entry(parent)
        self.lastNameEntry = Entry(parent)

        self.firstNameEntry.grid(row=0, column=1)
        self.lastNameEntry.grid(row=1, column=1)

        return self.firstNameEntry	# Initial focus

    def validate(self):

        if not self.firstNameEntry.get().isalpha():
            tkMessageBox.showwarning('Warning - bad input', 'Please check the first name entry')
            return 0
        elif not self.lastNameEntry.get().isalpha():
            tkMessageBox.showwarning('Warning - bad input', 'Please check the last name entry')
            return 0
        else:
            return 1

    def apply(self):
        self.firstName = self.firstNameEntry.get()
        self.lastName = self.lastNameEntry.get()
