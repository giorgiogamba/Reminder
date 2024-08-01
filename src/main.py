# Created by Giorgio Gamba

# Imports
import os
import time
from multiprocessing import Process
import tkinter as tk

# Constants
MIN_WIDTH = 200
MIN_HEIGHT = 200
APP_TITLE = "Reminder"

# Defines a notification
class Notification:

    def __init__(self, title, msg, subtitle, soundName, time):
        self.title = title
        self.msg = msg
        self.subtitle = subtitle
        self.soundName = soundName
        self.time = time

    def __str__(self):
        return self.title + " -- Every " + str(self.time) + " minutes"

    # Sends a nofification to the user through the OS with passed information in it
    def sendNotification(self):

        # Build the command
        command = 'display notification "{0}"'.format(self.title)

        if (self.title is not None):
            command += ' with title "{0}"'.format(self.title)

        if (self.subtitle is not None):
            command += ' subtitle "{0}"'.format(self.subtitle)

        if (self.soundName is not None):
            command += ' sound name "{0}"'.format(self.soundName)

        print(command)

        # Execute the command
        os.system("osascript -e '{0}' ".format(command))

    def wait(self):
        time.sleep(self.time)

    def execute(self):
        while True:
            self.sendNotification()
            self.wait()

    def start(self):

        # Each notification is represented by a single process that handles its sleeping
        process = Process(target = self.execute)
        process.start()        

class Window:

    def createAndAddNotification():
        return

    def removeNotification():
        # Retrieve the currently selected notification
        
        # stop
        # remove from list
        return
    
    def loop(self):
        self.window.mainloop()
    
    def addTestNotification(self,notification):
        self.listView.insert("end", notification)
        self.listView.pack()
    
    def updateListIndex(self, event):
        selection = event.widget.curselection()
        if selection:
            print("Changed list selection in "+str(selection[0]))
            self.currIndex = selection[0]
        else:
            self.currIndex = None

    def createListview(self):
        self.listView = tk.Listbox(self.window)
        self.listView.pack(padx=10,pady=10,fill=tk.BOTH,expand=True)
        self.listView.bind("<<ListboxSelect>>", self.updateListIndex)
        self.listView.pack()

    def createButtons(self):
        self.addButton = tk.Button(self.window, text='Add', width=25, command=self.createAndAddNotification)
        self.addButton.pack()

        self.removeButton = tk.Button(self.window, text='Remove', width=25, command=self.removeNotification)
        self.removeButton.pack()

    def createWindow(self):
        self.window = tk.Tk()
        self.window.title(APP_TITLE)
        self.window.resizable()
        self.window.geometry("200x200")
        self.window.minsize(MIN_WIDTH, MIN_HEIGHT)

    def __init__(self):
        self.currIndex = None

        self.createWindow()
        self.createListview()
        self.createButtons()

if __name__ == '__main__':

    activeNotifications = [] # Keeps track of the active notifications

    # TEST CODE
    activeNotifications.append(Notification("TITLE", "MSG", "SUBTITLE", "Pop", 10))
    activeNotifications.append(Notification("TITLE2", "MSG2", "SUBTITLE2", "Pop", 5))

    activeNotifications[0].start()
    activeNotifications[1].start()

    window = Window()
    window.addTestNotification(activeNotifications[0])
    window.addTestNotification(activeNotifications[1])

    # Starts the window
    window.loop()
