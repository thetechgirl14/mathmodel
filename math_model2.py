""" Written on 4/15/2022 by Abhilasha, Sakshi & Pankti
Module contains functions for Lotka-Volterra Systems aka Predator - Prey Model"""

import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

pred_label = 'Predator Count (Thousands)'
prey_label = 'Prey Count (Thousands)'
time_label = 'Time'

pred_color = 'blue'
prey_color = 'green'


class LotkaVolterra(object):
    """To set up a simple Lotka_Volterra system"""

    def __init__(self, predgrow, preddie, preygrow, preydie, tmax, timestep, prey_capacity=100,
                 predator_capacity=100):
        """Create Lotka-Volterra system"""

        self.n = int(tmax / timestep)
        self.dt = timestep
        self.time = np.zeros(self.n)
        self.prey = np.zeros(self.n)
        self.predator = np.zeros(self.n)
        self.preygrow = preygrow
        self.preydie = preydie
        self.predgrow = predgrow
        self.preddie = preddie
        self.prey_capacity = prey_capacity
        self.predator_capacity = predator_capacity
        self.d_predator = np.zeros(self.n)
        self.d_prey = np.zeros(self.n)

    def set_initial_conditions(self, pred_zero, prey_zero, t_zero=0.0):
        """Setting up initial conditions"""
        self.prey[0] = prey_zero
        self.predator[0] = pred_zero
        self.time[0] = t_zero

    def sys(self):
        """Differential vanilla Lotka-Volterra System"""

        for i in range(self.n - 1):
            self.d_predator[i] = self.predator[i] * (self.predgrow * self.prey[i] - self.preddie)
            self.d_prey[i] = self.prey[i] * (self.preygrow - self.predator[i] * self.preydie)
            self.time[i] = self.time[i] + self.dt

        return self.d_predator, self.d_prey

    def system(self):
        """Integration vanilla Lotka-Volterra system"""

        for i in range(self.n - 1):
            self.d_predator[i] = self.predator[i] * (self.predgrow * self.prey[i] - self.preddie)
            self.d_prey[i] = self.prey[i] * (self.preygrow - self.predator[i] * self.preydie)
            self.time[i + 1] = self.time[i] + self.dt
            self.predator[i + 1] = self.predator[i] + self.dt * self.d_predator[i]
            self.prey[i + 1] = self.prey[i] + self.dt * self.d_prey[i]

        return self.time, self.predator, self.prey, self.d_predator, self.d_prey

    def system_logistic(self):
        """Integration of Lotka-Volterra system assuming logistic growth"""

        for i in range(self.n - 1):
            self.time[i + 1] = self.time[i] + self.dt
            self.predator[i + 1] = self.predator[i] + self.dt * self.predator[i] * (
                    self.predgrow * self.prey[i] * (1.0 - self.predator[i] / self.predator_capacity) - self.preddie)
            self.prey[i + 1] = self.prey[i] + self.dt * self.prey[i] * self.preygrow * (
                    1.0 - self.prey[i] / self.prey_capacity) - self.prey[i] * self.predator[i] * self.preydie

    def system_stochastic(self):
        """Integration of vanilla Lotka-Volterra system with stochastic predator death rate"""

        for i in range(self.n - 1):
            self.time[i + 1] = self.time[i] + self.dt
            self.predator[i + 1] = self.predator[i] + self.dt * self.predator[i] * (
                    self.predgrow * self.prey[i] - self.preddie * (1 - 0.1) * np.random.rand())
            self.prey[i + 1] = self.prey[i] + self.dt * self.prey[i] * (
                    self.preygrow * (1 - 0.1) * np.random.rand() - self.predator[i] * self.preydie)

    def plot_vs_time(self, filename='populations_vs_time.png', plot_capacity=False):

        """Plotting both populations vs time"""
        fig1 = plt.figure()
        ax1 = fig1.add_subplot(111)
        ax2 = ax1.twinx()
        ax1.set_xlabel('Time', fontsize=16)
        ax1.set_ylabel(pred_label, fontsize=16, color=pred_color)
        ax1.tick_params('y', colors=pred_color)
        ax2.set_ylabel(prey_label, fontsize=16, color=prey_color)
        ax2.tick_params('y', colors='blue', color=prey_color)
        ax1.plot(self.time, self.predator, label='Predator', color=predcolor, linestyle='dashed')
        ax2.plot(self.time, self.prey, label='Prey', color=preycolor)
        if plot_capacity:
            ax2.axhline(self.prey_capacity, label='Prey carrying capacity', color=prey_color, linestyle='dotted')
        # ax2.axhline(self.predator_capacity, label= 'Predator carrying capacity', color=predcolor, linestyle='dashed')
        plt.show()
        fig1.savefig(filename, dpi=300)

    def plot_predator_vs_prey(self, filename='predator_vs_prey.png'):

        """Plotting predator vs prey"""
        fig1 = plt.figure()
        ax1 = fig1.add_subplot(111)

        ax1.set_xlabel(pred_label, fontsize=16)
        ax1.set_ylabel(prey_label, fontsize=16)
        ax1.plot(self.predator, self.prey, color='black')
        plt.show()
        fig1.savefig(filename, dpi=300)

    def plot_both_figures(self):
        """To plot both the graphs: populations vs time & predators vs prey"""

        fig = plt.figure(figsize=(15, 5))
        fig.subplots_adjust(wspace=0.5, hspace=0.3)
        ax1 = fig.add_subplot(1, 2, 1)
        ax2 = fig.add_subplot(1, 2, 2)

        ax1.plot(self.predator, 'r-', label='Predator')
        ax1.plot(self.prey, 'b-', label='Prey')
        ax1.set_title("Dynamics in time")
        ax1.set_xlabel("Time")
        ax1.grid()
        ax1.legend(loc='best')

        ax2.plot(self.predator, self.prey, color="blue")
        ax2.set_xlabel("Predator")
        ax2.set_ylabel("Prey")
        ax2.set_title("Phase space")
        ax2.grid()
        plt.show()

    # x, y, a, b, c, d
    def get_critical(self):
        x, y, a, b, c, d = sp.symbols('x', 'y', 'a', 'b', 'c', 'd')


if __name__ == "__main__":
    predgrow = 0.5  # growth rate of the predator -> delta
    preddie = 0.25  # predator death rate -> gamma
    preygrow = 1  # prey growth rate -> alpha
    preydie = 0.5  # prey death rate -> beta
    tmax = 5  # max time limit
    timestep = 0.1  # delta time

    pred_zero, prey_zero = 10, 10

    lv = LotkaVolterra(predgrow, preddie, preygrow, preydie, tmax, timestep)
    lv.set_initial_conditions(pred_zero, prey_zero)
    t, x, y, dx, dy = lv.system()
    print(len(x), len(y), len(dx), len(dy))

    # if dx[i] = 0, and dy[j] = 0, then return x[i], y[j] and x[j], y[i]
    # y = alpha/beta, x= gamma/delta
