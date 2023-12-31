import pandas as pd
import numpy as np
import fp_functions
import matplotlib.pyplot as plt
import fp_functions
'''
    module contains pandas support module and species list for menu option
    Args:
        No argument. Function calls species column by reading excel file
        *args: The variable arguments are used so just the species column is printed
                column location is defined as a variable
                prints list from function
'''

#function for search history option 
def recent_searches():
    with open('search_history.txt', 'r') as f: #open search history txt file
        content = f.readlines()
        print(content)             #print lines
'''
    Args:
        No arguments. Opens search history archive in txt document to read
        readlines attribute is used
        
    content is printed from function instead of returned
'''







#Opening message to user
print('Hello and Welcome to Sample Mammal Species Database')
print()
print('Please select an option 1 though 5 from the following menu:\n')
#Opening Menu 1 Options (main)
main_menu = ('Options:\n'
      '1) Access Database\n'
      '2) See Species List\n'
      '3) Quit')
print(main_menu)
option = input('User Option Select: ')  #first option input
print('----------------------------------------------------------------------')
print()

#Menu 1 looping satements
while option != '3':
    if option == '1':
        print('Thank you! Please proceed')
        #Database sub menu
        dataopt = input('Database includes 30 animal species,\n'
                                  'their status, current population,\n'
                                  'population in year 2021, population in 2020,\n'
                                  'and environment system. Please select species \n'
                                  '--------------------------------------------------- \n'
                                  'Type 1 to place query\n'
                                  'Type 2 to see species list\n'     #option leads to function
                                  'Type 3 to see search history\n'   #option leads to function
                                  'Type 4 to quit\n'
                                  'Insert command: '
                                  )
        #Query menu
        while dataopt != '4':
            if dataopt == '1':
                
                    df = pd.read_excel('Endangered_list.xlsx', index_col = 'Species') #index converted to species column
                # with open('search_history.txt', 'w') as f:     #open txt file for writing
                    # key_lis = []
                    key_ani = input('Select mammal species: ')  #key animal variable
                    with open('search_history.txt', 'a') as f:     #open txt file for writing
                        f.write("{}\n".format(key_ani))
                        #archive search results in txt file

                    y_n = input('Would you like to view search history? Yes or No: ')
                    #prompt to view search history in txt file
                    if y_n == 'yes' or y_n == 'Yes':
                            recent_searches()       #calls recent_searches function
                            print('\n\n')
                    elif y_n == 'no' or y_n == 'No':    #continues to next prompt
                        continue
                    else:
                        continue

                    print(df.loc[key_ani])  
                    print('Information on your query for', key_ani)#displays row by index selection
                    key_pop = (df.at[key_ani, "Current Population"])
                    mon = int(input('Current population divided by how many months?'
                                'Insert number of months: '))
                    fp_functions.pop_month(key_pop, mon) 
                    #calls function dividing key pop by user months
                    print('Alive per month')
                    year_2021_pop = (df.at[key_ani, "2021 Population"])
                    year_2020_pop = (df.at[key_ani, "2020 Population"])
                    print("\n\n\n")
                    totals = fp_functions.total_pop(key_pop,year_2021_pop,year_2020_pop)
                    print('Total population over past 3 years:', totals)
                    query = input('What would you like to know?: \n '   #second option query
                        '----------------------------------\n\n'
                        '1) Populations over last 2 years\n'    #includes graph
                        '2) Current population of first 3 entries\n'               #includes graph
                        '3) Environment system\n'              #System queries
                        '4) Quit\n'                       
                        'Command: ')
                    while query != '4':
                        if query == '1':
                            df = pd.read_excel('Endangered_list.xlsx')  #dataframe of excel sheet
                            # values = df[['Species', 'Current Population']]
                            # mylist = df['Current Population'].tolist()
                            # print(mylist)
                            # ax = values.plot.line(x='Species', y='Current Population', rot=0)
                            # plt.show()
                            df.reset_index().plot(x="Species", y=["Current Population", "2021 Population", "2020 Population"], kind="bar")
                            #FIX PLOT STYLES
                                                                                    
                            plt.title("Population Comparison")     #graph title
                            plt.xlabel("Species")              #graph x axis label
                            plt.ylabel("Population(millions)")   #graph y axis label
                            plt.show()
                            
                            query = input('Insert Command: ')     #third command prompt
                        elif query == '2':
                            df = pd.read_excel('Endangered_list.xlsx')
                            #dataframe of excel sheet
                            df2 = df.head(3)
                            
                            values = df2[['Species', 'Current Population']]  #species and current population column values
                            print(values)
                            mylist = df2['Current Population'].tolist()   #current population column to list
                            mylist2 = df2['Species'].tolist()          #species column to list
                            plt.plot(mylist2, mylist)         #plotting using list 1 and list 2
                            plt.xlabel("Species")        #styles for second graph
                            plt.ylabel("Population total (millions)")
                            plt.title('Current Population')
                            plt.show()
                            print('Current population of first 3 entries')

                            query = input('Insert Command: ')
                            
                        elif query == '3':        #System column queries
                            print('To see which species belong to which environmental ecosystem,\n'
                                  'choose from the options:\n'
                                  '1)Terrestrial\n'
                                  '2)Marine\n'
                                  '3)Quit')
                            syst =input('Insert Command(Type Terrestrial or Marine. Otherwise, type 3): ')
                            result_syst = fp_functions.system_query(syst) 
                            #function call from module returns entries that satisfy user condition
                            #syst is function argument variable
                            print(result_syst)
                            syst =input('Insert Command: ')
                            if syst == '3':
                                break
                            
                    
                        
                        
                        elif query == '4':
                            break
                        else:
                            print('Invalid selection')
                            query = input('Insert Command: ')

            elif dataopt == '2':            #Query menu option
                fp_functions.species_list()        #species list function
                dataopt = input('Insert Command: ')
            elif dataopt == '3':             #query option menu
                recent_searches()            #search archive function call
                dataopt = input('Insert command: ')
            elif dataopt == '4':
                break                #break loop
            else:
                print('Invalid Selection')
                dataopt = input('Insert command: ')
    elif option == '2':           #second main menu option 
        fp_functions.species_list()               #function for species list (module)
        option = input('Insert command: ')
    elif option == '3':
        break                    #break loop
    else:
        print('Invalid Selection')
        option = input('Insert Command: ')

                
                
                
                                    
