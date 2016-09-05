from Fwk.logger import Logger
from Fwk.request import Request
from Fwk.response import Response

def application(environ, start_response):

    Logger.log(Logger.ERROR, 'This is the message')
    Logger.log(Logger.ERROR, 'Second message')
    Logger.log(Logger.ERROR, environ)
    
    start_response('200 OK', [('Content-Type','text/html')])
    return b"Hello world"

