import os


class mudplayer():
    
    def __init__(self, name="nobody", password="password"):
        self.name = name
        self.password = password

    def auth(self):
        return (self.name, self.password)

    def login(self, username, password):
        self.name = username
        self.password = password

    def readinventory(self):
        if os.path.exists(os.environ["HOME"] + "/papermud/users/" + self.name + "inventory")