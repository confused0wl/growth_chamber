# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 14:56:27 2019

@author: me442
"""
import numpy as np
# Sensible Heat flux in the foliage layer
# Leaf Area Index
LAI = 2
#******************** Air properties near foliage**************************

# ******************* density
rho_a = 1.225                       # density of air at instrument height
rho_f = 1.225                       # density of air at leaf temperature
rho_af = 0.5*(rho_a+rho_f)          # density of air near the foliage model
C_pa = 1005                         # Heat capacity of air 
sigma_f = 0.95                      # ratio of shaded ground surface to total 
                                    # ground surface area

#*****************    temperature
T_a = 283            # temperature of air at instrument height in Kelvin
T_f = 284            # leaf temperature in kelvin
T_g = 286            # ground surface temperature in kelvin
T_af = (1-sigma_f)*T_a+sigma_f*(0.3*T_a + 0.6*T_f + 0.1*T_g)

#****************     Wind coefficients

W = 2                         # larger of 2 or actual wind speed above canopy
Kv = 0.4                      # Karmens constant
Z_a = 0.1
Z_f = 0.1                     # ??? foliage height          
Z_d = 0.701*Z_f**(0.979)      # Zero displacement height in meters
Z_fo = 0.131*Z_f**(0.997)     # foliage roughness length scale
C_hfn = (Kv**2)*np.log((Z_a - Z_d)/Z_fo)**-2  # Transfer coefficient at atmospheric stability conditions

# ***********      Foliage Wind Speed
W_af = 0.83*sigma_f*W*(C_hfn**0.5)+(1-sigma_f)*W

#      Bulk transfer coefficient as defined by Deardorff

C_f = 0.01*(1+(0.3/W_af))
H_f = (1.1*LAI*rho_af*C_pa*C_f*W_af)*(T_af-T_f)

print(H_f)