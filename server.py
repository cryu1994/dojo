from flask import Flask, render_template, redirect, request, session, flash
# import re
# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
@app.route('/')

def index():

    return render_template('index.html')
@app.route('/process', methods=['POST'])
def process():

    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']

    if len(request.form['name']) < 1:
        flash("Name Cannot be empty!")
    if len(request.form['comment']) < 1:
        flash('Please leave a comment')
    if len(request.form['comment']) > 120:
        flash("Comment must be less than 120 characters!")
    return redirect('/result')

@app.route('/result')
def result():

    return render_template('result.html', name=session['name'], location=session['location'], language=session['language'], comment=session['comment'])

app.run(debug=True)
