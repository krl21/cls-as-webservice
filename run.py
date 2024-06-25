
from dataset import numbers as numbers_dataset
from classifier import MyClassifier

data = numbers_dataset.load((10, 15, 1), (1, 2, 1))

cls = MyClassifier()
cls.build_models(data)

print(list(cls.models.items()))

print('Hello you!')
