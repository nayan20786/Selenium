import logging


def test_loggingDemo():
    logger = logging.getLogger(__name__)
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    fileHandler = logging.FileHandler('logfile.log')  # This decides where the logfile will be saved
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)  # file handler object
    logger.setLevel(logging.INFO)

    # How to log
    # logger.debug("A debug statement is executed")
    # logger.info("Information Statement")
    # logger.warning("Warning but not error")
    # logger.error("Error has been detected")
    # logger.critical("Critical issue")
