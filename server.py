from doctest import run_docstring_examples
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def checkerboard():
    return render_template('index.html', x=8, y=8)

@app.route('/<int:y>')
def change_column(y):
    return render_template('index.html', y=y, x=8)

@app.route('/<int:x>/<int:y>')
def changeboth(x,y):
    return render_template('index.html', x=x, y=y) 

if __name__ == '__main__':
    app.run(debug=True)