import logging

log = '%(lineno)d -- %(asctime)s -- %(message)s'
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG, format=log, filemode='w')
logging.debug("This is a debug")
logging.info("This is a info")
logging.warning("This is a warning")
logging.error("This is a Error")
logging.critical("This is a critical")

