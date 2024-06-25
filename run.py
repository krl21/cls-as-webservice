
# import numbers_dataset
# from code import MyClassifier
# from . import numbers_dataset
# from dataset import numbers_dataset

# print(help(numbers_dataset.load))
from dataset import numbers as numbers_dataset

# cls = MyClassifier()
print(numbers_dataset.load((10, 15, 1), (1, 2, 1)))

# cls.build_models(numbers_dataset.load(1, 100, 1, 1, 100, 1))

print('Hello you!')
