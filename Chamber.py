# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 15:08:46 2019

@author: me442
"""
import Air as air
import Environment as env
class Chamber:
  def __init__(self,indoor_Env,volume,Area,Uvalue,):
    self.volume = volume
    self.Uvalue = Uvalue
    self.Area = Area
    self.env = indoor_Env
  def updateAirProperties(self,temp, RH):
    self.env.temp = temp
    self.env.RH=RH
    self.env.HR=air.getHR(temp)
  def skinLoss(self,env_outdoor):
    skinLosses = -self.Uvalue*self.Area*(self.env.temp-env_outdoor.temp)
    return skinLosses
  def changeTemp(self, heat_rate, time_step):
    deltaT = heat_rate*time_step/(air.cp_air*air.density*self.volume)
    return deltaT
  def mixedAir(self,ACH, time_step,outdoEnv):
    SAP = ACH*time_step/60/self.volume
    MAHR = self.env.HR*(1-SAP)+outdoEnv.HR*(SAP)
    MAT = self.env.temp*(1-SAP)+outdoEnv.temp*(SAP)
    self.env.HR = MAHR
    self.env.temp = MAT
  def removeHR(self,ACH,coolingRate,time_step):
    SAP = ACH*time_step/60/self.volume
    deltaHR = coolingRate*time_step*60*SAP/(1000)
    self.env.HR = self.env.HR - deltaHR
  def addHR(self, Et_rate,time_step):
    if self.env.RH<1:
      self.env.HR = self.env.HR+Et_rate*time_step
    return self.env.HR

