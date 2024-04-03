# Created by Giorgio Gamba

import os

# Sends a nofification to the user through the OS with passed information in it
def sendNotification(message, title):
    command = 'display notification "{0}" {1}'.format(title, message)
    os.system("osascript -e {0}".format(command))

if __name__ == '__main__':
    sendNotification("TEST TITLE", "TEST MSG")
