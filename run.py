
from dataset import numbers as numbers_dataset
from classifier import MyClassifier

data = numbers_dataset.load((10, 15, 1), (1, 2, 1))

dir_path = './models'


cls = MyClassifier()
# cls.build_models(data)
# cls.save_models(dir_path)
cls.load_models(dir_path)

print('Hello you!')

