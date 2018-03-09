from flask import Flask, render_template, redirect, session

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def home():
    if not session.get('count'):
        session['count'] = 0
    session['count'] += 1
    return render_template('index.html', counter=session['count'])

@app.route('/add2')
def add2():
    session['count'] += 1
    return redirect('/')

@app.route('/reset')
def reset():
    session['count'] = 0
    return redirect('/')

app.run(debug=True)