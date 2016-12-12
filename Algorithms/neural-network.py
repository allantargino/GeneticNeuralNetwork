import math
import csv
import os
import numpy as np
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import r2_score

def MLP():
    # Data sampling:
    x_len = len(x)
    n_elem = int(math.floor(x_len*train_perc))

    train_data = x[0:n_elem]
    train_labels = y[0:n_elem]
    test_data = x[n_elem:x_len]
    test_labels = y[n_elem:x_len]

    # Regression using neural network:
    clf = MLPRegressor(solver='lbfgs',
                        alpha=1e-4,
                        hidden_layer_sizes=(10,),
                        max_iter=200, learning_rate_init=1e-3,
                        verbose='false')

    # Train the network:
    clf.fit(train_data,train_labels)

    # Scores the validation set:
    scored_labels = clf.predict(test_data)

    # Outputs the results:
    r2= r2_score(test_labels, scored_labels)
    print 'R^2:'
    print r2
    return r2

def get_Apartamentos():
    script_dir = os.path.dirname(__file__)
    rel_path = "../Datasets/apartamentos_mini.csv"
    filename = os.path.join(script_dir, rel_path)
    filename = os.path.abspath(os.path.realpath(filename))

    apartamentos = []
    with open(filename, 'rb') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            apartamentos+=[[int(row['min_area']), float(row['latitude_formatada']), float(row['longitude_formatada']), int(row['quant_quartos']), int(row['quant_vagas']), int(row['quant_suites']), float(row['price'])]]
    return apartamentos



#------------------------------------------------------------------------------------------------
# Parameters:
train_perc = 0.8

apt = get_Apartamentos()
array_apt = np.array(apt)

x = list(array_apt[:,[0, 1, 2, 3, 4, 5]])
y = list(array_apt[:,6])

# print 'apt[0]'
# print apt[0]
# print 'x[0]'
# print x[0]
# print 'y[0]'
# print y[0]

# # Data:
# x = [[0., 0.], [1., 1.], [2., 2.], [3., 3.], [4., 4.], [5., 5.], [6., 6.], [7., 7.]]
# y = [0., 1., 2., 3., 4., 5., 6., 7.]
MLP()

#print test_data
#print scored_labels
# print 'Result'
# print clf.predict([[2.3, 2.3]])
# # print result
# # print 'Coefs'
# # print clf.coefs_
# # print 'Bias'
# # print clf.intercepts_
# # print 'Layers'
# # print clf.n_layers_ 