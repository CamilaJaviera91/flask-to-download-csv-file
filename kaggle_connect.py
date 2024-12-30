from kaggle.api.kaggle_api_extended import KaggleApi
from pathlib import Path

def search_datasets(search_term):
    """Search for datasets on Kaggle by term."""
    try:
        # Initialize the API and authenticate
        api = KaggleApi()
        api.authenticate()

        # Search for datasets
        datasets = api.dataset_list(search=search_term)
        return [{"ref": d.ref, "title": d.title} for d in datasets], None  # Return a list of refs and titles
    except Exception as e:
        return [], f"An error occurred: {e}"  # Return an empty list and the error message

def download_dataset(dataset_ref, download_path='./dataset'):
    """Download the selected dataset from Kaggle."""
    try:
        # Initialize the API and authenticate
        api = KaggleApi()
        api.authenticate()

        # Set download folder
        download_path = Path(download_path)
        download_path.mkdir(parents=True, exist_ok=True)

        # Download and unzip dataset
        api.dataset_download_files(dataset_ref, path=str(download_path), unzip=True)
        return f"Dataset downloaded successfully to {download_path}"
    except Exception as e:
        return f"An error occurred: {e}"
