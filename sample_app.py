from flask import Flask
app = Flask(__name__)  #single moduule

@app.route('/sample')   #decoratore @app
def running():
    return "Flask is on!"