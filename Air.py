# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 12:40:46 2019

@author: me442
"""

cp_air = 718
density = 1.225

# get slope of saturated vapor pressure curve at temp
def getSlopeSVP(temp):
  if temp < 0:
     temp = 0
  if temp > 41:
    temp = 41
  slopeSVP = 4*(0.00055742)*(temp**3)+3*0.01650908*(temp**2)+2*1.58627097*temp+43.49552629
  slopeSVP = slopeSVP/1000
  return slopeSVP

# Get saturated vapor pressure
def getSVP(temp):
  if temp < 0:
     temp = 0
  if temp > 41:
     temp = 41
  SVP = (0.00055742)*(temp**4)+0.01650908*(temp**3)+1.58627097*(temp**2)+43.49552629*temp+612.139
  SVP = SVP/1000
  return SVP
  
# get vapor pressure defecit 
def getVPD(temp,RH):
  comp_RH = 1-RH
  VPD = comp_RH*getSVP(temp)
  return VPD

#convert celsius to farenheit
def ctoF(temp):
  tempF = temp*1.8+32
  return tempF

# Get saturated humidity ratio
def getHR(temp):
  temp =ctoF(temp)
  if temp< -10:
    temp = -10
  if temp > 109:
    temp = 109;
  HR = (1.87357664525192*(10**-12))*(temp**5)+(5.74111223515208*(10**-11))*(temp**4)+(1.37856755313732*(10**-8))*(temp**3)+(1.15613338426377*(10**-6))*(temp**2)+0.0000412018683038945*temp+0.00077966191962974
  return HR

