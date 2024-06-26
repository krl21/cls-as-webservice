
# from logic.dataset.numbers import load, number2remainder
# from logic.classifier import MyClassifier


# data = load((1000, 2000, 1), (1, 100, 1))

# dir_path = './models'


# cls = MyClassifier()
# cls.build_models(data)
# # cls.save_models(dir_path)
# # cls.load_models(dir_path)

# f = lambda x: [number2remainder(v) for v in x]
# print('4:', cls.predict(4, f))
# print('5:', cls.predict(5, f))
# print('3:', cls.predict(3, f, 'decision_tree'))
# print('30:', cls.predict(30, f, 'knn'))

# print('Hello you!')

'''
consola
curl -X POST  -H"Content-Type: application/json" -d'{ "operacion": "suma", "valor1": 10, "valor2": 5 }' http://127.0.0.1:8000/api_classifier/

'''