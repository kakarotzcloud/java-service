import logging
import try_catch_

logging.basicConfig(filename='logging_example.log', level = logging.DEBUG ,format='%(asctime)s - %(levelname)s - %(name)s - %(message)s')

try:
    f = open('app1.log')
except Exception as e:
    logging.info(e)