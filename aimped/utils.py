import json
import logging


def get_logger(log_file='Kserve-Glowol.log', log_level=logging.DEBUG):
    """Returns the logger object for logging the output of the server.
    Parameters:
    ----------------
    log_file: str
        The name of the log file to which the logs will be written.
    log_level: int
        The logging level (e.g., logging.DEBUG, logging.INFO, logging.ERROR).  
    Returns:
    ----------------
    logger: logging.Logger
        The configured logger object.
    """
    # Create a FileHandler for writing logs to the specified log_file.
    f_handler = logging.FileHandler(log_file, encoding='utf-8', mode='w')
    # Define a log message format.
    formatter = logging.Formatter('[%(asctime)s %(filename)s:%(lineno)s] - %(message)s')
    # Set the formatter for the file handler.
    f_handler.setFormatter(formatter)
    # Set the logging level for the file handler.
    f_handler.setLevel(log_level)
    # Get the root logger.
    logger = logging.getLogger()
    # Set the logging level for the logger itself.
    logger.setLevel(log_level)
    # Add the file handler to the logger.
    logger.addHandler(f_handler)
    return logger