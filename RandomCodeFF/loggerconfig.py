# importing module
import logging
 
# Create and configure logger
logging.basicConfig(filename="/workspaces/practise/RandomCodeFF/LogaboutLog.log",
                    format='%(asctime)s %(message)s',
                    filemode='a')
# Creating an object
logger = logging.getLogger()
# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

# Test messages
logger.debug("Heart has 4 valves but still its beating for you.")
logger.info("I may be a page to you, but You are my whole Book.")
logger.warning("Trust breaking not fun")
logger.error("Cracking sound in every beat of the heart, is it the effect of breaking up.")
logger.critical("Rise Up, Long Way to Go, Travel matters, who cares if its single.")


print("sUccess depends on the second letter.   -J")
