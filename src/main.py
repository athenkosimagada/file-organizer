import os
import shutil
import time
import sys

from file_types import FILE_TYPES
from logger import log_activity, log_error, log_warning, log_debug
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from utils import is_file_downloaded, is_temp_file, get_unique_filename

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config.settings import DOWNLOAD_DIR, TARGET_DIR

is_file_path_already_moved = False

def move_file_to_target(file_path):
    """Move the file to the appropriate folder based on its extension."""
    if not os.path.exists(file_path):
        log_activity(f"Listening for new files in {DOWNLOAD_DIR}")
        return
    else:
        log_activity(f"File found: {file_path}")
    
    if is_temp_file(file_path):
        log_warning(f"Skipping temporary file: {file_path}")
        return
    
    if not is_file_downloaded(file_path):
        log_warning(f"Skipping {file_path} as it's still being downloaded")
        return
    
    ext = file_path.split('.')[-1]
    folder_name = FILE_TYPES.get(ext, 'Others')
    target_path = os.path.join(TARGET_DIR, folder_name)

    os.makedirs(target_path, exist_ok=True)

    file_name = os.path.basename(file_path)
    unique_file_name = get_unique_filename(target_path, file_name)

    try:
        # Move the file to the target directory
        shutil.move(file_path, os.path.join(target_path, unique_file_name))
        is_file_path_already_moved = True
        log_activity(f'Moved: {file_path} to {target_path}')
    except Exception as e:
        log_error(f"Failed to move {file_path}: {e}")

extensions = {item.split('.')[-1] for item in os.listdir(TARGET_DIR) if os.path.isfile(os.path.join(TARGET_DIR, item))} 

class DownloadHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        file_path = event.src_path

        time.sleep(1)

        log_debug(f"Detected new file: {file_path}")
        move_file_to_target(file_path)

observer = Observer()
handler = DownloadHandler()

observer.schedule(handler, DOWNLOAD_DIR, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()