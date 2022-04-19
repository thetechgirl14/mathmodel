""" Written on 4/15/2022 by Abhilasha, Sakshi & Pankti
Module contains functions for Lotka-Volterra Systems aka Predator - Prey Model"""

import matplotlib.pyplot as plt
import numpy as np

pred_label = 'Predator Count (Thousands)'
prey_label = 'Prey Count (Thousands)'
time_label = 'Time'

pred_color = 'blue'
prey_color = 'green'


class Lotka_Volterra(object):
    """To set up a simple Lotka_Volterra system"""

    def __init__(self, predgrow, preddie, preygrow, preydie, tmax, timestep, prey_capacity=100.0,
                 predator_capacity=100.0):
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
        self.equilibria = []
        self.d_predator = np.zeros(self.n)
        self.d_prey = np.zeros(self.n)

    def set_initial_conditions(self, pred_zero, prey_zero, t_zero=0.0):
        """Setting up initial conditions"""
        self.prey[0] = prey_zero
        self.predator[0] = pred_zero
        self.time[0] = t_zero

    def system(self):
        """Integration vanilla Lotka-Volterra system"""

        for i in range(self.n - 1):
            self.d_predator[i] = self.predator[i] * (self.predgrow * self.prey[i] - self.preddie)
            self.d_prey[i] = self.prey[i] * (self.preygrow - self.predator[i] * self.preydie)
            self.time[i + 1] = self.time[i] + self.dt
            self.predator[i + 1] = self.predator[i] + self.dt * self.d_predator[i]
            self.prey[i + 1] = self.prey[i] + self.dt * self.d_prey[i]

        return self.time, self.predator, self.prey

    def sys(self):
        """Differential vanilla Lotka-Volterra System"""

        for i in range(self.n - 1):
            self.d_predator[i] = self.predator[i] * (self.predgrow * self.prey[i] - self.preddie)
            self.d_prey[i] = self.prey[i] * (self.preygrow - self.predator[i] * self.preydie)
            self.time[i] = self.time[i] + self.dt

        return self.d_predator, self.d_prey

    def system_logistic(self):
        """Integration of Lotka-Volterra system assuming logistic growth"""

        for i in range(self.n - 1):
            self.d_predator[i] = self.predator[i] * (self.predgrow * (1.0 - self.predator[i] / self.predator_capacity) - self.preddie* self.prey[i])
            self.d_prey[i] = self.prey[i] * (self.preygrow - self.predator[i] * self.preydie)
            self.time[i + 1] = self.time[i] + self.dt
            self.predator[i + 1] = self.predator[i] + self.dt * self.d_predator[i]
            self.prey[i + 1] = self.prey[i] + self.dt * self.d_prey[i]

    def plot_populations_vs_time(self, filename='populations_vs_time.png', plot_capacity=False):
        """Plotting both populations vs time"""

        fig = plt.figure(figsize=(15, 5))
        fig.subplots_adjust(wspace=0.5, hspace=0.3)
        ax = fig.add_subplot(1, 2, 1)

        ax.plot(self.predator, 'r-', label='Predator')
        ax.plot(self.prey, 'b-', label='Prey')
        ax.set_title("Dynamics in time")
        ax.set_xlabel("Time")
        ax.grid()
        ax.legend(loc='best')
        plt.show()

    def plot_predator_vs_prey(self, filename='predator_vs_prey.png'):
        """Plotting predator vs prey"""

        fig = plt.figure(figsize=(15, 5))
        fig.subplots_adjust(wspace=0.5, hspace=0.3)
        ax = fig.add_subplot(1, 2, 1)

        ax.plot(self.predator, self.prey, color="blue")
        ax.set_xlabel("Predator")
        ax.set_ylabel("Prey")
        ax.set_title("Phase space")
        ax.grid()
        plt.show()

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
