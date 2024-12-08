import logging


def get_logger(name: str) -> logging.Logger:
  logger = logging.getLogger(name)
  logging.basicConfig(level=logging.INFO,
                      # filename='bot_log.log',
                      format="[%(asctime)s] - [%(levelname)s] - "
                                 "%(funcName)s:%(lineno)d - %(message)s",
                      datefmt='%d-%m-%y %H:%M:%S')
  return logger