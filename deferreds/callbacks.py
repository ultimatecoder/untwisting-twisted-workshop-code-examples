from twisted.internet.defer import Deferred


def callback_func(result):
    print(result)


def errback_func(failure):
    print(failure)


d = Deferred()
d.addCallbacks(callback_func, errback_func)
d.callback(b"I am success callback!")

# OR

#d.errback(b"I am error callback!")
