import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MainPyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith('main.py'):
            print("\n--- File changed, running main.py ---")
            subprocess.run(['python3', 'main.py'])
            print("\n--- Waiting for changes ---")

def watch_main():
    event_handler = MainPyHandler()
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=False)
    observer.start()

    print("Watching main.py for changes... Press Ctrl+C to stop")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    watch_main()
