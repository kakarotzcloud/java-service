import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', filename='log.txt')

try:
    def main():
        logging.debug("This is the main function of the first module.")
    if __name__ == '__main__':
        logging.debug(main())

except Exception as e:
    logging.exception("An error occurred: {}".format(e))