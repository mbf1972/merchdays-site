from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/activation', methods=['GET', 'POST'])
def activation():
    if request.method == 'POST':
        # Récupérer la clé d'activation depuis la requête
        key = request.form.get('activation_key')

        # Enregistrer la clé dans le fichier keys.txt
        if key:
            with open('keys.txt', 'a') as f:
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                f.write(f"{key} - généré le {timestamp}\n")

            return jsonify({'success': True, 'message': 'Clé enregistrée avec succès'})

        return jsonify({'success': False, 'message': 'Clé invalide'})

    return render_template('activation.html')

@app.route('/save-key', methods=['POST'])
def save_key():
    # Récupérer la clé d'activation depuis la requête JSON
    data = request.get_json()
    key = data.get('key')

    # Enregistrer la clé dans le fichier keys.txt
    if key:
        with open('keys.txt', 'a') as f:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            f.write(f"{key} - généré le {timestamp}\n")

        return jsonify({'success': True, 'message': 'Clé enregistrée avec succès'})

    return jsonify({'success': False, 'message': 'Clé invalide'})

if __name__ == '__main__':
    app.run(debug=True)