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

# Brownian Bridge construction 

