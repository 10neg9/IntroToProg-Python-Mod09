# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# NSmith,6/14/2020,Pasted import code from TestHarness and added comments
# NSmith,6/14/2020,Added code to read file and store contents to list of objects
# NSmith,6/14/2020,Added code to print menu
# NSmith,6/14/2020,Added code to get user's choice
# NSmith,6/14/2020,Added code to show current list of employee objects
# NSmith,6/14/2020,Added code to let user add to employee object list
# NSmith,6/14/2020,Added code to save employee object list to file
# NSmith,6/14/2020,Added code to exit the program
# NSmith,6/14/2020,Added code to let user know their choice is not valid
# ------------------------------------------------------------------------ #
# TODO: Import Modules
if __name__ == "__main__":  # check that this is running as main
    from DataClasses import Employee as Emp  # import Employee class as alias Emp
    from ProcessingClasses import FileProcessor as Fp  # import FileProcessor class as alias Fp
    from IOClasses import EmployeeIO as Eio  # import EmployeeIO class as alias Eio
else:  # raise exception if this has been imported
    raise Exception("This file was not created to be imported")  # Exception raised with message

# print(locals())  # used to check local symbol table, just playing around

# Variables
lstLstTable = []  # list of lists
lstObjTable = []  # list of objects
fn = "EmployeeData.txt"  # file to read current employee data
strChoice = ""  # string to store user's choice

# Main Body of Script  ---------------------------------------------------- #

# Load data from file into a list of employee objects when script starts
lstTable = Fp.read_data_from_file(fn)  # create a list of lists
for i in lstTable:  # iterate through the list of lists
    lstObjTable.append(Emp(i[0], i[1], i[2].strip()))  # add employee object to list of objects

while True:
    # Show user a menu of options
    Eio.print_menu_items()  # use EmployeeIO class of IOClasses Module to print menu

    # Get user's menu option choice, and check for errors
    try:  # check that code will run
        strChoice = Eio.input_menu_options()  # store user's selection
    except Exception as e:  # exception handled
        print(e)  # print error message

    # Show user current data in the list of employee objects
    if strChoice == '1':  # checks if user entered 1
        Eio.print_current_list_items(lstObjTable)  # print current list of employees
        input("Press [Enter] key to return to the menu. ")  # print message to continue

    # Let user add data to the list of employee objects
    elif strChoice == '2':  # checks if user entered 2
        try:  # check that code will run
            lstObjTable.append(Eio.input_employee_data())  # ask user to input new employee data
        except Exception:  # exception handles
            print("Something went wrong inputting employee data.")  # custom error message
        print("New employee info input complete.")  # let user know employee data input is complete
        input("Press [Enter] key to return to the menu. ")  # print message to continue

    # let user save current data to file
    elif strChoice == '3':  # checks if user entered 3
        Fp.save_data_to_file(fn, lstObjTable)  # save list of objects to file
        print("Employee data saved to file.")  # let user know employee data was saved
        input("Press [Enter] key to return to the menu. ")  # print message to continue

    # Let user exit program
    elif strChoice == '4':  # checks if user entered 4
        print('Goodbye!')  # print message
        break  # break the while loop i.e. end program

    # Let user know that 1-4 was not selected
    else:
        print(f"You chose '{strChoice}', but that is not valid.")  # provide feedback to user
        input("Press [Enter] key to return to the menu. ")  # print message to continue

# Main Body of Script  ---------------------------------------------------- #
