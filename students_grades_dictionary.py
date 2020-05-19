# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 19:37:53 2020

@author: richa
"""

def main():
    
    studentName = ["Terry", "John", "Susan", "Rondell", "Aaron", "Kalifa"]

    studentGrade = [[79, 85, 82], [65, 69, 73], [91, 93, 80], [45, 70, 81], [83, 85, 80], [90, 93, 82]]
    
    name_grade_dict = dict(zip(studentName, studentGrade))
    
    name = input("Enter the name of the student: ")
    
    calculate_avg(name,studentGrade,studentName)
    
    find_lowest(name_grade_dict, name)
    
    find_highest(name_grade_dict, name)

def calculate_avg(name,studentGrade,studentName):
    
    avgs = []
    for grades in studentGrade:
        
        avgs.append(sum(grades)/len(grades))
    
    studentAvg = dict(zip(studentName, avgs))
    
    avgGrade = studentAvg.get(name, 'not found')
            
    print(f"{name}'s average grade is",avgGrade)

def find_lowest(name_grade_dict, name):
    
    student = name_grade_dict.get(name, "not found")
    
    lowestGrade = min(student)
    print(f"{name}'s lowest grade is: {lowestGrade}")

def find_highest(name_grade_dict, name):
    
    student = name_grade_dict.get(name, "not found")
    
    highestGrade = max(student)
    print(f"{name}'s highest grade is: {highestGrade}")

    
main()