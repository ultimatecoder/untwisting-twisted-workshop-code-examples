import time

from twisted.internet import reactor
from twisted.internet.task import deferLater
from twisted.web.resource import Resource
from twisted.web.server import Site, NOT_DONE_YET


class BusyPage(Resource):

    isLeaf = True

    def _delayResponse(self, request):
        end_time = time.time()
        response = "Ended at {}".format(end_time)
        request.write(response.encode("utf-8"))
        request.finish()

    def render_GET(self, request):
        d = deferLater(reactor, 5, lambda: request)
        d.addCallback(self._delayResponse)
        return NOT_DONE_YET


if __name__ == "__main__":
    factory = Site(BusyPage())
    reactor.listenTCP(8000, factory)
    reactor.run()
