import os
import requests
from collections import namedtuple

from flask import (
    Flask,
    render_template,
    url_for,
    request,
    session,
    redirect,
)

import sqlite3

DB_FILE = 'register.db'

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact Us')


@app.route('/work_with_us')
def work_with_us():
    return render_template('work_with_us.html', title='Work With Us')


@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')


@app.route('/register_new_form', methods=['GET', 'POST'])
def register_new_form():

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    telephone = request.form['telephone']
    email = request.form['email']
    tpe = request.form['tpe']

    url = "https://api.sendinblue.com/v3/smtp/email"

    payload = "{\"sender\":{\"email\":\"bogdan.vlad.@gmail.com\",\"name\":\"Bogdan Vlad\"},\"to\":[{\"email\":\"bogdan.vlad@tuware.com\",\"name\":\"Bogdan Vlad\"}],\"replyTo\":{\"email\":\"bogdan.vlad@tuware.com\"},\"subject\":\"Hello\",\"htmlContent\":\"%s %s\"}" % (first_name, last_name)

    headers = {
        'accept': "application/json",
        'content-type': "application/json",
        'api-key': "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"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    statement = 'INSERT INTO test (' \
                'first_name,' \
                'last_name,' \
                'telephone,' \
                'email, tpe) VALUES (?, ?, ?, ?, ?)'
    cursor.execute(statement, (first_name, last_name, telephone, email, tpe))
    conn.commit()
    conn.close()
    return render_template('index.html', response=response)


if __name__ == "__main__":
    app.run(debug=True)
