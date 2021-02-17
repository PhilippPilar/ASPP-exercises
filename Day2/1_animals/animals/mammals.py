# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 13:49:52 2021

@author: Admin
"""

class Mammals:
    def __init__(self):
        ''' Constructor for this clas. '''
        # Create some member animals
        self.members = ['Tiger', 'Elephant', 'Wild Cat']
        
    def printMembers(self):
        print('Printing members of the Mammals class')
        for member in self.members:
            print('\t%s ' % member)
    