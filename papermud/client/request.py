import player
import os


class mudrequest():
    def __init__(self, player, command, args):
        self.username, self.password = player.auth()
        self.command = command
        self.args = args
                    

class mudanswer():
    def __init__(self, player):
        this.player = player
        if player in playermessages.keys():
            this.messages = playermessages[player]
        else:
            this.messages = False
