
import numpy as np

from typing import TypeVar
T = TypeVar('T')


def load(train_parameters: tuple[int, int, int], test_parameters: tuple[int, int, int], preprocess : callable = None) -> tuple[np.ndarray[T], np.ndarray[str], np.ndarray[T], np.ndarray[str]]:
    """Loads data from a source based on train and test data ranges.

    Args:
        train_parameters (tuple[int, int, int]): A tuple representing the training data range (start, end, step).
        test_parameters (tuple[int, int, int]): A tuple representing the testing data range (start, end, step).
        preprocess (function, optional): A function for data preprocessing and representing. Defaults to None. if the value is None, the `number2remainder` function will be taken to represent the values.
        
    Raises: 
        ValueError: Invalid train data range. Start index cannot be greater than end index with a positive step or vice versa.
        ValueError: Invalid test data range. Start index cannot be greater than end index with a positive step or vice versa.

    Returns:
        tuple[np.array[Any], np.array[str], np.array[Any], np.array[str]]: 
            A tuple containing four elements:
                - Training data (list of values)
                - Training labels (list of strings)
                - Testing data (list of values)
                - Testing labels (list of strings)
    """
    if (train_parameters[0] > train_parameters[1] and train_parameters[2] > 0) or \
       (train_parameters[0] < train_parameters[1] and train_parameters[2] < 0):
        raise ValueError('Invalid train data range. Start index cannot be greater than end index with a positive step or vice versa.')
    
    if (test_parameters[0] > test_parameters[1] and test_parameters[2] > 0) or \
       (test_parameters[0] < test_parameters[1] and test_parameters[2] < 0):
        raise ValueError('Invalid test data range. Start index cannot be greater than end index with a positive step or vice versa.')
    
    if preprocess is None: 
        preprocess = number2remainder
        
    return _load(train_parameters, test_parameters, preprocess)

def _load(train_parameters: tuple[int, int, int], test_parameters: tuple[int, int, int], preprocess : callable) -> tuple[np.ndarray[T], np.ndarray[str], np.ndarray[T], np.ndarray[str]]:
    """Loads data from a source based on train and test data ranges.

    Args:
        train_parameters (tuple[int, int, int]): A tuple representing the training data range (start, end, step).
        test_parameters (tuple[int, int, int]): A tuple representing the testing data range (start, end, step).
        preprocess (function, optional): A function for data preprocessing and representing. Defaults to None. if the value is None, the `number2remainder` function will be taken to represent the values.

    Returns:
        tuple[np.array[Any], np.array[str], np.array[Any], np.array[str]]: 
            A tuple containing four elements:
                - Training data (list of values)
                - Training labels (list of strings)
                - Testing data (list of values)
                - Testing labels (list of strings)
    """
    
    training_values = [i for i in range(train_parameters[0], train_parameters[1] + 1, train_parameters[2])]
    test_values = [i for i in range(test_parameters[0], test_parameters[1] + 1, test_parameters[2])]
    
    return np.array([preprocess(i) for i in training_values]), \
        np.array([_classify(i) for i in training_values]), \
        np.array([preprocess(i) for i in test_values]), \
        np.array([_classify(i) for i in test_values])


def _classify(n: int) -> str:
    """Classifies a number based on predetermined rules

    Args:
        n (int): The number to classify.

    Return:
        str: The classification string ("Fizz", "Buzz", "FizzBuzz", or "None")
    """
    return 'FizzBuzz' if n % 15 == 0 \
        else 'Fizz' if n % 3 == 0 \
        else 'Buzz' if n % 5 == 0 \
        else 'None'


def number2remainder(n :int) -> list[bool, bool]:
    """Check if a number is divisible by 3 and 5.

    Arg:
        n (int): The integer for which to calculate the remainders.

    Returns:
        list[bool, bool]: A list containing the remainders of `n`.
    """
    return [n % 3 == 0, n % 5 == 0]
