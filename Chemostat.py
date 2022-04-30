#!/usr/bin/python
import sys
import matplotlib.pyplot as plt



class Chemostat(object):
    def __init__(self, strain1_vmax, strain1_km, strain1_yield, strain1_starting, strain2_vmax,
              strain2_km, strain2_yield, strain2_starting):
        # strain 1
        self.strain1_vmax = strain1_vmax
        self.strain1_km = strain1_km
        self.strain1_yield = strain1_yield
        self.strain1_starting = strain1_starting

        # strain 2
        self.strain2_vmax = strain2_vmax
        self.strain2_km = strain2_km
        self.strain2_yield = strain2_yield
        self.strain2_starting = strain2_starting

        self.plot_minutes = []
        self.plot_prop = []

    def set_start_conditions(self, flow_rate, volume, endtime, substrate_media, substrate_init):
        """
        :param flow_rate:
        :param volume:
        :param endtime:
        :param substrate_media:
        :param substrate_init:
        :return:
        """
        self.flow_rate = flow_rate
        self.volume = volume
        self.endtime = endtime
        self.substrate_media = substrate_media
        self.substrate_init = substrate_init
        self.dilution = flow_rate/volume

    def set_parameter(self):
        """
        Set initial parameters
        :return:
        """
        self.parameters = list()
        self.parameters = map(float, self.parameters)
        return self.parameters



###creating file for output

    """def write_output(self):
        
        writes the results to output file
        :return: output file
        
        prop_out = open("simulation_results.tsv","w")
        prop_out.write("Time\tNutr\tStrain1\tStrain2\tProp")"""

#substrate = self.substrate_init
#strain1 = self.strain1_starting
#strain2 = self.strain2_starting
    def simulation(self):
        """
        Looping through the simulation
        :return:
        """
        for minutes in range(0, self.endtime):
            if minutes < 10000:
                #calculating the change in nutrients
                nutr_flux = self.dilution*(self.substrate_media-self.substrate_init) - (self.strain1_starting/self.strain1_yield)*\
                            ((self.strain1_vmax*self.substrate_init)/(self.strain1_km+self.substrate_init))
                strain1_flux = ((self.strain1_vmax*self.substrate_init)/(self.strain1_km+self.substrate_init)-self.dilution)*self.strain1_yield

                #recalculating substrate and strain1 count
                substrate = self.substrate_init+nutr_flux
                strain1 = self.strain1_yield+strain1_flux

                if str(int(minutes)/int(250)).isdigit() == True:

                    self.plot_minutes.append(minutes)
                    #print(plot_minutes)
                    self.plot_prop.append(0)

                    print(str(minutes) + "\t" + str(substrate) + "\t" + str(strain1) + "\t" + "0" + "\t0\n")
            if minutes >= 10000:
                #calculating the change in nutrients after 2 strains
                nutr_flux = self.dilution*(self.substrate_media-self.substrate_init) - \
                            (self.strain1_starting/self.strain1_yield)*\
                            ((self.strain1_vmax*self.substrate_init)/(self.strain1_km+self.substrate_init)) - \
                            (self.strain2_starting/self.strain2_yield)*\
                            ((self.strain2_vmax*self.substrate_init)/(self.strain2_km+self.substrate_init))
                strain1_flux = ((self.strain1_vmax*self.substrate_init)/(self.strain1_km+self.substrate_init)-self.dilution)*self.strain1_starting
                strain2_flux = ((self.strain2_vmax*self.substrate_init)/(self.strain2_km+self.substrate_init)-self.dilution)*self.strain2_starting

            #recalculating substrate and strain1 count
                substrate = self.substrate_init+nutr_flux
                strain1 = self.strain1_starting+strain1_flux
                strain2 = self.strain2_starting+strain2_flux
                if str(minutes/250).isdigit() == True:
                    proportion = strain2/(strain1+strain2)
                    print((str(minutes) + "\t" + str(substrate) + "\t" + str(strain1) + "\t" + str(strain2) + "\t" + str(proportion) + "\n"))
                    self.plot_minutes.append(minutes)
                    self.plot_prop.append(proportion)
            print(self.plot_minutes, self.plot_prop)
            #self.write_output.close()
            #plt.plot(plot_minutes, plot_prop, color='black')
            #plt.show()

    def plot_min_vs_proportion(self, filename = 'minutes_vs_proportion.png', plot_capacity=False):
        """
        Plot minutes vs proportion
        """
        '''Plot minutes vs proportion'''
        fig1 = plt.figure()
        ax1 = fig1.add_subplot(111)
        ax1.set_xlabel("Minutes", fontsize=22)
        ax1.set_ylabel("Proportion", fontsize=22)
        ax1.plot(self.plot_minutes,self.plot_prop, color='black')
        plt.show()
        fig1.savefig(filename,dpi=300)
