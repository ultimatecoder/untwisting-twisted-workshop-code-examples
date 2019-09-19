from twisted.internet import protocol, reactor


class EchoServer(protocol.Protocol):

    def dataReceived(self, data):
        print(data)
        self.transport.write(data)


class EchoFactory(protocol.Factory):

    def buildProtocol(self, addr):
        return EchoServer()


if __name__ == "__main__":
    reactor.listenTCP(8000, EchoFactory())
    reactor.run()
