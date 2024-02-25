import os
import datetime
from typing import List

class File:
    """
    Represents a file in the vault
    """

    def __init__(self, path: str) -> None:
        self.path = path
        pass

    def get_file(self) -> str:
        """
        Read all the contents of the file and return it as a string
        """
        with open(self.path, "r") as file:
            return file.read()

    def write_file(self, content: str) -> None:
        """
        Write the content to the file
        """
        with open(self.path, "w") as file:
            file.write(content)


class Vault:
    """
    The representation of an obsidian vault
    """

    def __init__(self, path: str) -> None:
        self.full_path = path
        self.files = []
        self._read_files()
        pass

    def _read_files(self) -> None:
        # read all files recursively in the vault into a file object
        exclude_dirs = [".obsidian", ".stversions", ".trash"]
        for root, dirs, files in os.walk(self.full_path):
            # remove the excluded directories
            dirs[:] = [d for d in dirs if d not in exclude_dirs]
            for file in files:
                file_path = os.path.join(root, file)
                self.files.append(File(file_path))

    def get_old_daily_notes(self) -> List[File]:
        """
        Get the old daily notes
        """
        daily_notes_dir = "01 - daily notes"  # Directory containing daily notes
        current_date_str = datetime.datetime.now().strftime("%Y-%m-%d")  # Get the current date as a string
        old_notes = []  # Initialize an empty list to store old notes
        for file in self.files:
            if daily_notes_dir in file.path and current_date_str not in file.path:  # Check conditions
                old_notes.append(file)  # Append the file to the list if it meets the conditions
        return old_notes  # Return the list of old notes



if __name__ == "__main__":
    vault = Vault(input())
    files = vault.get_old_daily_notes()
    for file in files:
        print(file.path)
