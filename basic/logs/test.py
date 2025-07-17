from logs import logging
def add(a=5,b=10):
    return a+b

logging.info("Oparation Started")
logging.debug(add())
logging.info("Completed")