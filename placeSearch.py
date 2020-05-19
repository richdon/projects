# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 00:42:02 2020

@author: richa
"""

import requests

print('Welcome to U.S PlaceSearch!')
initiate = True

while initiate:
       
    paramType = input('Would you like search by phone number(p),address(a), or name (n): ')

    if paramType == 'p'.lower():
        phone = input('Enter the 10 digit phone number of the location: ')
        parameters = '+1'+phone
    
    elif paramType == 'a'.lower():
        address = input('Enter the address of the location: ')
        parameters = address
    
    elif paramType == 'n'.lower():
        name = input('Enter the name of the location: ')
        parameters = name
    else:
        print('That is not a valid entry')
        
    API_key = 'AIzaSyAqIcWFXcXyumPjT_qDt36IBjQhTPTRGYk'
    
    try:
        id_response = requests.get(f'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={parameters}&inputtype=textquery&key={API_key}')

        for item in id_response:
            data = id_response.json()
            can = data["candidates"]

            placeid = can[0]["place_id"]

        details_response = requests.get(f'https://maps.googleapis.com/maps/api/place/details/json?place_id={placeid}&fields=name,rating,formatted_phone_number,formatted_address,url&key={API_key}')

        for i in details_response:
            item = details_response.json()

        details = item['result']

        if paramType == 'n'.lower():
           print(f"\nThe phone number is: {details['formatted_phone_number']}")
           print(f"The address is: {details['formatted_address']}" )
           print(f"The rating is: {details['rating']}")
           print(f"The google maps url to this location is: {details['url']}")
                                                           
        elif paramType == 'p'.lower():
            print(f"\nThe name of this location is: {details['formatted_address']}")
            print(f"The address is: {details['formatted_address']}" )
            print(f"The rating is: {details['rating']}")
            print(f"The google maps url to this location is: {details['url']}")
           
            
        elif paramType == 'a'.lower():
            print(f"\nThe name of this location is: {details['formatted_address']}")
            print(f"The phone number is: {details['formatted_phone_number']}")
            print(f"The rating is: {details['rating']}")
            print(f"The google maps url to this location is: {details['url']}")
        
        choice = input('Would you like to search another place (Y/N)?: ')
        
        if choice == 'y':
            pass
        elif choice == 'n'.lower():
            break
        else:
            print('Enter Yes or No (Y/N): ')
              
    except:
        print('Place not found.') 
        choice = input('Would you like to search another place (Y/N)?: ')
        if choice == 'y':
            pass
        elif choice == 'n'.lower():
            break
           
        
    
    

        

    
   
        
        
                                                                                                                                                            
            
    
    
    
        
        


