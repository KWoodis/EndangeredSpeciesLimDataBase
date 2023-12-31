#Functions for database
import pandas as pd

#List of species first column in excel sheet
def species_list():
    cols = [0]
    df = pd.read_excel('Endangered_list.xlsx', usecols=cols)
    print(df)
'''
    function to list species from the excel sheet Species column
    Args:
        No argument. Function calls species column by reading excel file
        *args: The variable arguments are used so just the species column is printed
                column location is defined as a variable
                prints list from function
'''

def pop_month(pop, months):
    x = 0
    try:
        x = pop/months
    except ZeroDivisionError:
        print('Invalid. Cannot divide by 0')
    finally:
        print('Result is', x)
        
'''
    Purpose of function to make sure result is not dividing by 0. Exception handling
    
    Args:
        population argument derived from dataframe value variable separately
        months argument from user input prompt
        *args: variable arguments are not used. placeholding variable x gets rewritten
        for division algorithm. exception ZeroDivision Error. Result is returned
'''
       
def total_pop(year1, year2, year3):
    total = year1 + year2 + year3
    return total

'''
    Simple sum calculation to total 3 values from Population columns from dataframe
    Args:
        Args for function were pulled from dataframe query and separated into variables
        *args: Simple sum calculation that returns total
'''

def system_query(choice):
    df = pd.read_excel('Endangered_list.xlsx')
    system_id = df[df['System'] == choice]
    return system_id
'''
    function reads Endangered_list excel sheet and creates data view from System column
    based on user input. List of entries that satisfy the filter conditions are returned
    Args:
        choice argument is made from user input 
        *args: variable argument targets System column in dataframe with user choice values 
        pulled
    List of entries that satisfy the user input choice are returned
'''
