# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 14:09:12 2021

@author: Admin
"""

class Fish:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Salmon', 'Arapaima', 'Magikarp']
        
    def printMembers(self):
        print('Printing members of the Fish class')
        for member in self.members:
            print('\t%s ' % member)