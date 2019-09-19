from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver
from twisted.internet import reactor


class ChatProtocol(LineReceiver):

    def __init__(self, factory):
        self.factory = factory

    def connectionMade(self):
        self.factory.users.append(self)

    def lineReceived(self, line):
        for user in self.factory.users:
            if user != self:
                user.transport.write(line + b"\r\n")


class ChatFactory(Factory):

    def __init__(self):
        self.users = []

    def buildProtocol(self, addr):
        return ChatProtocol(self)


if __name__ == "__main__":
    reactor.listenTCP(6000, ChatFactory())
    reactor.run()
