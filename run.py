
from dataset.numbers import load, number2remainder
from classifier import MyClassifier


data = load((10, 15, 1), (1, 2, 1))

dir_path = './models'


cls = MyClassifier()
# cls.build_models(data)
# cls.save_models(dir_path)
cls.load_models(dir_path)

f = lambda x: [number2remainder(v) for v in x]
print('4:', cls.predict(4, f))
print('5:', cls.predict(5, f))
print('3:', cls.predict(3, f))
print('30:', cls.predict(30, f))

print('Hello you!')



