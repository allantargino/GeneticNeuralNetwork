import math
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import r2_score

# Parameters:
train_perc = 0.8

# Data:
x = [[0., 0.], [1., 1.], [2., 2.], [3., 3.], [4., 4.], [5., 5.], [6., 6.], [7., 7.]]
y = [0., 1., 2., 3., 4., 5., 6., 7.]

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
                    hidden_layer_sizes=(3,),
                    max_iter=200, learning_rate_init=1e-3,
                    random_state=7)

# Train the network:
clf.fit(train_data,train_labels)

# Scores the validation set:
scored_labels = clf.predict(test_data)

# Outputs the results:
print 'R^2:'
print r2_score(test_labels, scored_labels)



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