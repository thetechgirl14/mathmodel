from Chemostat import Chemostat
strain1_vmax = 0.0030
strain1_km = 481.26
strain1_yield = 0.396345
strain1_starting = 0.14
strain2_vmax = 0.0024
strain2_km = 751.19
strain2_yield = 0.3963745
strain2_starting = 0.001
flow_rate = 0.00000347
volume = 0.010
endtime = 100000
substrate_media = 2200
substrate_init = 1100

chemo = Chemostat(strain1_vmax, strain1_km, strain1_yield, strain1_starting, strain2_vmax, strain2_km, strain2_yield, strain2_starting)
chemo.set_start_conditions(flow_rate, volume, endtime, substrate_media, substrate_init)
chemo.simulation()
chemo.plot_min_vs_proportion()

