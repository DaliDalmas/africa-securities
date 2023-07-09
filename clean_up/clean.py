import os
from pathlib import Path


class Clean:
    def __init__(self, path) -> None:
        self.path = path

    def remove(self):
        if os.path.isfile(self.path):
            os.remove(self.path)
            print(f"{self.path} file deleted")

        else:
            # If it fails, inform the user.
            print(f"Error: %s file not found {self.path}")