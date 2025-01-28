import logging
import os
from logging.handlers import RotatingFileHandler
import colorlog

LOG_DIR = 'logs'
LOG_FILE = os.path.join(LOG_DIR, 'organizer.log')

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

log_handler = RotatingFileHandler(LOG_FILE, maxBytes=5 * 1024 * 1024, backupCount=3)  # 5 MB max, 3 backups
log_handler.setLevel(logging.DEBUG)

log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
log_handler.setFormatter(log_formatter)

logging.getLogger().addHandler(log_handler)
logging.getLogger().setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

colored_formatter = colorlog.ColoredFormatter(
    '%(asctime)s - %(log_color)s%(levelname)s%(reset)s - %(message)s',
    log_colors={
        'DEBUG': 'blue',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'bold_red',
    }
)
console_handler.setFormatter(colored_formatter)

logging.getLogger().addHandler(console_handler)

def log_activity(message):
    """Logs an activity message (INFO level)."""
    logging.info(message)

def log_error(message):
    """Logs an error message (ERROR level)."""
    logging.error(message)

def log_warning(message):
    """Logs a warning message (WARNING level)."""
    logging.warning(message)

def log_debug(message):
    """Logs a debug message (DEBUG level)."""
    logging.debug(message)

def log_critical(message):
    """Logs a critical error message (CRITICAL level)."""
    logging.critical(message)
