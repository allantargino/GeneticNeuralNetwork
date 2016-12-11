import math
from sklearn.neural_network import MLPRegressor

def int_to_bin_vec(int_num, max_length):
    binary = bin(int_num)
    binary_vec = list(binary[2:])
    if  len(binary_vec) > max_length:
        return []
    if len(binary_vec) < max_length:
        temp = []
        for i in range(0,(max_length- len(binary_vec))):
            temp +='0' 
        binary_vec = temp + binary_vec
    return binary_vec

def bin_vec_to_int(bin_vec):
    str_num = '0b' + ''.join(bin_vec)
    int_num = int(str_num, 2)
    return int_num


# X = [[0., 0.], [1., 1.], [2., 2.], [3., 3.]]
# y = [0., 1., 2., 3.]
# clf = MLPRegressor(solver='lbfgs', alpha=1e-4, hidden_layer_sizes=(3,), max_iter=200, learning_rate_init=1e-3, verbose='false', random_state=7)

# clf.fit(X, y)
# # # result = clf.predict([[2., 2.], [-1., -2.]])
# print 'Result'
# print clf.predict([[2.3, 2.3]])
# # print result
# # print 'Coefs'
# # print clf.coefs_
# # print 'Bias'
# # print clf.intercepts_
# # print 'Layers'
# # print clf.n_layers_ 