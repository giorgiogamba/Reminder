# Created by Giorgio Gamba

# Imports
import os
import time
from multiprocessing import Process

# Defines a notification
class Notification:

    def __init__(self, title, msg, subtitle, soundName, time):
        self.title = title
        self.msg = msg
        self.subtitle = subtitle
        self.soundName = soundName
        self.time = time

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

if __name__ == '__main__':

    activeNotifications = [] # Keeps track of the active notifications

    # TEST CODE
    activeNotifications.append(Notification("TITLE", "MSG", "SUBTITLE", "Pop", 10))
    activeNotifications.append(Notification("TITLE2", "MSG2", "SUBTITLE2", "Pop", 5))

    activeNotifications[0].start()
    activeNotifications[1].start()
