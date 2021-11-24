from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Bem vindo ! Ao modelo padrão"

if __name__ == "__name__":
    app.run(host = '0.0.0.0', port = 8080, debug = True)
