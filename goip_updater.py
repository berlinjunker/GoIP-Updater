#!/usr/bin/python

__author__ = 'Peter Werner'
__version__ = "1.0"

from urllib2 import urlopen
import os.path

#######################################
#### Login Data #######################
#######################################

username = "USERNAME" # fill in your username
password = "PASSWORD" # fill in your password

#######################################
#######################################

class GoIPUpdater(object):
    username = ""
    password = ""

    def __init__(self, username, password):
        super(GoIPUpdater, self).__init__()
        self.username = username
        self.password = password

    def start(self):
        self.createIPFile()

        if not self.checkIP():
            self.sendUpdate()
            self.updateIPFile()

    def updateIPFile(self):
        open("./current_ip.txt", "w").close()
        f = open("./current_ip.txt", "r+")
        f.write(self.getPublicIP())
        f.close()

    def checkIP(self):
        currentIP = self.getPublicIP()
        lastIP = self.readIPFile()

        if currentIP == lastIP:
            return True
        else:
            return False

    def readIPFile(self):
        ipFileExists = os.path.isfile("./current_ip.txt")
        if ipFileExists:
            f = open("./current_ip.txt")
            return f.read()

    def createIPFile(self):
        ipFileExists = os.path.isfile("./current_ip.txt")
        if not ipFileExists:
            f = open("./current_ip.txt", 'a')
            f.write(self.getPublicIP())
            f.close()

    def buildURL(self):
        url = "https://www.goip.de/setip?username=" + self.username + \
              "&password=" + self.password
        return url

    def getPublicIP(self):
        my_ip = urlopen("http://ip.42.pl/raw").read()
        return my_ip

    def sendUpdate(self):
        return urlopen(self.buildURL()).read()


def main():
    updater = GoIPUpdater(username, password)
    updater.start()

    # print(updater.getPublicIP()) # prints the current public IP adress
    # print(updater.buildURL()) # returns the update URL for current public IP adress
    # print(updater.sendUpdate()) # send update to DNS


if __name__ == '__main__':
    main()
