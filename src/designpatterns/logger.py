import logging

logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")

console_handler = logging.StreamHandler()
file_handler = logging.FileHandler("output.log", mode="w", encoding="utf-8")

logger.addHandler(console_handler)
logger.addHandler(file_handler)

formatter = logging.Formatter(
    "[{asctime}]: {levelname}: {message}", style="{", datefmt="%Y-%m-%d %H:%M"
)

console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

console_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.INFO)
