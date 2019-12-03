import zmq
import papermud
import * from papermud.client.request
import papermud.request as srequest

context = zmq.Context()
socket = context.socket(zmq.REQ)  # pylint: disable=no-member
socket.bind("tcp://*:5555")

onlineplayers = {}
playermessages = {}

while True:
    message = socket.recv_pyobj()
    if ! srequest.check(message):
        continue
