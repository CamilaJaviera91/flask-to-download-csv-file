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

def download_dataset(dataset_ref):
    """Download a dataset by its reference."""
    try:
        api = KaggleApi()
        api.authenticate()

        # Destination folder
        base_folder = Path('./dataset')
        base_folder.mkdir(exist_ok=True, parents=True)  

        # Download and unzip
        api.dataset_download_files(dataset_ref, path=str(base_folder), unzip=False)
        s = dataset_ref.split("/")
        return s[1]
    except Exception as e:
        return f"Failed to download dataset: {e}"
