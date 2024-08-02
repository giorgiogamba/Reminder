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
        self.process = None

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
        self.process = Process(target = self.execute)
        self.process.start()        

    def stop(self):
        self.process.kill()
        return

class Window:

    def createAndAddNotification():
        return

    def removeNotification(self):
        self.listView.delete(self.currIndex, self.currIndex)
        self.listView.pack()

        self.activeNotifications[self.currIndex].stop()
        del self.activeNotifications[self.currIndex]
            
    def launchWindow(self):
        self.window.mainloop()
    
    def addTestNotification(self,notification):
        self.listView.insert("end", notification)
        self.listView.pack()
        self.activeNotifications.append(notification)

        notification.start()
    
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

    def onCloseApp(self):
        for notification in self.activeNotifications:
            notification.stop()

        self.window.destroy()

    def createWindow(self):
        self.window = tk.Tk()
        self.window.title(APP_TITLE)
        self.window.resizable()
        self.window.geometry("200x200")
        self.window.minsize(MIN_WIDTH, MIN_HEIGHT)
        self.window.protocol("WM_DELETE_WINDOW", self.onCloseApp)


    def __init__(self):
        self.currIndex = None
        self.activeNotifications = []

        self.createWindow()
        self.createButtons()
        self.createListview()

if __name__ == '__main__':

    window = Window()
    window.addTestNotification(Notification("TITLE", "MSG", "SUBTITLE", "Pop", 10))
    window.addTestNotification(Notification("TITLE2", "MSG2", "SUBTITLE2", "Pop", 5))

    # Starts the window
    window.launchWindow()
