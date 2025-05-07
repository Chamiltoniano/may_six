from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "¡I am in render now?!"

if __name__ == "__main__":
    app.run()
