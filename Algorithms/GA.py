import math
import Queue as Q
from random import shuffle, randrange, randint, choice, random
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import r2_score

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

def MLP(seed, train_perc):
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
                        random_state=seed)

    # Train the network:
    clf.fit(train_data,train_labels)

    # Scores the validation set:
    scored_labels = clf.predict(test_data)

    # Outputs the results:
    r2= r2_score(test_labels, scored_labels)
#     print 'R^2:'
#     print r2
    return r2

def split_list(lista, idx):
        l1=[]
        l2=[]
        for i in range(idx):
             l1+=[lista[i]]
        for i in xrange(idx,len(lista),1):
             l2+=[lista[i]]
        return [l1, l2]

def croms_ini(tc, pop_ini):
        croms=[]
        limit = int(math.pow(2, tc))
        for _ in range(pop_ini):
                num=randint(0,limit)
                crom = int_to_bin_vec(num, tc)
                croms+=[crom]
        return croms

def cruzamento(n_filhos, tc, X, Y):
        filhos=[]
        for _ in xrange(0,n_filhos,2):
                # Garante que o corte garantira ao menos um bit trocado:
                p = randint(1,tc-2)
                X_=split_list(X,p)
                Y_=split_list(Y,p)
                F1=X_[0] + Y_[1]
                F2=Y_[0] + X_[1]
                filhos+= [F1] + [F2]
        return filhos

def calc_fitness(croms, train_perc):
        fitness=[]
        l = len(croms)
        for i in range(l):
                seed = bin_vec_to_int(croms[i])
                r2 = MLP(seed, train_perc)
                fitness+=[round(r2, 2)]
        return fitness

def calc_prob(fitness):
        prob=[]
        acum=0.0
        total=sum(fitness)
        for i in range(len(fitness)):
                acum+=float(fitness[i])/total
                prob+=[acum]
        return prob

def roleta(croms, prob, croms_passados):
        novos_croms=[]
        for _ in range(croms_passados):
                r = random()
                for i in range(len(prob)):
                        if r <= prob[i]:
                                novos_croms+=[croms[i]]
                                break 
        return novos_croms

def GA(objetivo_max, bits_busca, train_perc):
        # Parametros:
        # Tamanho do Cromossomo (Maximo valor da seed 2^tc):
        tc=bits_busca
        # Populacao Inicial:
        n_pop_ini=3
        # Numero de filhos resultantes do Cruzamento:
        n_filhos=2*n_pop_ini
        # Numero maximo de geracoes:
        max_geracoes=100
        geracao=0
        # Numero de cromossos passados por geracao:
        croms_passados=n_pop_ini*3/4
        
        # ==> POPULACAO INICIAL DE SEEDS:
        croms=croms_ini(tc,n_pop_ini)

        while True:
                print ('====> GERACAO ' + str(geracao))
                # ==> CRUZAMENTO:
                X = choice(croms)
                Y = choice(croms)
                filhos=cruzamento(n_filhos, tc, X, Y)
                croms+=filhos

                # ==> MUTACAO:
                # i: index garante que os novos filhos nao sofrerao mutacao
                i = randint(0,len(croms)-n_filhos-1)
                j = randint(0,tc-1)
                if croms[i][j]==str(0): croms[i][j]=str(1)
                else: croms[i][j]=str(0) 

                # ==> SELECAO:
                fitness=calc_fitness(croms, train_perc )
                print fitness
                fit_max=objetivo_max
                for i in range(len(croms)):
                        if fitness[i] >= fit_max:
                                return (True, croms[i], geracao)

                # Remove cromossomos com fitness<=0:
                i = len(croms)-1
                while i>0:
                        if fitness[i]<=0:
                                del fitness[i]
                                del croms[i]
                        i-=1

                # Distribuicao de probabilidade:
                prob = calc_prob(fitness)
                # Roleta:
                croms = roleta(croms, prob, croms_passados)
        
                # ==> CRITERIO DE PARADA:
                if geracao>=max_geracoes: return (False, [], geracao)

                geracao+=1


# ---------------------------------------------------------------------------------------------
# Parameters:
train_perc_a = 0.5
precisao_r2_max = 0.99
bits_seed_busca = 10

# Data:
x = [[0., 0.], [1., 1.], [2., 2.], [3., 3.], [4., 4.], [5., 5.], [6., 6.], [7., 7.]]
y = [0., 1., 2., 3., 4., 5., 6., 7.]

b=GA(precisao_r2_max, bits_seed_busca, train_perc_a)

if b[0]:
        print '===> SUCESSO'
        print str(b[2]) + ' geracoes'
        print '-> Cromossomo:'
        print b[1]
        print '-> Seed:'
        print bin_vec_to_int(b[1])
else:
        print '===> FALHA'
        print 'Max_geracoes atingida: ' + str(b[2])