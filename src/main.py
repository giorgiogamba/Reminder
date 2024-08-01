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

def createAndAddNotification():
    return

if __name__ == '__main__':

    activeNotifications = [] # Keeps track of the active notifications

    # TEST CODE
    activeNotifications.append(Notification("TITLE", "MSG", "SUBTITLE", "Pop", 10))
    activeNotifications.append(Notification("TITLE2", "MSG2", "SUBTITLE2", "Pop", 5))

    activeNotifications[0].start()
    activeNotifications[1].start()

    # Crates User Interface
    window = tk.Tk()
    window.title("TEST")
    window.resizable()
    window.geometry("200x200")
    window.minsize(MIN_WIDTH, MIN_HEIGHT)

    # Add notification button
    addButton = tk.Button(window, text='Add', width=25, command=createAndAddNotification)
    addButton.pack()


    # Remove notification button
    removeButton = tk.Button(window, text='Remove', width=25, command=createAndAddNotification)
    removeButton.pack()


    # Notifications list view
    listView = tk.Listbox(window)
    listView.pack(padx=10,pady=10,fill=tk.BOTH,expand=True)

    listView.insert(0, activeNotifications[0])
    listView.insert(1, activeNotifications[1])
    listView.pack()


    # Starts the window
    window.mainloop()
