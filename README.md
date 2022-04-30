# mathmodel

This module provides access to model functions for the analysis of Predator-Prey Model.

> **Lotka - Volterra Systems**

In any given environment, every species has a niche which comprises of Abiotic elements, Food source and Habit. When two different species have same niche, they are competitors. It leads to either win/loss, in which case one species wins and other one gets extinct from that particular environment. Or it could lead to partitioning, where one of the species changes something in their niche to co-exist in the environment. When a species survives on another species, The Lotka Volterra model is used to predict the variation in the population with time because of the predatory interaction. 
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

>  **Chemostat**

The chemostat model is used to determine the type of interaction between two species. If the interaction leads to the model where two microbial species that are in same medium, and they both decline with time, the interaction is a predator-prey type. If one species thrives at the cost of other, it is a competition. The type when, with interaction both the species thrive, is called mutualism. 

With
V = constant volume of solution in culture chamber 
F = (constant and equal) flows in vol/sec, e.g. m3/s 
N(t) = bacterial concentration in mass/vol, e.g. g/m3 
C0, C(t) = nutrient concentrations in mass/vol (C0 assumed constant)
Chamber is well-mixed:
Assuming that growth is proportional to initial population, time intervals and food quantity, the equation is:
N(t + ∆t) − N(t) due to growth = r(C(t)) N(t) ∆t

The function r(C) is a reasonable choice. Here we have used Vmax/Km 
When consumption of food is inversely proportional to the population growth the equation is:
C(t + ∆t) − C(t) due to consumption = −α [N(t + ∆t) − N(t)]


This Package requires following external libraries: 

•	NumPy (see http://www.numpy.org)

•	matplotlib (see http://matplotlib.org/)
