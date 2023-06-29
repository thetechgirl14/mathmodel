# Math Model Python Package

This package provides model functions for the analysis of predator-prey interactions and other ecological systems. It includes implementations of the Lotka-Volterra model, logistic systems, and chemostat models.

## Lotka-Volterra Systems
The Lotka-Volterra model describes the population dynamics of two species that interact via predation. The system of equations is given by:

```
dx/dt = x(α - βy)

dy/dt = y(-δ + γx)
```
where x represents the prey population and y represents the predator population. The parameters α, β, δ, and γ are positive constants. The solution to this system exhibits periodic behavior, with prey and predator populations oscillating in a cycle.

## Logistic Systems
Logistic systems take into account the carrying capacity of the environment, which limits the maximal population size. The equations for the logistic model are:
``` 
dx/dt = αx(1 - x/K) - βy

dy/dt = y(-δ + γx)
```
where x is the population of the first species, y is the population of the second species, and K is the carrying capacity. The logistic model captures the decrease in population when it exceeds the carrying capacity.

## Chemostat
The chemostat model is used to analyze the interaction between two microbial species in a shared medium. The dynamics of the system depend on the flow rate, nutrient concentrations, and growth rates of the species. The equations governing the chemostat model are:
```
N(t + ∆t) - N(t) = r(C(t)) * N(t) * ∆t

C(t + ∆t) - C(t) = -α * [N(t + ∆t) - N(t)]
```
where N(t) represents the bacterial concentration and C(t) represents the nutrient concentration at time t.

## Dependencies
This package requires the following external libraries:

NumPy (http://www.numpy.org)
matplotlib (http://matplotlib.org/)
os (https://docs.python.org/3/library/os.path.html)
sys (https://docs.python.org/3/library/sys.html)

Make sure you have the necessary dependencies installed
```
pip install -r requirements.txt
```

## Usage

The main code for the Lotka-Volterra model is located in [math_model.py](https://github.com/thetechgirl14/mathmodel/blob/main/math_model.py) within the Lotka_Volterra class. The code that integrates the equations with exponential growth is tested in [test_lotka_volterra.py](https://github.com/thetechgirl14/mathmodel/blob/main/test_lotka_volterra.py).

The chemostat model's core source code is written in [Chemostat.py](https://github.com/thetechgirl14/mathmodel/blob/main/Chemostat.py) within the Chemostat class, and it can be accessed through the [chemostat_test.py](https://github.com/thetechgirl14/mathmodel/blob/main/Chemostat_test.py) test file.

Adjust the parameter values in the test files to customize the experiments and plot the resulting graphs.
