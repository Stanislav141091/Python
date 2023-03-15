import logging
from test_data.test_data import TestData


class Loger:

    @staticmethod
    def custom_logger(loglevel):
        logger = logging.getLogger(__name__)
        logger.setLevel(loglevel)
        file = logging.FileHandler(TestData.get_log_file_name())
        formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(message)s", "%d-%m-%Y %H:%M:%S ")
        file.setFormatter(formatter)
        logger.addHandler(file)
        return logger

    @staticmethod
    def info(message):
        log = Loger.custom_logger(loglevel=logging.INFO)
        return log.info(message)

    @staticmethod
    def warning(message):
        log = Loger.custom_logger(loglevel=logging.WARNING)
        return log.warning(message)

    @staticmethod
    def error(message):
        log = Loger.custom_logger(loglevel=logging.ERROR)
        return log.error(message)

    @staticmethod
    def critical(message):
        log = Loger.custom_logger(loglevel=logging.CRITICAL)
        return log.critical(message)



'''
def cust_log(self, level, message, file):
    logging.basicConfig(level=logging.INFO, filename=file, filemode="w",
                        format="%(asctime)-12s%(levelname)s%(message)s",
                        datefmt="%d-%m-%Y %H:%M:%S")
    if level == "INFO": logging.info(message)
    if level == "WARNING": logging.info(message)
    if level == "ERROR": logging.info(message)
    if level == "CRITICAL": logging.info(message)'''