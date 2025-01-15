# file_detector.py

import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from file_organizer import organize_file  # Ensure this import is correct

class FileDownloadHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        # Trigger the file organization as soon as a new file is detected
        organize_file(event.src_path)

def start_monitoring(path):
    event_handler = FileDownloadHandler()
    observer = Observer()
    observer.schedule(event_handler, path=path, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
