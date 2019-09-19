from twisted.internet import reactor, protocol


class EchoClient(protocol.Protocol):

    def connectionMade(self):
        response = "Hello world!"
        self.transport.write(response.encode("utf-8"))

    def dataReceived(self, data):
        print(data)
        self.transport.loseConnection()


class EchoFactory(protocol.ClientFactory):

    def buildProtocol(self, addr):
        protocol = EchoClient()
        protocol.factory = self
        return protocol

    def clientConnectionFailed(self, connector, reason):
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        reactor.stop()


if __name__ == "__main__":
    reactor.connectTCP("localhost", 8000, EchoFactory())
    reactor.run()
