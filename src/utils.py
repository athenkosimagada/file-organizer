import os
import time
from file_types import TEMP_EXTENSIONS
from logger import log_error

def is_temp_file(file_path):
    """Check if the file has a temporary extension like .tmp, .crdownload, etc."""
    file_name, ext = os.path.splitext(file_path)
    return ext.lower() in TEMP_EXTENSIONS

def is_file_downloaded(file_path, max_retries=5, delay=1):
    """Check if the file is still being written to (downloaded)."""
    try:
        retries = 0
        while retries < max_retries:
            initial_size = os.path.getsize(file_path)
            time.sleep(delay)
            final_size = os.path.getsize(file_path)

            if initial_size == final_size:
                return True

            retries += 1

        return False
    except Exception as e:
        log_error(f"Error while checking file size: {e}")
        return False

def get_unique_filename(target_path, file_name):
    """Generate a unique file name if the file already exists in the target folder."""
    base_name, ext = os.path.splitext(file_name)
    counter = 1
    # Keep generating a new filename until we find one that doesn't exist
    while os.path.exists(os.path.join(target_path, file_name)):
        file_name = f"{base_name}_{counter}{ext}"
        counter += 1
    return file_name
