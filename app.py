from flask import Flask, render_template, request, redirect, url_for, flash, send_file
from urllib.parse import quote, unquote
from kaggle_connect import search_datasets, download_dataset

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_term = request.form.get('search_term')
        if not search_term:
            flash('Please enter a search term.')
            return redirect(url_for('search'))

        # Search datasets
        datasets, error = search_datasets(search_term)
        if error:
            flash(error)
            return redirect(url_for('search'))

        # Render the search results
        return render_template('search_results.html', datasets=datasets, search_term=search_term)

    return render_template('search.html')

@app.route('/download/<path:dataset_ref>')
def download(dataset_ref):
    # Decode the dataset reference
    dataset_ref = unquote(dataset_ref)

    # Download the selected dataset
    message = download_dataset(dataset_ref)
    flash(message)
    return send_file(f'./dataset/{message}.zip', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
