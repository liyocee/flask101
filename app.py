from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
app.debug = True

GREETINGS = {'default': ['Hello there']}


@app.route('/')
def index():
    return render_template('home.html', message='Hello world')


@app.route('/<person>/')
def greeting(person):
    greetings = GREETINGS.get(person, GREETINGS['default'])
    return render_template('home.html', message='{}, {}'.format('|'.join(greetings), person))


@app.route('/greeting/add/', methods=['POST', 'GET'])
def add_greeting():
    if request.method == 'POST':
        greeting = request.form['greeting']
        person = request.form['person']
        if person in GREETINGS:
            GREETINGS[person].append(greeting)
        else:
            GREETINGS[person] = [greeting]
    return render_template('greeting.html', greetings=GREETINGS)


if __name__ == '__main__':
    app.run()
