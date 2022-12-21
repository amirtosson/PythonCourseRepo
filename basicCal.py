# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 17:33:42 2022

@author: amirt
"""

class BasicCal:

    def sum_two_nums(self, num1, num2):
        res = num1 + num2
        print(res)
        return res
    
    def subtract_two_nums(self, num1, num2):
        res = num1 - num2
        print(res)
        return res
    
    def multi_two_nums(self, num1, num2):
        res = num1 * num2
        print(res)
        return res
    
    def divide_two_nums(self, num1, num2):
        if num2 == 0:
            print("wrong input")
            return 0
        res = num1 / num2
        print(res)
        return res