#!/usr/bin/python

# Program to multiply two matrices using nested loops
import random
#from memory_profiler import profile
#import line_profiler
#import line_profiler
#profile = line_profiler.LineProfiler()
#atexit.register(profile.print_stats)


N = 250


# NxN matrix
@profile
def NxN_matrix():
    X = []
    for i in range(N):
        X.append([random.randint(0,100) for r in range(N)])
    return X

X = NxN_matrix()

# Nx(N+1) matrix
@profile
def NxNp1_matrix():
    Y = []
    for i in range(N):
        Y.append([random.randint(0,100) for r in range(N+1)])
    return Y

Y = NxNp1_matrix()

# result is Nx(N+1):
@profile
def get_result():
    result = []
    for i in range(N):
        result.append([0] * (N+1))
    return result

result = get_result()

# iterate through rows of X
@profile
def matmult(X,Y,result):
    for i in range(len(X)):
        # iterate through columns of Y
        for j in range(len(Y[0])):
            # iterate through rows of Y
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]
    return result
                
result = matmult(X,Y,result)

# for r in result:
#     print(r)
