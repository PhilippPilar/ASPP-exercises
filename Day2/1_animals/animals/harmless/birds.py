# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 13:51:50 2021

@author: Admin
"""

class Birds:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Sparrow', 'Robin', 'Duck']
        
    def printMembers(self):
        print('Printing members of the Birds class')
        for member in self.members:
            print('\t%s ' % member)