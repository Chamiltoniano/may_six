from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return '''
    <html>
    <head>
    <title>Acerca de</title>
    <link rel="icon" href="/static/musicaon.ico" type="image/x-icon">
    <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
    <div class="contenedor">
    <h1>¡Hola desde Render3!</h1>
    <img src="/static/spchamy1.png" alt="Imagen centrada">
    </div>

    <script>
    const hora = new Date().getHours();
    if (hora >= 18 || hora < 6) {
    document.body.style.backgroundColor = "#1c1c1c";
    document.body.style.color = "#fff";
    }
    </script>
    </body>

    </html>

    '''

    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
