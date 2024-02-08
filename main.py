from utils.openspace import Openspace
import configparser
import json

def load_config(config_path):
    """Load configuration file."""
    config = configparser.ConfigParser()
    config.read(config_path)
    return config

def load_colleagues(file_path):
    """Load colleagues' names from a file."""
    with open(file_path, 'r') as file:
        # Assuming the file contains names in a JSON array or one name per line
        # names = json.load(file)  # For JSON
        names = file.read().splitlines()  # For plaintext file with one name per line
    return names

if __name__ == "__main__":
    # Load config
    config = load_config('config.ini')
    colleagues_file_path = config['DEFAULT']['ColleaguesFilePath']
    
    # Load colleagues
    colleagues = load_colleagues(colleagues_file_path)
    
    # Setup and launch the organizer
    number_of_tables = int(config['DEFAULT']['NumberOfTables'])
    capacity_per_table = int(config['DEFAULT']['CapacityPerTable'])
    
    openspace = Openspace(number_of_tables, capacity_per_table)
    openspace.organize(colleagues)
    
    # Display the results
    openspace.display()
    
    # Optionally, store the results in a file
    openspace.store('seating_arrangement.txt')
