from flask import Flask ,redirect,url_for , render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/home')
def home():
    return render_template('test.html')

@app.route('/<name>')
def user(name):
    return f'hello {name}'

if __name__ == '__main__':
    app.run(debug=True)