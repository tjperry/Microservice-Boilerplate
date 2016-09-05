"""Class to instantiate instance of an http response and contain correlated functionality.

_response -- dictionary -- holds data regarding status of response and data

"""
from Fwk.logger import Logger

class Response():
    _response = None
    _status = None
    _data = None
    
    @classmethod
    def getInstance(cls):
        try:
            cls._response = {
                'status': cls._status,
                'data': cls._data,
            }
            return cls._response
        
        except NameError:
            Logger.log(Logger.ERROR, 'Response.getInstance() failed to set and return Response._response')

    @classmethod
    def setStatus(cls, status):
        try:
            cls._status = status
        except:
            Logger.log(Logger.ERROR, 'Response.setStatus() failed to set Response._status')

    @classmethod
    def setData(cls, data):
        try:
            cls._data = data
        except:
            Logger.log(Logger.ERROR, 'Response.setData() failed to set Response._data')
            
            


        

            

