# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 20:28:54 2024

@author: Arnav
"""
def draw_filled_square( n ):

    for i in range (n):
    
       print ('* ' * n)
       
    print()
    

#######################################################


def draw_empty_square ( n ):
    
    for i in range (n): 
        
        if ( n - i == n or n - i == 1):
            
            print ('* ' * n)
        
        elif ( n - i != n ):
            
            print('*', end = "")
            
            print('   ' * (n - 2), end = "")
            
            print('*')
            
    print()
            
            
#######################################################


def draw_filled_triangle (n):
    
    for i in range (n):
       
       print("  " * ((n - i) - 1), end = "")
       
       print("* " * ((i * 2) + 1))
       

#######################################################

def draw_inverted_triangle (n):
    
    for i in range (n):
       
      print((" " * (i * 2)) + ("* " * ((2*n - 1) - (i * 2))))


#######################################################
            
draw_filled_square( 5 )
draw_empty_square( 5 )
draw_filled_triangle( 5 )
draw_inverted_triangle( 5 )

    
