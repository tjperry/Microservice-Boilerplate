"""Framework module for creating a FwkLogging object.

DEBUG -- constant 

__init__() -- Instantiate an instance of FwkLogging.
log(module, severity)      -- Log a message to the specified severity.
"""


import logging
import logging.config

class Logger():
    # logger module constants
    DEBUG = 10
    INFO  = 20
    WARN  = 30
    ERROR = 40
    CRITICAL = 50
    _LOGGING_CONFIGURATION  = {
        'version' : 1,
        'disable_existing_loggers': True,
        'formatters': {
            'verbose': {
                'class': 'logging.Formatter',
                'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            },
            'simple': {
                'class': 'logging.Formatter',
                'format': '%(levelname)s %(message)s'                
            }
        },
        'handlers': {
            'log': {
                'level':'DEBUG',
                'class':'logging.FileHandler',
                'filename':'logs/app.log',
                'formatter': 'simple'
            },
            'console': {
                'level':'ERROR',
                'class':'logging.StreamHandler',
                'formatter': 'verbose'
            }
        },
        'loggers': {
            'app': {
                'handlers': ['log', 'console'],
                'level': 'DEBUG',
                'propagate': False
            }
        }
    }

    @classmethod
    def log(cls, severity, message, module = 'app'):
        try:
            cls._logger.log(severity, message)          
        except:
            print('Initializing logger')
            logging.config.dictConfig(cls._LOGGING_CONFIGURATION)
            cls._logger = logging.getLogger(module)
            cls.log(severity, message)

