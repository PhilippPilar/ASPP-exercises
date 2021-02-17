# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 13:54:06 2021

@author: Admin
"""


#old version of package
# import animals

# m = animals.Mammals()
# m.printMembers()

# b = animals.Birds()
# b.printMembers()

# c = animals.Fish()
# c.printMembers()

import animals

harmless_birds = animals.harmless.Birds()
harmless_birds.printMembers()

dangerous_fish = animals.dangerous.Fish()
dangerous_fish.printMembers()