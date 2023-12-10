import numpy as np
import math as mt
import random

def nbits(a, b, dx):
    r=b-a
    B=mt.ceil(mt.log2(r/dx+1))
    dx_new =r/(2**B-1)
    return B, dx_new

def gen_population(P, N, B):
    pop=np.random.randint(2, size=(P,N*B))
    return pop

def decode_individual(individual, N, B, a, dx):
    individual=np.array(individual)
    individual=individual.reshape(N,B) 
    for j in range(0,N):
        for i in range(0,B):
            individual[j,B-i-1]=individual[j,B-i-1]*2**i
    r=np.sum(individual, axis=1)
    decode_individual=a+dx*r
    return decode_individual

def evaluate_population(func, pop, N, B, a, dx):
    evaluated_pop=[]
    for i, ind in enumerate(pop):
        evaluated_pop.append(func(decode_individual(ind,N,B,a,dx)))
    return np.array(evaluated_pop)

def get_best(pop, evaluated_pop):
    best_value=max(evaluated_pop)
    for i in range(0,len(evaluated_pop)):
        if evaluated_pop[i]==best_value:
            best_individual=pop[i]
    return best_individual, best_value

def roulette(pop, evaluated_pop):
    ### TWÓJ KOD TUTAJ
    new_pop = random.choices(pop, weights = evaluated_pop*(1/sum(evaluated_pop)), k = len(pop))
    new_pop = np.asarray(new_pop)
    return new_pop

def cross(pop, pk):
    #l=[]
    new_pop=np.empty_like(pop)
    podzial=random.randint(1,len(pop[0])-1)
    for i in range(len(pop)):
        r=random.random()
        #l.append(r)
        if pk > r:
            new_pop[i]=np.append(pop[i][:podzial],pop[(i+1)%len(pop)][podzial:])
            #d2=np.append(pop[i+1][:podzial],pop[i][podzial:])
            # random.choice([d1,d2])
        else:
            new_pop[i]=pop[i]  
    ### TWÓJ KOD TUTAJ
    return new_pop

def mutate(pop, pm):
    new_pop=pop
    for i in range(len(pop)): #wiersze
        for j in range(len(pop[0])): #kol
            r=random.random()
            if pm > r:
                if new_pop[i][j]==1:
                    new_pop[i][j]=0
                else:
                    new_pop[i][j]=1
            else:
                None
    return new_pop