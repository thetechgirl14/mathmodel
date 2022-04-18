''' Written on 4/15/2022 by Abhilasha, Sakshi & Pankti
Module contains functions for Lotka-Volterra Systems aka Predator - Prey Model'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy

pred_label = 'Predator Count (Thousands)'
prey_label = 'Prey Count (Thousands)'
time_label = 'Time'

pred_color = 'blue'
prey_color = 'green'


class Lotka_Volterra(object):
    '''To set up a simple Lotka_Volterra system'''
    
    def __init__(self, predgrow, preddie, preygrow, preydie, tmax, timestep, prey_capacity=100.0, predator_capacity = 100.0):
        '''Create Lotka-Volterra system'''
        
        self.n = int(tmax/timestep)
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
        
    def set_initial_conditions(self, pred_zero, prey_zero, t_zero=0.0):
        '''Setting up initial conditions'''
        self.prey[0] = prey_zero
        self.predator[0] = pred_zero
        self.time[0] = t_zero
        
    def system(self):
        '''Integration vanilla Lotka-Volterra system'''
        
        for i in range(self.n-1):
                        
            self.time[i+1] = self.time[i] + self.dt
            self.predator[i+1] = self.predator[i] + self.dt*self.predator[i]*(self.predgrow*self.prey[i] - self.preddie)
            self.prey[i+1] = self.prey[i] + self.dt*self.prey[i]*(self.preygrow - self.predator[i]*self.preydie)

    
    def system_logistic(self):
        '''Integration of Lotka-Volterra system assuming logistic growth'''
        
        for i in range(self.n-1):
            self.time[i+1] = self.time[i]+self.dt
            self.predator[i+1] = self.predator[i] + self.dt*self.predator[i]*(self.predgrow*self.prey[i]*(1.0 - self.predator[i]/self.predator_capacity) - self.preddie)
            self.prey[i+1] = self.prey[i] + self.dt*self.prey[i]*self.preygrow*(1.0-self.prey[i]/self.prey_capacity) - self.prey[i]*self.predator[i]*self.preydie
            #print self.time[i], self.predator[i],self.prey[i]
    
    def system_stochastic(self):
        '''Integration of vanilla Lotka-Volterra system with stochastic predator death rate'''
        
        for i in range(self.n-1):
                        
            self.time[i+1] = self.time[i] + self.dt
            self.predator[i+1] = self.predator[i] + self.dt*self.predator[i]*(self.predgrow*self.prey[i] - self.preddie*(1-0.1)*np.random.rand())
            self.prey[i+1] = self.prey[i] + self.dt*self.prey[i]*(self.preygrow*(1-0.1)*np.random.rand() - self.predator[i]*self.preydie)

            
    def plot_vs_time(self, filename='populations_vs_time.png', plot_capacity=False):
        
        '''Plotting both populations vs time'''
        fig1 = plt.figure()
        ax1 = fig1.add_subplot(111)
        ax2 = ax1.twinx()
        ax1.set_xlabel('Time', fontsize=16)
        ax1.set_ylabel(predlabel,fontsize=16, color=predcolor)
        ax1.tick_params('y', colors=predcolor)
        ax2.set_ylabel(preylabel,fontsize=16, color=preycolor)
        ax2.tick_params('y', colors='blue', color=preycolor)
        ax1.plot(self.time, self.predator, label='Predator', color=predcolor, linestyle='dashed')
        ax2.plot(self.time, self.prey, label = 'Prey', color = preycolor)
        if(plot_capacity):
            ax2.axhline(self.prey_capacity, label= 'Prey carrying capacity', color=preycolor, linestyle='dotted')
        #ax2.axhline(self.predator_capacity, label= 'Predator carrying capacity', color=predcolor, linestyle='dashed')
        plt.show()
        fig1.savefig(filename, dpi=300)
        
    def plot_predator_vs_prey(self, filename = 'predator_vs_prey.png'):
        
        '''Plotting predator vs prey'''
        fig1 = plt.figure()
        ax1 = fig1.add_subplot(111)
        
        ax1.set_xlabel(predlabel,fontsize=16)
        ax1.set_ylabel(preylabel,fontsize=16)
        ax1.plot(self.predator,self.prey, color='black')
        plt.show()
        fig1.savefig(filename,dpi=300)
        
    def plot_both_figures(self):
        
        '''To plot both the graphs: populations vs time & predators vs prey'''
        fig1 = plt.figure()
        
        ax1 = fig1.add_subplot(211)
        ax2 = ax1.twinx()
        ax1.set_xlabel(timelabel)
        ax1.set_ylabel(predlabel, color=predcolor)
        ax2.set_ylabel(preylabel, color =preycolor)
        ax1.plot(self.time, self.predator, label='Predator', color=predcolor)
        ax2.plot(self.time, self.prey, label = 'Prey', color = preycolor)
        ax1.legend()
        
        ax3 = fig1.add_subplot(212)
        
        ax3.set_xlabel(predlabel)
        ax3.set_ylabel(preylabel)
        ax3.plot(self.predator,self.prey, color = 'black')

        
        plt.show()
