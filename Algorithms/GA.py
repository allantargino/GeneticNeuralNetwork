from random import shuffle, randrange, randint, choice, random
import Queue as Q
import math

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
        for _ in range(pop_ini):
                crom=[]
                for _ in range(tc):
                      crom+=[randint(0,1)]
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

def calc_fitness(croms, ini, obj, w, h):
        fitness=[]
        obj_ = posidx(obj,w)
        for i in range(len(croms)):
                croms[i]
                f = posfinal(croms[i], nwabs, ini,obj,w,h)
                f_ = posidx(f,w)
                x = f_[0]-obj_[0]
                y = f_[1]-obj_[1]
                fitness+=[(w-1)*(h-1)-(abs(x)+abs(y))]
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

def GA(ini, obj,w,h):
        # Parametros:
        # Tamanho do Cromossomo (Pior caso (h*w>2)):
        tc=(w*h-1)*2
        # Populacao Inicial:
        n_pop_ini=50
        # Numero de filhos resultantes do Cruzamento:
        n_filhos=2*3
        # Numero maximo de geracoes:
        max_geracoes=100
        geracao=0
        # Numero de cromossos passados por geracao:
        croms_passados=n_pop_ini*3/4
        
        # ==> POPULACAOO INICIAL:
        croms=croms_ini(tc,n_pop_ini)

        while True:
                # ==> CRUZAMENTO:
                X = choice(croms)
                Y=choice(croms)
                filhos=cruzamento(n_filhos, tc, X, Y)
                croms+=filhos

                # ==> MUTACAO:
                # i: index garante que os novos filhos nao sofrerao mutacao
                i = randint(0,len(croms)-n_filhos-1)
                j = randint(0,tc-1)
                if croms[i][j]==0: croms[i][j]=1
                else: croms[i][j]=0 

                # ==> SELECAOO:
                fitness=calc_fitness(croms,ini,obj,w,h)
                fit_max=(w-1)*(h-1)
                if fit_max in fitness:
                        i=fitness.index(fit_max)
                        return (True, croms[i], geracao)

                # Remove cromossomos com fitness=0:
                while 0 in fitness:
                        idx=fitness.index(0)
                        del fitness[idx]
                        del croms[idx]

                # Distribuicao de probabilidade:
                prob = calc_prob(fitness)
                # Roleta:
                croms = roleta(croms, prob, croms_passados)
        
                # ==> CRITERIO DE PARADA:
                if geracao>=max_geracoes: return (False, [], geracao)

                geracao+=1

w0=4
h0=5

b=GA(inicio,objetivo,w0,h0)

if b[0]:
        print '===> SUCESSO'
        print str(b[2]) + ' geracoes'
        print '-> Cromossomo:'
        print b[1]

else:
        print '===> FALHA'
        print 'Max_geracoes atingida: ' + str(b[2])