from flask import Flask, render_template, request, redirect, url_for, send_file, flash
from kaggle_connect import kaggle_connect
from pathlib import Path

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        search_term = request.form.get('search_term')

        if not search_term:
            flash('Please provide a search term.')
            return redirect(url_for('index'))

        # Call kaggle_connect to download the dataset
        csv_file, error = kaggle_connect(search_term)
        if error:
            flash(error)
            return redirect(url_for('index'))

        # Store the file path in the session for download
        file_path = csv_file.resolve()  # Get the absolute path
        return render_template('index.html', download_url=url_for('download_file', file_path=str(file_path)))

    return render_template('index.html')

@app.route('/download', methods=['GET'])
def download_file():
    file_path = request.args.get('file_path')
    if not file_path or not Path(file_path).exists():
        flash('The requested file does not exist.')
        return redirect(url_for('index'))
    
    # Send the file to the user for download
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
