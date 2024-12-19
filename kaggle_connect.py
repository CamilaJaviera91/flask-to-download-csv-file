from kaggle.api.kaggle_api_extended import KaggleApi as ka
import pandas as pd
from pathlib import Path
import curses

def kaggle_connect(stdscr):
    try:
        # "Download" base path
        base_folder = Path("./")

        # Initialize the API and authenticate
        api = ka()
        api.authenticate()

        # Clear the screen for the curses menu
        stdscr.clear()
        stdscr.refresh()

        # Prompt for the search term
        stdscr.addstr("Search for data (press Enter to skip): ")
        stdscr.refresh()
        curses.echo()
        search_term = stdscr.getstr().decode('utf-8').strip()
        curses.noecho()
        if not search_term:

            stdscr.addstr("No search term entered. Exiting...")
            stdscr.refresh()
            stdscr.getch()
            return None

        # List datasets related to the search term
        datasets = api.dataset_list(search=search_term)
        datasets = list(datasets)  # Convert to list for indexing
        if not datasets:

            stdscr.addstr("No datasets found for the search term.")
            stdscr.refresh()
            stdscr.getch()
            return None
        
        # Display datasets and prompt for selection
        stdscr.addstr("Datasets found:\n\n")
        stdscr.refresh()  # Refresca para mostrar el texto en pantalla
        for i, dataset in enumerate(datasets):
            stdscr.addstr(f"{i + 1}){dataset.ref}\n")
            stdscr.refresh()  # Refresh after every line


        stdscr.addstr("\nEnter the number of the dataset to download: ")
        stdscr.refresh()
        curses.echo()
        try:
            option = int(stdscr.getstr().decode('utf-8'))
            curses.noecho()
            if option < 1 or option > len(datasets):
    
                stdscr.addstr("Invalid selection. Exiting.")
    
                stdscr.refresh()
                stdscr.getch()
                return None
            
            # Dataset selection
            data_ref = datasets[option - 1].ref
        
        except ValueError:
            curses.noecho()
            stdscr.addstr("Invalid input. Please enter a number.")

            stdscr.refresh()
            stdscr.getch()
            return None

        # Destination folder for the download
        fixed_folder_name = "dataset"  # Nombre fijo del directorio
        download_path = base_folder / fixed_folder_name

        # Create the folder if it doesn't exist
        if not download_path.exists():
            download_path.mkdir(parents=True, exist_ok=True)

        # Download the dataset and unzip it in the specified folder
        stdscr.addstr("\nDownloading dataset...")
        stdscr.refresh()
        api.dataset_download_files(data_ref, path=str(download_path), unzip=True)

        # List all CSV files in the download directory
        csv_files = list(download_path.glob('*.csv'))
        if not csv_files:
    
             stdscr.addstr("No CSV files found in the dataset.")
        else:
            # Select the first CSV file in the directory
            csv_file = csv_files[0]

            stdscr.addstr(f"\nLoading dataset from: {csv_file}")
            stdscr.refresh()

        # Load the dataset into a DataFrame
            df = pd.read_csv(csv_file)

            stdscr.addstr("\nDataset loaded successfully.")
            stdscr.refresh()

        stdscr.getch()
        return df
    
    except Exception as e:
        stdscr.addstr(f"An error occurred: {e}")
        stdscr.refresh()
        stdscr.getch()
        return None
#To test we type "Boston Housing Dataset" and we select option 7 (willianleite/boston-housing-dataset)    
#curses.wrapper(kaggle_connect)