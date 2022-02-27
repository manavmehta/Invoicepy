import logging

def getLogger():
    logging.basicConfig(filename="Logs/0.log",
                    format='[%(asctime)s] [%(levelname)s] [%(message)s]',
                    filemode='a',
                    level=logging.DEBUG)
    return logging.getLogger()
