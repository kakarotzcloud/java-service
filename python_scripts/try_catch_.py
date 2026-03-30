# import logging

# logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(name)s - %(message)s')

# def read_file(file_name):
#     try:
#         f = open(file_name)
#     except Exception as e:
#         logging.exception(e)
#     else:
#         # file_content = f.read(80)
#         logging.info(f"file opened")
#     finally:
#         try:
#             f.close()
#             logging.info("File closed successfully")
#         except Exception as e:
#             logging.exception(e)

# __main__ = read_file('app.log')



import logging
from logging.handlers import RotatingFileHandler
import os

# -------------------------------
# Logger Configuration
# -------------------------------
def setup_logger(name: str, log_file: str, level=logging.INFO):
    formatter = logging.Formatter(
        '%(asctime)s | %(levelname)s | %(name)s | %(filename)s:%(lineno)d | %(message)s'
    )

    # Log rotation (10 MB per file, keep 5 backups)
    handler = RotatingFileHandler(log_file, maxBytes=10*1024*1024, backupCount=5)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers
    if not logger.handlers:
        logger.addHandler(handler)

    return logger


logger = setup_logger("file_reader", "app.log")


# -------------------------------
# Business Logic
# -------------------------------
def read_file(file_name: str):
    logger.info("Starting file read operation", extra={"file_name": file_name})

    if not os.path.exists(file_name):
        logger.error("File does not exist", extra={"file_name": file_name})
        return None

    try:
        with open(file_name, 'r') as f:
            content = f.read(80)
            logger.info("File read successfully", extra={"file_name": file_name})
            return content

    except IOError as e:
        logger.exception("IO error while reading file", extra={"file_name": file_name})

    except Exception:
        logger.exception("Unexpected error occurred", extra={"file_name": file_name})


# -------------------------------
# Entry Point
# -------------------------------
if __name__ == "__main__":
    read_file("app1.log")