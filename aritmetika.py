import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('aritmetika.log')
logger.addHandler(file_handler)

logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
file_handler.setFormatter(formatter)


def dalyba(a, b):
    return a / b


a = 10
b = 5

padalinom = dalyba(a, b)
logger.info(f"Dalyba: {a} / {b} = {padalinom}")
