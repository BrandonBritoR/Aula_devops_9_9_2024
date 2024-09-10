from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Olá Mundo, acabo por favor"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    #rnd_vNyfCRxO05vuYQFycDJQPQjorHnG