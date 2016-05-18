from flask import Flask
from flask import render_template

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    return render_template('home.html', message='Hello world')


@app.route('/<person>/<greeting>')
def greeting(person, greeting):
    return render_template('greeting.html', message='{}, {}'.format(greeting, person))


if __name__ == '__main__':
    app.run()
