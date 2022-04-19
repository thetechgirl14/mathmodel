# mathmodel

This module provides access to model functions for the analysis of Predator-Prey Model.

> **Lotka - Volterra Systems**

The Lotka - Voltera model is the simplest predator-prey model, describes the variation in populations of two species which interact via predation. This is a classical model to represent the dynamic of two populations used to predict changes in both with time.

Let α > 0, β > 0, δ > 0 and γ > 0 . The system is given by:

dx/dt= x (α − βy)

dy/dt= y (−δ + γx)

where x represents prey population and y represents predator population. It’s a system of first-order non-linear ordinary differential equations.

A typical solution to this system is given by x and y being periodic and out of phase. Prey grow exponentially, then predators feed on the overpopulated prey and grow exponentially until local prey are exhausted. The predators die off, then prey are able to return and the cycle repeats. 

>  **Logistic Systems**

There are limits imposed by the environment on the maximal possible size of a population: not
enough nutrients for a large bacterial culture, insufficient food for the human population of an island, or a small hunting territory for a given animal species. Ecologists talk about the carrying capacity of the environment, a number y with the property that no populations x > y are sustainable. If the population starts bigger than y, the number of individuals will decrease.

dx/dt= αx( 1 - x/K) - βy
dy/dt= y (−δ + γx)

