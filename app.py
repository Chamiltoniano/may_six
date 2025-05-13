from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return '''
    <h1>¡Hola desde Render!</h1>
    <img src="/static/spchamy1.png" alt="Imagen de prueba" width="400">
    '''

import os
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
