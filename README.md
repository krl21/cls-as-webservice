# cls-as-webservice

Simple project to classify integers.

## Table of Contents
- [cls-as-webservice](#cls-as-webservice)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
  - [Installation](#installation)
  - [Usage](#usage)
    - [API Endpoints](#api-endpoints)
      - [List](#list)
      - [Predict](#predict)
  - [Testing](#testing)

## Description

The project provides an API to classify integers. The classification is given as follows:
- `Fizz` if the number is divisible by 3.
- `Buzz` if the number is divisible by 5.
- `FizzBuzz` if the number is divisible by 3 and 5.
- `None` otherwise.

Some classification models from the [scikit-learn](https://scikit-learn.org/stable/index.html) library are used for classification. The models used were:
- Logistic regression
- SVC 
- Decision tree 
- Random forest 
- KNN 
- Naive Bayes
  
During training, the continuous interval of integers from $1000$ to $2000$ was used and using **k-fold** ($k=10$) the performance of each one was evaluated, using the accuracy measure. Then, the best models were evaluated with the interval from 1 to 100 to obtain the final accuracy metric.

The metrics are displayed in the console, while the server loads.

## Installation

The project was developed using Python version 3.10 and the Django framework.

Create a clone project and install the necessary dependencies. To do this you can copy and execute the following commands in the console:

```shell
python --version
git clone https://github.com/krl21/cls-as-webservice.git
cd cls-as-webservice
pip install -r requirements.txt
```

## Usage

The project only has two services, which complement each other. To activate the server, run the following command:
```shell
./startup.sh
```

If you get error, try running the following commands before:
```shell
chmod 777 ./startup.sh
chmod 777 ./start_test.sh
```

### API Endpoints

#### List

> **GET api/number-classifier/list_models/** 
  
  * Description: Allows you to consult the models used to classify. With this, you can restrict yourself to one model when classifying.

  * Answer:
    * 200 (success): The request was completed successfully.

  * Response body (JSON):
    * `success`: Indicates the general status of the operation.
      * Type: Boolean
      * Value:
        * True: The operation was successful.
        * False: The operation failed.
    * `result`: Contains the result of the operation.
      * Type: Object
      * Value:
        * `models`: List of names of the learning models managed by the system.
          * Type: List of string
          * Values ​​(possible, you don't have to have all of them):
            * "logistic_regression"
            * "svc"
            * "decision_tree"
            * "random_forest"
            * "knn"
            * "naive_bayes"
  
  * Example:
    Open a console and copy the following command:
    ```shell
    curl -X GET http://127.0.0.1:8000/api/number-classifier/list_models/
    ```

    And you will get:
    ```
    {"success": true, "result": {"models": ["logistic_regression", "svc", "decision_tree", "random_forest", "knn", "naive_bayes"]}}
    ```

#### Predict

> **POST api/number-classifier/predict/:** 

  * Description: Requests the classification of several integers.

  * Answer:
    * 200 (success): The request completed successfully.
    * 400 (bad request): The request contains invalid JSON.
  
  * Request body (JSON):
    * `values`: Indicates the numerical values ​​to be classified.
      * Value: List of integers.
      * Required: Yes
    * `model_name`: Indicates the classification model to use. It has to match one of the available ones (see [api](#list)).
      * Value: String
      * Required: No. If defined, forces the system to only classify with that one, otherwise the most common classification of all classifiers is returned, which is generally the same.

  * Response body (JSON):
    * `success`: Indicates the general status of the operation.
      * Type: Boolean
      * Values:
        * True: The operation was successful.
        * False: The operation failed by internal error from the user data.
    * `result`: Contains the result of the operation.
      * Type: Object
        * `classification`: List of ordered pairs representing the classification of the required numbers.
          * Type: List of lists. Each internal array has two elements:
            * First: Integer that represents the number to be classified.
            * Second: Text string indicating the classification of the number. Possible values ​​are: `"Fizz"`, `"Buzz"`, `"FizzBuzz"` and `"None"`.
  
  * Example:
    Open a console and copy the following command:
    ```shell
    curl -X POST \
      -H"Content-Type: application/json" \
      -d'{"values": [0, 1, 2, 3, 4, 5]}' \
      http://127.0.0.1:8000/api/number-classifier/predict/
    ```

    And you will get:
    ```
    {"success": true, "result": {"classification": [[0, "FizzBuzz"], [1, "None"], [2, "None"], [3, "Fizz"], [4, "None"], [5, "Buzz"]]}}
    ```

## Testing

You can run the defined tests by copying the following code into the console:

```shell
./start_test.sh
```
