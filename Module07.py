# ------------------------------------------------- #
# Title: Module07
# Description: A simple example of storing data in a binary file
# ChangeLog: (Who, When, What)
# <LFerrier>,<11.29.2022>,Created Script
# ------------------------------------------------- #
import pickle

# Data -------------------------------------------- #
strFileName = 'RabbitManagement.dat'

# Processing -------------------------------------- #
def save_data_to_file(file_name, list_of_data):
    file = open(file_name, "ab")
    for data in list_of_data:
        pickle.dump(data, file)
    file.close()

def read_data_from_file(file_name):
    file = open(file_name, "rb")
    list_of_data = []
    while(True):
        try:
            data = pickle.load(file)  # load() only loads one row of data.
            list_of_data.append(data)
        except EOFError:
            break
    file.close()
    return list_of_data

def print_bunnies(list_of_data):
    for data in list_of_data:
        print(str(data[0]) + ": " + data[1])

# Presentation ------------------------------------ #
while(True):
    try:
        intId = int(input("Enter the Rabbit's ID #: "))
    except Exception as e:
        print("Invalid ID # input, please try again! Error: " + str(type(e)))
        continue
    strName = str(input("Enter Rabbit's Name: "))
    bunnyEntry = [intId, strName]
    print("...")
    save_data_to_file(strFileName, [bunnyEntry])
    print("Rabbit Saved!")
    print("*******************************************")
    print("Hit any key to add more rabbits or type 'Exit' to review all")

    # If Option Exit is Selected
    strUserInput = input()
    if strUserInput == "Exit":
        break

print("*******************************************")
print("All Current Buns:")
print_bunnies(read_data_from_file(strFileName))