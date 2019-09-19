from twisted.test import proto_helpers
from twisted.trial import unittest

from echo.server import EchoFactory


class TestEchoServer(unittest.TestCase):

    def test_response(self):
        factory = EchoFactory()
        protocol = factory.buildProtocol(("localhost", 0))
        transport = proto_helpers.StringTransport()

        protocol.makeConnection(transport)
        data = b"test\r\n"
        protocol.dataReceived(data)
        self.assertEqual(transport.value(), data)
