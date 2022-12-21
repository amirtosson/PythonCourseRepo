# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 17:23:01 2022

@author: amirt
"""
import matplotlib.pyplot as plt
import numpy as np

from basicCal import BasicCal 
from scientificCal import ScientificCal
from advancedCla import AdvancedCal

basic_cal_obj = BasicCal()
basic_cal_obj.test_print()


scientific_cal_obj = ScientificCal()
scientific_cal_obj.test_print()

advanced_cal_obj = AdvancedCal()
advanced_cal_obj.test_print()