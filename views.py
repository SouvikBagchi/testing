from flask import Flask, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

@app.route('/', methods = ['GET','POST'])
def hello_world():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)