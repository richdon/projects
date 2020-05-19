# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 21:38:31 2019

@author: richa
"""
def change_contacts(Email_Lookup):
    name = str(input("Enter the name of the contact who's E-mail you wish to change: "))
    del Email_Lookup[name]
    changed_email = str(input('Enter the new E-mail: '))
    Email_Lookup[name]=[changed_email]

def del_contacts(Email_Lookup):
    del_name= str(input('Enter the name of the contact you would like to delete: '))
    del Email_Lookup[del_name]
    
def show_contacts(Email_Lookup):
    find_Email = str(input("Enter the contact's name to pull up their E-mail: "))
    Email = Email_Lookup.get(find_Email, "That name is not in the directory")
    print(Email)

def add_contact(Email_Lookup):
    name = str(input('Please add you name to the directory: '))
    Email = str(input('Please add your E-mail address to the directory: '))
    Email_Lookup[name] = [Email]

def main():
    Email_Lookup={}
    
    start_end = str(input("press 's' to access E-mail Lookup or press any other keys to close the program: " ))
    while start_end == 's':
    
        choice = str(input(" Enter 'add' if you want to add email/name to the directory \n Enter 'search'if you want to look up an E-mail by entering the name in the directory \n Enter 'delete' if you want to remove the contact from the directory \n Enter 'change' to change the contact info in the directory \n "))
    
        if choice == 'add':
            add_contact(Email_Lookup)
        elif choice == 'search':
            show_contacts(Email_Lookup)
        elif choice == 'delete':
            del_contacts(Email_Lookup)
        elif choice == 'change':
            change_contacts(Email_Lookup)
        else:
            print('That is an invalid entry')
        
        start_end = str(input("press 's' to access E-mail Lookup or press any other key to close the program: " ))
         
    


main()