
# Import all required package/function
from pathlib import Path
from ast import literal_eval

# directory = Path(path to directory)
# file_name = 'test.txt'

# file_path = directory / filename

# Request user to enter folder name with all the data files

# Iterate through the list of files and read as separate variables


# Function to load data from existing file
def load_data(file_name):
# Load the data from the file and use it to initialise program state
    try:
        with open(file_name, 'r') as file:
            data = literal_eval(file.read())
            return data
    # Handle error during file opening
    except FileNotFoundError:
        print("File not found. Creating new empty variable...")
        return " "
    except PermissionError:
        print("Permission error: You don't have access to the file.")
    except IOError as e:
        print(f"Error reading the file: {e}")
        return " "

    

# Function to write data to existing file
def write_data(file_name, data):
# Open file in write mode
    with open(file_name, 'w') as file:
        file.write(str(data))
