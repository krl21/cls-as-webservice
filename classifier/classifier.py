

import numpy as np

import pickle
from os import path
from os import listdir

from sklearn.model_selection import KFold

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB 

from sklearn.metrics import accuracy_score

from typing import TypeVar
T = TypeVar('T')
R = TypeVar('R')

from tools import create_directory


class MyClassifier: 
    
    def __init__(self):
        self.model_names = ['logistic_regression', 'svc', 'decision_tree', 'random_forest', 'knn', 'naive_bayes']
        self.models = dict()
    
    def build_models(self, dataset: tuple[np.ndarray[T], np.ndarray[R], np.ndarray[T], np.ndarray[R]]):
        """Builds and evaluates different machine learning models using K-fold cross-validation.
        
        This function performs basic data validation and then delegates the actual model building and evaluation to the function.

        Args:
            dataset (tuple[np.ndarray[T], np.ndarray[R], np.ndarray[T], np.ndarray[R]]):
                A tuple containing training data (X_train, y_train) and testing data (X_test, y_test).

        Raise:
            ValueError: 
                If the lengths of the data arrays within the dataset are not equal (indicating inconsistencies).

        """
        if len(dataset[0]) != len(dataset[1]) or len(dataset[2]) != len(dataset[3]):
            raise ValueError("Dataset lists must have equal dimensions.")

        return self._build_models(dataset)
    
    def _build_models(self, dataset: tuple[np.ndarray[T], np.ndarray[R], np.ndarray[T], np.ndarray[R]]) -> None:
        """
        Builds and evaluates different machine learning models using K-fold cross-validation.

        Args:
            dataset (tuple[np.ndarray[T], np.ndarray[R], np.ndarray[T], np.ndarray[R]]):
                A tuple containing training data (X_train, y_train) and testing data (X_test, y_test).
            
        """
        kfold = KFold(n_splits=5, shuffle=True, random_state=42)
        
        print('### BUILDING MODELS ###')
        for model_name in self.model_names:
            self._evaluate_model(model_name, *dataset[:2])
            self._train_model(model_name, dataset)
            print('')
        
    def _evaluate_model(self, model_name: str, X_train: np.ndarray[T], y_train: np.ndarray[R]) -> None:
        """
        Evaluates the accuracy of the model using K-fold cross-validation.

        Args:
            model_name (str): 
                The name of the model to be evaluated.
            X_train (np.ndarray[T]): 
                Training data features.
            y_train (np.ndarray[R]): 
                Training data labels.

        """
        kfold = KFold(n_splits=min(10, len(X_train)), shuffle=True, random_state=42)
            
        accuracies = []
            
        for train_index, test_index in kfold.split(X_train):
            model = initialize_model(model_name)
            
            Xtrain = X_train[train_index]
            ytrain = y_train[train_index]
            Xtest = X_train[test_index]
            ytest = y_train[test_index]

            model.fit(Xtrain, ytrain)

            accuracies.append(accuracy_score(ytest, model.predict(Xtest)))

        print(f'  Using K-fold. Model: {model_name}. Average accuracy: {np.mean(accuracies)}')
            
    def _train_model(self, model_name: str, dataset: tuple[np.ndarray[T], np.ndarray[R], np.ndarray[T], np.ndarray[R]]) -> None:
        """Trains a model using the provided dataset.

        Args:
            model_name (str): 
                The name of the model to be trained.
            dataset (tuple[np.ndarray[T], np.ndarray[R], np.ndarray[T], np.ndarray[R]]): 
                A tuple containing training data (X_train, y_train) and testing data (X_test, y_test).

        """
        X_train, y_train, X_test, y_test = dataset
        
        model = initialize_model(model_name)
        model.fit(X_train, y_train)
        
        print(f'  Using original test data. Model: {model_name}. Accuracy: {accuracy_score(y_test, model.predict(X_test))}')
        
        self.models[model_name] = model

    def save_models(self, dir_path: str) -> None:
        """
        Saves the trained models to the specified directory

        Args:
            dir_path (str): 
                The path of the directory to save the models.

        Raises:
            OSError: 
                If an error occurs while creating the directory or saving the models.
            
        """
        create_directory(dir_path)
        
        for model_name, model in self.models.items():
            name = model_name + '.pkl'
            with open(path.join(dir_path, name), 'wb') as f:
                pickle.dump(model, f)
    
    def load_models(self, dir_path: str) -> None:
        """
        Loads trained models from the specified directory

        Args:
            dir_path (str): 
                The path of the directory containing the saved models.

        Raises:
            OSError: 
                If an error occurs while loading the models.
            FileNotFoundError: 
                If a model file is not found for a given model name.
            
        """
        for filename in listdir(dir_path):
            if filename.endswith('.pkl'):
                model_name, _ = path.splitext(filename)
                with open(path.join(dir_path, filename), 'rb') as f:
                    model = pickle.load(f)
                    self.models[model_name] = model
        


def initialize_model(model_name: str) -> callable:
    """Initializes a machine learning model based on the provided name.

    Args:
        model_name (str): 
            The name of the model to be initialized.

    Raises:
        ValueError: 
            If the provided model name is not supported.

    Returns:
        callable: 
            A newly initialized model object.
        
    """    
    if model_name == 'logistic_regression':
        return LogisticRegression(random_state=42, n_jobs=4) 
    
    elif model_name == 'svc':
        return SVC()

    elif model_name == 'decision_tree':
        return DecisionTreeClassifier(random_state=42) 

    elif model_name == 'random_forest':
        return RandomForestClassifier(random_state=42) 

    elif model_name == 'knn':
        return KNeighborsClassifier(n_neighbors=1, n_jobs=4) 

    elif model_name == 'naive_bayes':
        return GaussianNB()

    else:
        raise ValueError(f"Unsupported model name: {model_name}")


 