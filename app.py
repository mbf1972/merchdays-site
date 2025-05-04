from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Clé d'activation fixe (provenant du fichier keys.txt)
FIXED_KEY = "4NUB-3C11-HAI0-EX1Z"

@app.route('/')
def index():
    """Page d'accueil du site"""
    return render_template('index.html')

@app.route('/activation', methods=['GET'])
def activation():
    """Page d'activation de la licence"""
    return render_template('activation.html')

@app.route('/get-key', methods=['GET'])
def get_key():
    """API pour récupérer la clé d'activation fixe"""
    return jsonify({'key': FIXED_KEY})

@app.route('/verify-key', methods=['POST'])
def verify_key():
    """API pour vérifier si une clé d'activation est valide"""
    data = request.get_json()
    key = data.get('key')

    if key == FIXED_KEY:
        return jsonify({'valid': True, 'message': 'Clé valide'})

    return jsonify({'valid': False, 'message': 'Clé invalide'})

if __name__ == '__main__':
    # Lancer le serveur de développement
    app.run(debug=True)