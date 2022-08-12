#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Sal runs the biggest shipping company in the tri-county area, Sal’s Shippers. Sal wants to make sure that every single one of his customers has the best, and most affordable experience shipping their packages.

#In this project, you’ll build a program that will take the weight of a package and determine the cheapest way to ship that package using Sal’s Shippers.

#Sal’s Shippers has several different options for a customer to ship their package:

# 1) Ground Shipping, which is a small flat charge plus a rate based on the weight of your package.
    # Weight of Package	Price per Pound	Flat Charge
    # 2 lb or less	$1.50	$20.00
    # Over 2 lb but less than or equal to 6 lb	$3.00	$20.00
    # Over 6 lb but less than or equal to 10 lb	$4.00	$20.00
    # Over 10 lb	$4.75	$20.00
  
# 2) Ground Shipping Premium, which is a much higher flat charge, but you aren’t charged for weight.
    # Flat charge: $125.00
  
# 3) Drone Shipping (new), which has no flat charge, but the rate based on weight is triple the rate of ground shipping.
    # Weight of Package	Price per Pound	Flat Charge
    # 2 lb or less	$4.50	$0.00
    # Over 2 lb but less than or equal to 6 lb	$9.00	$0.00
    # Over 6 lb but less than or equal to 10 lb	$12.00	$0.00
    # Over 10 lb	$14.25	$0.00

# Code:

weight = 41.5 #in lbs
print('Weight (lbs): ', weight)

#Ground Shipping
costGroundShipping = 0 #in dollars
if weight <= 2:
  costGroundShipping = (1.5*weight)+20
elif weight <= 6:
  costGroundShipping = (3*weight)+20
elif weight <= 10:
  costGroundShipping = (4*weight)+20
else:
  costGroundShipping = (4.75*weight)+20
print('Ground Shipping Cost ($): ', costGroundShipping)

#Premium Ground Shipping
costPremiumGroundShipping = 125

print('Premium Ground Shipping Cost ($): ', costPremiumGroundShipping)

#Drone Shipping
costDroneShipping = 0
if weight <= 2:
  costDroneShipping = 4.5*weight
elif weight <= 6:
  costDroneShipping = 9*weight
elif weight <= 10:
  costDroneShipping = 12*weight
else:
  costDroneShipping = 14.25*weight
print('Drone Shipping Cost ($): ', costDroneShipping)
