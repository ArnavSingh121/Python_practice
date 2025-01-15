# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 12:16:25 2025

@author: Arnav
"""


def simple_interest(p,t,r):
    
    print('The principal is', p)
    
    print('The time period is', t)
    
    print('The rate of interest is',r)
    
    si = (p * t * r)/100
    
    print('The Simple Interest is', si)
    
    
    print()



###############################################################################

def compound_interest(p,r,t,n):
    
    print("The principal is", p)
    
    print("The time period is", t)
    
    print("The rate of interest is",r)
    
    ci = p * (1 + r / n) ** (n*t)
    
    print("The Compound Interest is", ci)
    
    
    
###############################################################################
    
def Prime_Numbers(x,y):
    
    list_primes = []
    
    
    for i in range (x, y):
    
        if i == 0 or i == 1:
            continue
        
        else:
            for x in range(2, int(i/2) + 1):
                if i % x == 0:
                    break
                
            else: 
                list_primes.append(i)
                    
    print("the prime numbers are >> ", list_primes)
        
        
    






#simple_interest(8, 6, 8) 

#compound_interest(3, 4, 1, 6)

Prime_Numbers(2, 10)