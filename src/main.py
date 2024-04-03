# Created by Giorgio Gamba

import os

# Sends a nofification to the user through the OS with passed information in it
def sendNotification(message, title, subtitle, soundName):
    command = 'display notification "{0}"'.format(title)

    if (title is not None):
        command += ' with title "{0}"'.format(title)

    if (subtitle is not None):
        command += ' subtitle "{0}"'.format(subtitle)

    if (soundName is not None):
        command += ' sound name "{0}"'.format(soundName)

    print(command)

    os.system("osascript -e '{0}' ".format(command))

if __name__ == '__main__':
    sendNotification("TEST TITLE", "TEST MSG", "TEST SUBTITLE", "Pop")
