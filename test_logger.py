# importing module
import logging
 
# Create and configure logger
logging.basicConfig(filename="C:/Users/Administrator/Desktop/vu/auto_training/newfile.log",
                    #format='%(asctime)s %(message)s',
                    filemode='w')
 
# Creating an object
logger = logging.getLogger()
 
# Setting the threshold of logger to DEBUG
logger.setLevel(logging.INFO)
 
# Test messages
# logger.debug("Harmless debug Message")
logger.info("abcdef")
# logger.warning("Its a Warning")
# logger.error("Did you try to divide by zero")
# logger.critical("Internet is down")