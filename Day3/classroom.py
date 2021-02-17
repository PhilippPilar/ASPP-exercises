# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 14:22:50 2021

@author: Admin
"""

class Person():    
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname
        
    def name(self):
        return self.firstname + ' ' + self.lastname
    
class Student(Person):
    def __init__(self,firstname,lastname,subjectarea):
        super(Student,self).__init__(firstname,lastname)
        self.subjectarea = subjectarea
        
    def info(self):
        buf = self.name()
        print(buf + ' ' + self.subjectarea)
    
class Teacher(Person):
    def __init__(self,firstname,lastname,course):
        super(Teacher,self).__init__(firstname,lastname)
        self.course = course
        
    def info(self):
        buf = self.name()
        print(buf + ' ' + self.course)
    