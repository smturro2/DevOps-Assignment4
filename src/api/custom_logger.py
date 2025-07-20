from typing import Dict, Any
import pathlib
import datetime
import logging

logger = logging.getLogger(__name__)

logger_config = {
    'overall_level': logging.DEBUG,
    'format': 'LOGGER - %(asctime)s - %(name)s - %(levelname)s - %(message)s',
    'console_level': logging.DEBUG,
    'file': False,
    'file_level': logging.DEBUG,
    'log_folder': 'logs'
}

logger.setLevel(logger_config['overall_level'])
formatter = logging.Formatter(logger_config['format'])

# Create console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logger_config['console_level'])
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# Create file handler if file is specified
if logger_config['file']:
    
    # Determine file path and make folder
    file_path = pathlib.Path(logger_config['log_folder']) / f"{datetime.datetime.now().strftime('%Y%m%d_%H%M')}.log"
    file_path.parent.mkdir(parents=True, exist_ok=True)

    # Create file handler
    file_handler = logging.FileHandler(file_path)
    file_handler.setLevel(logger_config['file_level'])
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)