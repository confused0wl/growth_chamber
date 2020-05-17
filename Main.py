# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 12:39:19 2019

@author: me442
"""
import numpy as np
import Air as air
import Environment as enviro
import Chamber as chm
import AHU as ahu
import PlantCanopy as plants
import matplotlib.pyplot as plt
#************************************************************************
ts = 1/6
fl = 0.6
#***************Initialize components***************
outdo_Env = enviro.Environment(15,0.2,170)
indo_Env = enviro.Environment(15,0.2908,0)

vol = 1
PF = chm.Chamber(indo_Env,vol,vol/5,20)
ht = ahu.Heater(60)
cool = ahu.Cooling(80)
vent =ahu.AHU(1)

Canopy = plants.Plants(2,PF.Area)
ACH = 0

#************Conduct heat balance*******************
def conductHeatBalance(PF,outdo_Env,ht,cool,ts,ACH):
  PF.mixedAir(ACH,ts,outdo_Env)
  skinLoss = PF.skinLoss(outdo_Env)
  deltaT = PF.changeTemp(skinLoss,ts)
  deltaT = deltaT + PF.changeTemp(outdo_Env.rad,ts)
  deltaT = deltaT+ PF.changeTemp(ht.output,ts)
  #deltaT = deltaT+PF.changeTemp(cool.output,ts)
  return deltaT
def checkHt(PF,ht):
  if PF.env.temp<17:
    ht.setOn()
  if PF.env.temp>20:
    ht.setOff()
  return ht
def checkCool(PF,cool):
  if PF.env.temp>24:
    cool.setOn()
  if PF.env.temp<22:
    cool.setOff()
  return cool
def checkVent(PF,vent):
  if PF.env.temp>22:
    vent.setOn()
  if PF.env.temp<20:
    vent.setOff()
  return vent

#***************Update Air Properties****************
def updateAir(PF,deltaT):
  PF.env.temp = PF.env.temp+deltaT
  PF.env.RH = PF.env.HR/air.getHR(PF.env.temp)
  
num_steps =5000
temps = np.zeros((num_steps,1))
RHs = np.zeros((num_steps,1))
HRs = np.zeros((num_steps,1))
hts = np.zeros((num_steps,1))
vents = np.zeros((num_steps,1))

for i in range(num_steps):
  #ht = checkHt(PF,ht)
  #cool= checkCool(PF,cool)
  vent = checkVent(PF,vent)
  ACH = vent.output/PF.volume
  deltaT =conductHeatBalance(PF,outdo_Env,ht,cool,ts,ACH)
  updateAir(PF,deltaT)
  temps[i] = PF.env.temp
  RHs[i] = PF.env.RH
  HRs[i] = PF.env.HR
  hts[i] = ht.output
  vents[i] = vent.output
  
fig, axs = plt.subplots(2,2,True,False)
def formatSubs(values, ax):
  ax.plot(np.arange(0,num_steps)/10,values)
  if max(values)!=0:
    ax.set_ylim(0,max(values)*1.2)
  ax.grid()
  ax.minorticks_on()
  ax.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
   
formatSubs(temps, axs[0,0])
formatSubs(HRs, axs[0,1])
formatSubs(vents, axs[1,0])
formatSubs(RHs, axs[1,1])


#axs[0].plot(temps)
#axs[0].set_ylim(0,max(temps)*1.2)
#axs[0].grid()
#axs[0].minorticks_on()
#axs[0].grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
#
#
#   
#axs[1].plot(HRs)
#axs[1].set_ylim(0,max(HRs)*1.2)
#axs[1].grid()
#axs[1].minorticks_on()
#axs[1].grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
#   
#axs[2].plot(hts)
#axs[2].set_ylim(0,max(hts)*1.2)
#axs[2].grid()
#axs[2].minorticks_on()
#axs[2].grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
#
#axs[3].plot(vents)
#axs[3].set_ylim(0,max(vents)*1.2+7)
#axs[3].grid()
#axs[3].minorticks_on()
#axs[3].grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)



#************Conduct Moisture balance***************
Et_f = Canopy.ETr(indo_Env.rad,PF.env.temp,PF.env.RH)


#print(PF.updateAirProperties(PF.env.temp-PF.changeTemp(PF.skinLoss(outdo_Env))))




