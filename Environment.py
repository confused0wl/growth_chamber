# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 15:36:31 2019

@author: me442
"""
import Air as air
class Environment:
  def __init__(self, temp, RH, Rad):
    self.temp = temp
    self.RH = RH
    self.HR = air.getHR(temp)*self.RH
    self.rad = Rad

  

