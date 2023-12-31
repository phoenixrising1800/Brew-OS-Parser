import os
import sys
from bitstring import ConstBitStream
from src.sms import *
from src.contacts import *

def input_file():
    filename = input("Path to binary BREW OS memory image file: ")
    return filename

def main():
    ## Prompt user to specify file from path 
    file = input_file()
    while file == "":
        print("Enter valid path to file")
        file = input_file()

    ## Print file size (if file exists)
    try: 
        file_size_bytes = os.path.getsize(file)
    except FileNotFoundError:
        print("File does not exist, try again.")
        sys.exit(1)
    print(f'File size: {file_size_bytes} bytes') 
    print("*****************************************************************")

    #### EXTRACT CONTACT DATA
    contactEntries = getContacts(file)
    print("\nTotal contact entries found: " + str(contactEntries))
    print("*****************************************************************")

    #### EXTRACT SMS DATA
    smsEntries = getSMS(file)
    print("\nTotal SMS data entries found: " + str(smsEntries))
    
if __name__ == '__main__':
    main()