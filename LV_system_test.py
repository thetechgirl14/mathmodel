from math_model import Lotka_Volterra

predgrow = 0.5  # growth rate of the predator -> delta
preddie = 0.25  # predator death rate -> gamma
preygrow = 1  # prey growth rate -> alpha
preydie = 0.5  # prey death rate -> beta
tmax = 5  # max time limit
timestep = 0.1  # delta time

pred_zero, prey_zero = 10, 10

lv = Lotka_Volterra(predgrow, preddie, preygrow, preydie, tmax, timestep)
lv.set_initial_conditions(pred_zero, prey_zero)
t, x, y = lv.system()
lv.plot_both_figures()