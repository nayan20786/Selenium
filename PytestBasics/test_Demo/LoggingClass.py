import inspect
import logging


class LoggingClass:
    def getlogger(self):
        loggerName = inspect.stack()[1][3]  # This will log from the file from which the testcase is executing
        # logger = logging.getLogger(__name__)#This was logging LoggingClass class
        logger = logging.getLogger(loggerName)
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler = logging.FileHandler('logfile.log')  # This decides where the logfile will be saved
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # file handler object
        logger.setLevel(logging.INFO)

        return logger
