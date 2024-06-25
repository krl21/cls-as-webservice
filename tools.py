
import os

def create_directory(directory_path: str) -> None:
    """
    Creates a directory recursively if it does not exist.

    Args:
        directory_path (str): The path of the directory to be created.
        
    """
    if not os.path.exists(directory_path):
        try:
            os.makedirs(directory_path)
            print(f"Directory created: {directory_path}")
        except OSError as error:
            print(f"Failed to create directory: {error}")