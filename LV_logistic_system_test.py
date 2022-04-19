from math_model import Lotka_Volterra

predgrow = 0.5  # growth rate of the predator -> delta
preddie = 0.25  # predator death rate -> gamma
predator_capacity = 100 #predator carrying capacity -> K
    
preygrow = 1  # prey growth rate -> alpha
preydie = 0.5  # prey death rate -> beta
    
tmax = 5  # max time limit
timestep = 0.1  # delta time

pred_zero, prey_zero = 10, 10

lv = Lotka_Volterra(predgrow, preddie, preygrow, preydie, tmax, timestep, predator_capacity)
lv.set_initial_conditions(pred_zero, prey_zero)
lv.system_logistic()
lv.plot_both_figures()