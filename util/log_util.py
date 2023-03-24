from datetime import datetime
import logging
from os import path
from os import mkdir
import sys

# Import project folder.
_tmp_path = path.dirname(__file__)
_tmp_path = path.join(_tmp_path, '..')
sys.path.append(_tmp_path)
from util import file_util

logger: logging.Logger or None = None
_log_folder = "Logs"


def init_logger(root_path: str, project_name, is_debug: bool = False):
    global logger
    logger = logging.getLogger(project_name)

    # Set level.
    if is_debug:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

    # Initialize folders.
    log_path = path.join(root_path, _log_folder)
    if not path.exists(log_path):
        mkdir(log_path)

    tmp_name = datetime.now()
    tmp_name = tmp_name.strftime('%Y-%m%d_%H%M-%S')
    log_path = path.join(log_path, tmp_name)
    mkdir(log_path)

    tmp_name = file_util.convert_file_name(project_name)
    tmp_name = tmp_name + ".log"
    log_path = path.join(log_path, tmp_name)

    # Initialize File Handler.
    handler = logging.FileHandler(log_path)
    logger.addHandler(handler)
    fmt = '%(asctime)s\t%(processName)s[%(process)d]\t%(threadName)s[%(thread)d]'
    fmt += '\t%(filename)s\tLine%(lineno)d\t[%(levelname)s]\t%(message)s'
    fmt = logging.Formatter(fmt)
    handler.setFormatter(fmt)

    # Initialize Console Handler.
    handler = logging.StreamHandler()
    logger.addHandler(handler)
    handler.setFormatter(fmt)
