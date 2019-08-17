# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 19:03:49 2019

@author: mrsup

Simply testing the modules.
"""
import exp_data
import matplotlib.pyplot as plt

if __name__ == '__main__':
    my_data = exp_data.experimental_data()
    my_data.generate_random_data(2,120)
    my_data.sort_data()
    
    
    plot_data = my_data.data
    plt.plot(plot_data[0],plot_data[1])