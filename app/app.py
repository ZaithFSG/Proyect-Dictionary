from flask import Flask, render_template,request, jsonify
from deep_translator import GoogleTranslator
import requests

app = Flask(__name__, template_folder='templates')

@app.route('/definir', methods=['GET'])
def definir_palabra():
    palabra_es = request.args.get('palabra', '').strip().lower()
    
    if not palabra_es:
        return jsonify({"error": "Debes ingresar una palabra"}), 400
    
    try:
        # 1. Español → Inglés
        palabra_en = GoogleTranslator(source='es', target='en').translate(palabra_es)
        
        # 2. Consultar API inglesa
        api_url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{palabra_en}"
        respuesta = requests.get(api_url, timeout=5).json()
        definicion_en = respuesta[0]['meanings'][0]['definitions'][0]['definition']
        
        # 3. Inglés → Español
        definicion_es = GoogleTranslator(source='en', target='es').translate(definicion_en)
        
        return jsonify({
            "palabra": palabra_es,
            "definicion": definicion_es
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)