# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 15:44:20 2021

@author: Rajesh
"""


def savings (current_savings , portion_down_payment , \
             annual_salary , semi_annual_raise , guessed_savings_rate):
    
    for number_of_months in range(0 , 36):
        if number_of_months % 6 == 0 and number_of_months != 0:
            annual_salary += annual_salary * semi_annual_raise
            
        current_savings += guessed_savings_rate * annual_salary / 12 \
                        + current_savings * 0.04 / 12
                        
    return current_savings

def test_case(annual_salary):
    total_cost = 1000000
    semi_annual_raise = 0.07
    
    portion_down_payment = 0.25 * total_cost
    current_savings = 0
    
    steps_in_bisection_search = 0
    low = 0
    high = 10000
    
    guess = int((low + high) / 2)
    guessed_savings_rate = guess / 10000
        
    current_savings = savings (0 , portion_down_payment , \
                               annual_salary , \
                               semi_annual_raise , high/10000)
    
    if current_savings < portion_down_payment:
        print ("Unfortunately, it is not possible to pay for the down payment \
               in 36 months :(")
    else:
        current_savings = savings (0 , portion_down_payment , \
                                   annual_salary , \
                                   semi_annual_raise , guessed_savings_rate)
        steps_in_bisection_search += 1
        
        while abs(portion_down_payment - current_savings) >= 100:
    
            if  portion_down_payment > current_savings:
                low = guess
            else:
                high = guess
            guess = int((low + high) / 2)
            guessed_savings_rate = guess / 10000
            
            current_savings = int(savings (0 , portion_down_payment , \
                                       annual_salary , semi_annual_raise , \
                                       guessed_savings_rate))
            steps_in_bisection_search += 1
        print(guessed_savings_rate,steps_in_bisection_search)
        return guessed_savings_rate,steps_in_bisection_search

def main():
    
    annual_salary = 150000
    guessed_savings_rate_test = 0.4411
    steps = 12
    guessed_savings_rate , steps_in_bisection_search = test_case(annual_salary)
    
    if guessed_savings_rate_test == guessed_savings_rate and steps == steps_in_bisection_search:
        print("\033[1;32;32m Test case 1 passed!!")
        
        annual_salary = 300000
        guessed_savings_rate_test = 0.2206
        steps = 9
        guessed_savings_rate , steps_in_bisection_search = test_case(annual_salary)
        
        if guessed_savings_rate_test == guessed_savings_rate and steps == steps_in_bisection_search:
            print("\033[1;32;32m Test case 2 passed!!")
        else:
            print("\033[1;31;31m Test case 2 Failed!!")

    else:
        print("\033[1;31;31m Test case 1 Failed!!")



if __name__ == '__main__':
    main()