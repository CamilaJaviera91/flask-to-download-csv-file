# kaggle_connect.py

from kaggle.api.kaggle_api_extended import KaggleApi
import pandas as pd
from pathlib import Path

def kaggle_connect(search_term):
    try:
        # "Download" base path
        base_folder = Path("./dataset")

        # Initialize the API and authenticate
        api = KaggleApi()
        api.authenticate()

        # List datasets related to the search term
        datasets = api.dataset_list(search=search_term)
        datasets = list(datasets)  # Convert to list for indexing
        if not datasets:
            return None, "No datasets found for the search term."
        
        # Choose the first dataset (for simplicity)
        data_ref = datasets[0].ref

        # Destination folder for the download
        fixed_folder_name = "dataset"  # Nombre fijo del directorio
        download_path = base_folder / fixed_folder_name

        # Create the folder if it doesn't exist
        if not download_path.exists():
            download_path.mkdir(parents=True, exist_ok=True)

        # Download the dataset and unzip it in the specified folder
        api.dataset_download_files(data_ref, path=str(download_path), unzip=True)

        # List all CSV files in the download directory
        csv_files = list(download_path.glob('*.csv'))
        if not csv_files:
            return None, "No CSV files found in the dataset."
        
        # Load the dataset into a DataFrame
        df = pd.read_csv(csv_files[0])

        return df, None
    
    except Exception as e:
        return None, f"An error occurred: {e}"