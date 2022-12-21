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

while True:
    cal_type = input("Which calculator:\n b for basic\n a for advanced \n s for scientific\n q for quite\n")
    if cal_type == "s":
        print(cal_type)
    elif cal_type == "b":
        basic_cal_obj = BasicCal()

        while True: 
            num1_user = input("enter the first number or q to quite\n")
            if num1_user == "q":
                break
            
            num2_user = input("enter the second number q to quite\n")
            if num2_user == "q":
               break
           
            if not num1_user.isdigit() or not num2_user.isdigit():
                print("You entered not valid numbers")
                continue
            
            operation_user = input("Which operation\n s for subtraction\n a for sum\n m for multi\n d for division\n  q for quite\n")
            
            if operation_user == "s":
                result = basic_cal_obj.subtract_two_nums(int(num1_user), int(num2_user))
                print("My result is: ", result)
                
            elif operation_user == "a":
                result = basic_cal_obj.sum_two_nums(int(num1_user), int(num2_user))
                print("My result is: ", result)
                
            elif operation_user == "m":
                result = basic_cal_obj.multi_two_nums(int(num1_user), int(num2_user))
                print("My result is: ", result)
                
            elif operation_user == "d":
                result = basic_cal_obj.divide_two_nums(int(num1_user), int(num2_user))
                print("My result is: ", result)
                
            elif operation_user == "q":
                break
            
            else:
                print("Wrong")
                
    elif cal_type == "a":
        print(cal_type)
    elif cal_type == "q":
        break
    else:
        print("Wrong")





"""
basic_cal_obj = BasicCal()

result = basic_cal_obj.sum_two_nums(9, 10)

print("My result is: ", result)

result2 = basic_cal_obj.divide_two_nums(8, 0)

print("My result is: ", result2)
scientific_cal_obj = ScientificCal()
scientific_cal_obj.test_print()

advanced_cal_obj = AdvancedCal()
advanced_cal_obj.test_print()
"""