# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 14:18:23 2019

@author: me442
"""
import Air as air
class Plants:
  def __init__(self, LAI, Area):
    self.LAI  = LAI
    self.area = Area
    self.kt =3600
    self.rc =120
    self.ra =self.rc/1.26
    self.gamma = 66/1000
    self.lamb = 2.2
    
  def ETr(self, Rad, temp, RH):
    slope = air.getSlopeSVP(temp)
    t1 =2*self.LAI/self.lamb
    t2 = (1-0.25)*Rad*3600/(10**6)*slope
    t3 =air.getVPD(temp,RH)*self.kt*air.density*air.cp_air/(10**6)/self.ra
    num =t1*(t3+t2)
    den = self.gamma*(1+1.26)+slope
    Etr =num/den
    if Etr <0:
      Etr = 0
    return Etr