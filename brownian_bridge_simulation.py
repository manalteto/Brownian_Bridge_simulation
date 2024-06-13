# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 09:52:01 2024

@author: tetom
"""

import numpy
from matplotlib import pyplot
from multiprocessing.dummy import Pool as ThreadPool

# Parameters
M = 10000  # Number of simulations
N = 100    # Number of time steps
nodes = [1, 3, 5, 8, 12, 9 , 6, 8]
times = [0, 3, 5, 6, 9, 12, 15, 20]


"""
brownian_bridge_simulation.py

This Python script simulates a Brownian bridge process. The script includes three main functions:
1. `bridge(M, N, t1, t2, a, b)`:
    - Interpolates between two known points and constructs one Brownian bridge.
2. `multibridge(M, N, nodes, times)`:
    - Constructs multiple Brownian bridges between the specified nodes and times.
3. `parallel_multibridge(M, N, nodes, times)`:
    - Utilizes parallel computing to construct multiple Brownian bridges efficiently.

Manal Teto
2024/06/12
"""


def bridge(M, N, t1, t2, a, b):
    
    dt = (t2-t1) / (N-1)
    
    B = numpy.empty((M, N), dtype=numpy.float32)
    
    
    B[:, 0] = a
    
    B[:, -1] = b
    
    
    for n in range(1, N - 1):
    
        bridge_mean = ((N - n) * dt  * B[:, n - 1] + dt * b ) / ((N - (n-1)) * dt)
        
        bridge_var = ((N - n) * dt ) / (N - (n - 1))
        
        B[:, n] = numpy.random.randn(M) * numpy.sqrt(bridge_var) + bridge_mean 
    
    return B


def multibridge(M, N, nodes, times):
    
    # Empty array for the final result
    B_full = numpy.empty((M, 0), dtype=numpy.float32)
    
    for i in range(len(nodes) - 1):
        t1 = times[i]
        t2 = times[i + 1]
        a = nodes[i]
        b = nodes[i + 1]
        
        # Generate the bridge for each segment
        B_segment = bridge(M, N, t1, t2, a, b)
        
        # remove the first column to avoid repeated times for segments after the first one 
        if i > 0:
            B_segment = B_segment[:, 1:]
        
        # Concatenate each segment to the full bridge
        B_full = numpy.concatenate((B_full, B_segment), axis=1)  
    
    return B_full





def bridge_adapter(args):
    return bridge(*args) # Unpacks the tuple into separate arguments for the bridge function



def parallel_multibridge(M, N, nodes, times):
    B_full = numpy.empty((M, 0), dtype=numpy.float32)
    
    parameters = [(M, N, times[i], times[i + 1], nodes[i], nodes[i + 1]) for i in range(len(nodes) - 1)]
    
    with ThreadPool() as pool:    # create a new thread pool that automatically gets cleaned up 
        results = pool.map(bridge_adapter, parameters)  # applies the function to all items in parallel using multiple threads
    
    for i, B_segment in enumerate(results):   # gets index as well as element 
        if i > 0:
            B_segment = B_segment[:, 1:]
        B_full = numpy.concatenate((B_full, B_segment), axis=1)
    
    return B_full


B_multi = multibridge(M, N, nodes, times)
pyplot.plot(B_multi.T)
pyplot.show()

B_parallel = parallel_multibridge(M, N, nodes, times)
pyplot.plot(B_parallel.T)
pyplot.show()
