# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 16:20:08 2019

@author: me442
"""
# AHU capacity should be in m3/min

class AHU:
  def __init__(self, maxFlow):
    self.maxflow = maxFlow
    self.isOn = False
    self.output = 0
  def setOn(self):
    self.isOn =True
    self.output =self.maxflow
  def setOff(self):
    self.isOn = False
    self.output = 0
    
    
    # Heater capacity should be in Watts
class Heater:
  def __init__(self,capacity):
    self.capacity = capacity
    self.isOn = False
    self.output = 0
  def setOn(self):
    self.isOn =True
    self.output =self.capacity
  def setOff(self):
    self.isOn = False
    self.output = 0
    
    
    # Cooling capacity should be in Watts
class Cooling:
  def __init__(self,capacity):
    self.capacity = capacity
    self.isOn = False
    self.output = 0
  def setOn(self):
    self.isOn =True
    self.output =-self.capacity
  def setOff(self):
    self.isOn = False
    self.output = 0
    
  