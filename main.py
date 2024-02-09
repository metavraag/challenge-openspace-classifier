from utils.openspace import Openspace
import configparser
import argparse
import json

# def load_config(config_path):
#     """Load configuration file."""
#     config = configparser.ConfigParser()
#     config.read(config_path)
#     return config

def load_config(json_file_path):
    """Load configuration from a JSON file."""
    with open(json_file_path, 'r') as file:
        config = json.load(file)
    return config


def load_colleagues(file_path):
    """Load colleagues' names from a file."""
    with open(file_path, 'r') as file:
        # names = json.load(file)  # For JSON
        # For plaintext file with one name per line
        names = file.read().splitlines()  
    return names

if __name__ == "__main__":
    # Load config  defaults: 6 tables and 4 capacity per table, colleagues_file_path = './data/new_colleagues.csv'
    # config = load_config('config.ini')
    # colleagues_file_path = config['DEFAULT']['ColleaguesFilePath']
    # number_of_tables = int(config['DEFAULT']['NumberOfTables'])
    # capacity_per_table = int(config['DEFAULT']['CapacityPerTable'])

    config = load_config('config.json')
    number_of_tables = config['NumberOfTables']
    capacity_per_table = config['CapacityPerTable']
    colleagues_file_path = config['ColleaguesFilePath']    

    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Organize seating arrangement for colleagues.")
    # parser.add_argument("filepath", help="path to the configuration file")
    parser.add_argument('-f', '--filepath', help='Path to the file containing the list of colleagues',
                         default=colleagues_file_path)
                        #  default='./data/new_colleagues.csv')

    args = parser.parse_args()
    if args.filepath:
        colleagues_file_path = args.filepath
        # config = load_config(args.filepath)
        # colleagues_file_path = config['DEFAULT']['ColleaguesFilePath']

    
    # Load colleagues
    colleagues = load_colleagues(colleagues_file_path)
    
    # Setup and launch the organizer
    openspace = Openspace(number_of_tables, capacity_per_table)
    openspace.organize(colleagues)
    
    # Display the results
    openspace.display()
    
    # Optionally, store the results in a file
    openspace.store('seating_arrangement.txt')
