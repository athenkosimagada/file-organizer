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

def move_file_to_target(file_path, max_retries=3, delay=2):
    """Move the file to the appropriate folder based on its extension."""
    if not os.path.exists(file_path):
        log_activity(f"File not found: {file_path}")
        return

    log_activity(f"File found: {file_path}")

    file_name = os.path.basename(file_path)
    ext = os.path.splitext(file_name)[-1].lower().lstrip('.')

    folder_name = FILE_TYPES.get(ext, 'Others')
    target_path = os.path.join(TARGET_DIR, folder_name)

    os.makedirs(target_path, exist_ok=True)

    unique_file_name = get_unique_filename(target_path, file_name)

    try:
        shutil.move(file_path, os.path.join(target_path, unique_file_name))
        log_activity(f'Moved: {file_path} to {target_path}')
    except Exception as e:
        log_error(f"Failed to move {file_path}: {e}")


class DownloadHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return

        file_path = event.src_path
        log_debug(f"Detected new file: {file_path}")

        while True:
            if not os.path.exists(file_path):
                log_warning(f"File may have been moved or deleted: {file_path}")
                return

            if is_file_downloaded(file_path) and not is_temp_file(file_path):
                log_activity(f"File downloaded: {file_path}")
                move_file_to_target(file_path)
                return
            
            log_warning(f"File still downloading: {file_path}")
            time.sleep(5)


def main():
    observer = Observer()
    handler = DownloadHandler()

    observer.schedule(handler, DOWNLOAD_DIR, recursive=True)
    observer.start()

    try:
        log_activity(f"Started monitoring {DOWNLOAD_DIR}")
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        log_activity("Stopping the observer...")
        observer.stop()
    except Exception as e:
        log_error(f"Unexpected error: {e}")
    finally:
        observer.join()

if __name__ == "__main__":
    main()