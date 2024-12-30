from flask import Flask, render_template, request, redirect, url_for, flash
from kaggle_connect import kaggle_connect  # Importa la función desde kaggle_connect.py
from pathlib import Path

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Necesario para usar flash

# Ruta para almacenar datasets
UPLOAD_FOLDER = Path('./dataset')
UPLOAD_FOLDER.mkdir(exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_term = request.form.get('search_term')
        if not search_term:
            flash('Por favor, ingrese un término de búsqueda.')
            return redirect(url_for('search'))

        # Buscar datasets usando la función kaggle_connect
        df, error = kaggle_connect(search_term)
        if error:
            flash(error)
            return redirect(url_for('search'))

        # Si no hubo error, mostrar vista previa del dataset
        return render_template('index.html', data_preview=df.head().to_html())

    # Renderizar el formulario si es una solicitud GET
    return render_template('search.html')

if __name__ == '__main__':
    app.run(debug=True)
