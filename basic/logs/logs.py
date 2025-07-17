import logging

## basic setting
logging.basicConfig( # basicConfig ->configure logging system
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[ # list of output destinations for your logs
        logging.FileHandler("app2.log"), # Writes logs to a file
        logging.StreamHandler() # Displays logs in the console
    ]
)

logger = logging.getLogger("Logging Module")

def add(a=5,b=10):
    return a+b
result = add()
logging.info(f"result: {result}")
logging.info("Completed")

def multiplication(a=5,b=10):
    return a*b
result = multiplication()
logging.info("Multiplication Oparation Started")
logging.info(f"result: {result}")
logging.info("Completed")

