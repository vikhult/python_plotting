# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 19:03:50 2019

@author: mrsup

Class contains experimental data and methods to simplify the 
visualisation of the same.
"""
import numpy as np

class experimental_data:
    def __init__(self):
        # declaration of class variables
        self.data = None
        self.data_description = None
    
    def add_data_from_file(self,new_data):
        self.__TODO()
        
    def __TODO():
        print("This method still lacks implementation.")

    def generate_random_data(self,nbr_data_vectors=int,len_data_vectors=int):
        """Generates random data to be processed
            
        Parameters
        ----------
        nbr_data_vectors : int
            the number of data vectors to be generated for the data matrix
        len_data_vectors : int
            the length of the data vectors to be generated for the data matrix
        
        Returns
        -------
        self.data : np.array()
            sets the data variable to the generated data matrix
        """
        dt = np.dtype('f8')
        data_mat_shape = (nbr_data_vectors,len_data_vectors)
        data_mat = np.zeros(shape=data_mat_shape, dtype=dt, order='C')
        
        for data_vec_i in range(0,nbr_data_vectors):
            data_mat[data_vec_i] = np.random.uniform(-1,1,len_data_vectors)
            
        self.__set_data(data_mat)
        
    def sort_data(self,sorting_variable='atan'):
        if sorting_variable == 'atan':
            self.__set_data(self.__atan_sort())
        else:
            pass
        
    def __atan_sort(self):
        old_data = self.data
        tan_vec = np.arctan2(old_data[0],old_data[1])
        for ent in tan_vec:
            if ent<0:
                ent = ent + 2*np.pi
        sorted_indx = np.argsort(tan_vec)
        sorted_data = np.empty_like(old_data)
        
        for sorted_indx, data_indx in zip(sorted_indx, range(0,np.size(old_data,1))):
            for kk in range(0,np.size(old_data,0)):
                sorted_data[kk,data_indx] = old_data[kk, sorted_indx]
        return sorted_data
            
    def __set_data(self,new_data):
        self.data = new_data
