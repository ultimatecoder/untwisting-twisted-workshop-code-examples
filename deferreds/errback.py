from twisted.internet.defer import Deferred


def errback_func(failure):
    print(failure)


d = Deferred()
d.addErrback(errback_func)
d.errback("Error back Triggered!".encode("utf-8"))
