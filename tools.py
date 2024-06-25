
import os
from collections import Counter

from typing import TypeVar
T = TypeVar('T')


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
            

def most_frequent(data: list[T]) -> T:
    """
    Finds the most frequent value in a list using the `collections.Counter` class.

    Args:
        data (list[T]): 
            The input list of values.

    Returns:
        T: 
            The most frequent value.
            
    """
    counter = Counter(data)
    most_common_element = counter.most_common(1)[0]
    return most_common_element[0]

