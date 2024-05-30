import pickle

data = pickle.load(open(r'sample.pickle','rb'))
print(data.keys())