import logging
import inspect


def Logger(self, logLevel=logging.DEBUG):
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)
    logger.setLevel(logLevel)
    log_file = logging.FileHandler("automation.log")
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s : %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    log_file.setFormatter(formatter)
    logger.addHandler(log_file)
    return logger