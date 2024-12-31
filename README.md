# Dataset Search and Download App

This is a Flask-based web application that allows users to search for datasets on Kaggle and download them directly. The app provides a user-friendly interface to interact with Kaggle's dataset repository, making it easier to find and retrieve datasets.

## Features

- **Search for Datasets**: Enter a search term to find datasets hosted on Kaggle.
- **View Search Results**: See a list of datasets that match your query, along with their titles.
- **Download Datasets**: Download selected datasets as `.zip` files directly from the application.

## Files in the Repository

### Python Scripts

1. **`App.py`**
   - The main Flask application that handles routes and renders templates.
   - Routes:
     - `/`: Home page.
     - `/search`: Search for datasets.
     - `/download/<path:dataset_ref>`: Download the selected dataset.

2. **`kaggle_connect.py`**
   - Handles interaction with the Kaggle API.
   - Functions:
     - `search_datasets(search_term)`: Searches Kaggle for datasets matching the provided term.
     - `download_dataset(dataset_ref)`: Downloads a dataset by its reference.

### HTML Templates

1. **`index.html`**
   - Home page with a welcome message and a link to the search page.

2. **`search.html`**
   - A form to input a search term for finding datasets.

3. **`search_results.html`**
   - Displays the search results and provides download links for each dataset.

## Prerequisites

- Python 3.7+
- Kaggle API credentials (download your `kaggle.json` from Kaggle and place it in `~/.kaggle/` or the project root).

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/dataset-search-download.git
   cd dataset-search-download
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up Kaggle API credentials:
   - Place your `kaggle.json` file in the `~/.kaggle/` directory or in the root of the project.

## Usage

1. Run the Flask application:
   ```bash
   python App.py
   ```

2. Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

3. Use the application to search for datasets, view results, and download datasets.

## Project Structure

```
.
├── App.py                # Main Flask application
├── kaggle_connect.py     # Kaggle API integration
├── templates/            # HTML templates
│   ├── index.html
│   ├── search.html
│   ├── search_results.html
├── dataset/              # Directory for downloaded datasets
└── README.md             # Project documentation
```

## Notes

- Ensure that the Kaggle API is properly authenticated to use this application.
- The downloaded datasets are saved in the `dataset/` directory as `.zip` files.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- [Kaggle API Documentation](https://github.com/Kaggle/kaggle-api)
- [Flask Documentation](https://flask.palletsprojects.com/en/stable/)