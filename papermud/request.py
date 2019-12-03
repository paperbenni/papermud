from ...request import *

def check(rq, onlineplayers):
        # already logged in
        if rq.name in onlineplayers:
            if password == onlineplayers[name]:
                return True
            else:
                return False
        else:
            # sign into a new session
            passpath = os.environ["HOME"] + \
                "/papermud/users/" + name + "/password.txt"
            if os.path.exists(passpath):
                if password == open(passpath, "r").read():
                    onlineplayers[name] = password
                    return True
                else:
                    return False