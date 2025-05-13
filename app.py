from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return '''
    <html>
    <head>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <div class="contenedor">
            <h1>¡Hola desde Render2!</h1>
            <img src="/static/spchamy1.png" alt="Imagen centrada">
        </div>
    </body>
    </html>
    '''

import os
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
