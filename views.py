from flask import Flask, url_for, requests

app = Flask(__name__)
db = SQLALchemy(app)

@app.route('/', methods = ['GET','POST'])
def hello_world():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

