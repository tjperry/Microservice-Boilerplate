"""Module dedicated to parsing and seperating http request into variables via correlating methods

"""
class Request():
    _request = None
    _type = None
    _params = None
    
    @classmethod
    def getInstance(cls):
        try:
            cls._request = {
                'type': cls._type,
                'params': cls._params,
            }
            return cls._request
        except nameError:
            Logger.log(Logger.ERROR, 'Request.getInstance failed to set and return Request._request')

#    def setInstance(cls, request):
 #       try:
  #          cls._setType

