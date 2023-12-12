from porsche import Carrera
import pandas as pd


###### Information
# In order to perform an entire model, here are the **kwargs information you need to enter:
# model, price, year


# All 911 type cars
# What makes the 911 different is that it has different phases and it can be convertible

# Carrera 992
carrera = Carrera("992", False, model="911 Carrera", price=124885, year=2020)

# Carrera 992 T
carrera_T = Carrera("992", False, model="911 Carrera T", price=139559, year=2020)

# Carrera 992 S
carrera_S = Carrera("992", False, model="911 Carrera S", price=140485, year=2020)

# This is an example of things that do not work.
carrerataycan = Carrera("992", False, model="Taycan Turbo", price=200000, year=2021)






# print(carrerataycan.carrera_name())
# returns assertion error

