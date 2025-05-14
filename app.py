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
            <h1 id="titulo">¡Hola desde Render3!</h1>
            <img src="/static/spchamy1.png" alt="Imagen centrada">
        </div>
        <p id="mensaje"></p>

        <script>
        const hora = new Date().getHours();
        if (hora >= 18 || hora < 6) {
            document.body.style.backgroundColor = "#1c1c1c";
            document.body.style.color = "#fff";
        }
        function actualizarHora() {
        const ahora = new Date();
        const texto = ahora.toLocaleTimeString();
        document.getElementById("hora").textContent = "Hora actual: " + texto;
        }
        setInterval(actualizarHora, 1000);
        actualizarHora();

        document.getElementById("titulo").addEventListener("click", function() {
        this.textContent = "¡Gracias por hacer clic!";
        });


        const mensajes = [
          "¡Bienvenido a mi sitio!",
          "¿Sabías que esto está hecho con Flask?",
          "Render rocks 💥",
          "¿Te gusta el atardecer?",
          "Hecho con amor y Python 🐍"
        ];

        const elegido = mensajes[Math.floor(Math.random() * mensajes.length)];
        document.getElementById("mensaje").textContent = elegido;
        </script>
    </body>
    </html>
    '''

# 👇 Esto debe estar FUERA del bloque de la función `home()`
import os
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
