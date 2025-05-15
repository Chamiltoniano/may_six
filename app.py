from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return '''
    <html>
    <head>
        <title>Home</title>
        <link rel="icon" href="/static/musicaon.ico" type="image/x-icon">
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <nav>
            <div class="nav-links">
                <a href="/">Home</a>
                <a href="/about">About</a>
                <a href="/contact">Contact</a>
            </div>
            <button id="theme-toggle">Toggle Dark Mode</button>
        </nav>
        <div class="contenedor">
            <h1 id="titulo">¡Hola desde Render3!</h1>
            <img src="/static/spchamy1.png" alt="Imagen centrada">
        </div>
        <p id="mensaje"></p>
        <p id="hora" style="margin-top: 10px; font-weight: bold;"></p>
        <script>
        // Automatic dark mode at night
        const hora = new Date().getHours();
        if (hora >= 18 || hora < 6) {
            document.body.classList.add('dark-mode');
        }
        // Update current time every second
        function actualizarHora() {
            const ahora = new Date();
            const texto = ahora.toLocaleTimeString();
            document.getElementById("hora").textContent = "Hora actual: " + texto;
        }
        setInterval(actualizarHora, 1000);
        actualizarHora();
        // Change title text on click
        document.getElementById("titulo").addEventListener("click", function() {
            this.textContent = "¡Gracias por hacer clic!";
        });
        // Random welcome message
        const mensajes = [
            "¡Bienvenido a mi sitio!",
            "¿Sabías que esto está hecho con Flask?",
            "Render rocks 💥",
            "¿Te gusta el atardecer?",
            "Hecho con amor y Python 🐍"
        ];
        const elegido = mensajes[Math.floor(Math.random() * mensajes.length)];
        document.getElementById("mensaje").textContent = elegido;
        // Dark/Light mode toggle button handler
        document.getElementById("theme-toggle").addEventListener("click", function() {
            document.body.classList.toggle('dark-mode');
        });
        </script>
    </body>
    </html>
    '''

@app.route("/about")
def about():
    return '''
    <html>
    <head>
        <title>About</title>
        <link rel="icon" href="/static/musicaon.ico" type="image/x-icon">
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <nav>
            <div class="nav-links">
                <a href="/">Home</a>
                <a href="/about">About</a>
                <a href="/contact">Contact</a>
            </div>
            <button id="theme-toggle">Toggle Dark Mode</button>
        </nav>
        <div class="contenedor">
            <h1>About Page</h1>
            <p>This is the about page.</p>
        </div>
        <script>
        // Set dark mode class if it is night time
        const hora = new Date().getHours();
        if (hora >= 18 || hora < 6) {
            document.body.classList.add('dark-mode');
        }
        // Toggle dark/light mode on button click
        document.getElementById("theme-toggle").addEventListener("click", function() {
            document.body.classList.toggle('dark-mode');
        });
        </script>
    </body>
    </html>
    '''

@app.route("/contact")
def contact():
    return '''
    <html>
    <head>
        <title>Contact</title>
        <link rel="icon" href="/static/musicaon.ico" type="image/x-icon">
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <nav>
            <div class="nav-links">
                <a href="/">Home</a>
                <a href="/about">About</a>
                <a href="/contact">Contact</a>
            </div>
            <button id="theme-toggle">Toggle Dark Mode</button>
        </nav>
        <div class="contenedor">
            <h1>Contact Page</h1>
            <p>This is the contact page.</p>
        </div>
        <script>
        // Set dark mode class by default at night
        const hora = new Date().getHours();
        if (hora >= 18 || hora < 6) {
            document.body.classList.add('dark-mode');
        }
        // Toggle dark/light mode on click
        document.getElementById("theme-toggle").addEventListener("click", function() {
            document.body.classList.toggle('dark-mode');
        });
        </script>
    </body>
    </html>
    '''

import os
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
