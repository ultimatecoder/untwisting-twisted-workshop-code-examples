#!/bin/python3


import os
import sys

# Note: Below import should be always before importing Twisted library
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from twisted.application import internet, service

from server import EchoFactory


application = service.Application("echo")
echoService = internet.TCPServer(8000, EchoFactory())
echoService.setServiceParent(application)
