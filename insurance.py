# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 17:54:46 2020

@author: richa
"""

import os

def main():
    initiate = True
    vehical = input('Enter the vehical make, Toyata(T) or Honda(H): ').lower()
    driveType = input('is the vehical AWD (Y/N): ').lower()
    
    while initiate:
        insurance_check(vehical, driveType)
        

def insurance_check(vehical, driveType):
 
    if vehical == 'h':
        if driveType == 'y':
            fee = 450
            print (f'A Honda that is All Wheel Drive costs: ${fee}')
            check_more_vehicals()
        elif driveType == 'n':
            fee = 350
            print(f'A Honda that is not All Wheel Drive costs: ${fee}')
            check_more_vehicals()
        else:
           print('Invalid input. Enter (Y/N)')

    elif vehical =='t':
        if driveType == 'y': 
            fee = 300
            print(f'A Toyota that is All Wheel Drive costs: ${fee}')
            check_more_vehicals()
        elif driveType == 'n':
            fee = 250
            print(f'A Toyota that is not All Wheel Drive costs: ${fee}')
            check_more_vehicals()
        else:
            print('Invalid input. Enter (Y/N)')
            main()
    else:
       print('Invalid input. Enter Toyota (T) or Honda (H)' )
       main()
      

        
def check_more_vehicals():
 
    choice = input('Do you have more vehicals that you would like to insure?(Y/N): ').lower()
    
    
    if choice =='y':
        main()
   
    elif choice =='n':
        os._exit(0)
    else:
        print('Invalid input. Enter (Y/N)')
        check_more_vehicals()
        
main()
        