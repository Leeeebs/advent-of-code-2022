import logging


def create_logger(name: str) -> logging.Logger:
    """
    Set up a custom logger.

    Returns:
        logging.Logger: A logger set to print all messages levels to the console.
    """
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(
        logging.Formatter(
            fmt="| {asctime} | {levelname:^8s} | {name:^15s} | {message}",
            datefmt="%H:%M:%S %d-%m-%y",
            style="{",
        )
    )
    logger = logging.getLogger(name)
    logger.addHandler(console_handler)
    logger.setLevel(logging.DEBUG)

    return logger

