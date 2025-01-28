from flask import Flask ,redirect,url_for

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/home')
def home():
    return 'Hello, HomePage!'

@app.route('/home/test')
def homeTest():
    return redirect(url_for("hello_world"))

@app.route('/<name>')
def user(name):
    return f'hello {name}'

if __name__ == '__main__':
    app.run(debug=True)