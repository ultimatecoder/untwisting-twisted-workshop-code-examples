from twisted.internet.defer import Deferred


def callback_func(result):
    print(result)


d = Deferred()
d.addCallback(callback_func)
d.callback("Trigerred the callback1")
