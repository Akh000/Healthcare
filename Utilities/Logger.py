import inspect
import logging


class LogGenerator:
    @staticmethod
    def loggen():
        name = inspect.stack()[1][3]
        logger = logging.getLogger(name)
        logfile = logging.FileHandler("D:\\Python\\Revision 1\\OpenCart-Pytest\\Logs\\herokuapp.log")
        for_mat = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(lineno)s : %(message)s")
        logfile.setFormatter(for_mat)
        logger.addHandler(logfile)
        logger.setLevel(logging.INFO)
        return logger
