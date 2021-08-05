# EcolSimulation

####WORK IN PROGRESS

This project considers the simulation of population dynamics in a spatially explicit manner.

The simulation space consists of a grid, where each cell is initialised with a continuous number sampled uniformly in the range of 0-1. 
These numbers represent the fitness of the organism on a particular cell, where 1 represents optimal reproductive success and 0 none at all.
A number of cells are randomly initialised with an organism.

A fixed number of iterations is simulated. 
In each iteration, first, the reproductive potential of all organisms are calculated individually. 
In a second step, the dispersal of offspring around the parent is modelled.
For this process, a key parameter is the _dispersal decay_, i.e. the exponent with which the density of (direct) offspring decreases with distance from its parent.

![dyn_gif](media/dyn.gif "Simulation over 40 iterations")

Aim of this project is to 
- identify general differences in spatial vs non-spatial simulations
- investigate the effect of spatial structure on population dynamics and evolutionary strategy
