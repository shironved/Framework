# utils/logger.py
import logging

def setup_logger(name, logfile='logs/framework.log'):
    logging.basicConfig(
        filename=logfile,
        filemode='a',
        format='%(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )
    logger = logging.getLogger(name)
    return logger
