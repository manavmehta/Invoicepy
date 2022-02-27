import configparser
import logging

config = configparser.ConfigParser()
config.read('logger.config')

def getLogLevel(configLogLevel):
    if(configLogLevel == 'DEBUG'):
        return logging.DEBUG
    
    elif(configLogLevel == 'INFO'):
        return logging.INFO
    
    elif(configLogLevel == 'WARNING'):
        return logging.WARNING
    
    elif(configLogLevel == 'ERROR'):
        return logging.ERROR
    
    else:
        return logging.CRITICAL

def getLogger():
    logging.basicConfig(filename=config['DEFAULT']['Filename'],
                    format='[%(asctime)s] [%(levelname)s] [%(message)s]',
                    filemode=config['DEFAULT']['Filemode'],
                    level=getLogLevel(config['DEFAULT']['LogLevel']))
    
    return logging.getLogger()
