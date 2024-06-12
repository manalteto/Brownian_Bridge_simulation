# Brownian_Bridge_simulation

## Description

This repository contains a Python script for simulating a Brownian bridge process. The Brownian bridge is a key concept in stochastic processes and has applications in financial modeling and statistical analysis. The repository includes code for generating and visualizing sample paths of the Brownian bridge.

## Functions

1. **bridge(M, N, t1, t2, a, b)**:
    - Interpolates between two known points and constructs one Brownian bridge.

2. **multibridge(M, N, nodes, times)**:
    - Constructs multiple Brownian bridges between the specified nodes and times.

3. **parallel_multibridge(M, N, nodes, times)**:
    - Utilizes parallel computing to construct multiple Brownian bridges efficiently.

## Installation

To use this script, ensure you have Python and the necessary libraries installed. You can install the required libraries using pip:

```bash
pip install numpy matplotlib
```

# Brownian Bridge construction 
In simple terms, a Brownian Bridge is a method for interpolating or filling in the path of a Brownian motion between two fixed points in time, where the start and end points of the motion are known. In the Brownian Motion framework, we focus on simulating values $(W_{t_{1}}, \ldots, W_{t_{n}})$ at a fixed set of points $t_1, ..., t_n$ using independent standard normal random variables $(Z_1, \ldots, Z_n)$. Consider we set $t_0 = 0$ and $W(0)=0$ then the subsequent values can be generated as :
    $W(t_{i+1}) = W(t_i) + \sqrt{t_{i+1} - t_i}Z_{i+1}, \quad i = 0, \ldots, n-1$.
Equation (\ref{BM}) creates the vector $(W_{t_{1}}, \ldots, W_{t_{n}})$ from left to right. Instead of traditionally computing the values of Brownian motion at consecutive times in a sequential manner, we can opt for a more flexible approach by generating the values of Brownian motion $W_{t_{i}}$ at predetermined times in any sequence we prefer, as long as we adhere to the correct conditional probability distributions based on the values that have already been calculated. For instance, we could start by determining the value at the final time point $W_{t_{n}}$, compute the value at the midpoint time $W_{t_{n/2}}$ based on $W_{t_{n}}$ and then continue to fill in the rest of the intermediate values. 

