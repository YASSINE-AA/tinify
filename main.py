
from data import data
from flask import Flask, render_template, request, redirect
import shortening_algorithm
import config
import webbrowser
import sqlite3
application = Flask(__name__)


@application.route('/', methods=['POST'])
def get_url():
    global processed_url
    global finished_url
    global prefix
    processed_url = request.form['url_input']

    if "https://" in processed_url:
        processed_url = processed_url.replace("https://", "")
        prefix = "https://"
    elif "http://" in processed_url:
        processed_url = processed_url.replace("http://", "")
        prefix = "http://"
    else:
        prefix = "http://"

    if config.PORT:
        if "." in processed_url:
            finished_url = f'{config.HOST}' + \
                '/' + str(shortening_algorithm.start(processed_url)[0])
        else:
            finished_url = "the link you've entered is invalid."
    else:
        if "." in processed_url:
            finished_url = f'{config.HOST}' + \
                '/' + str(shortening_algorithm.start(processed_url)[0])
        else:
            finished_url = "the link you've entered is invalid."
    redirect_dict = {
        "url": finished_url
    }
    return render_template("redirect.html", result=redirect_dict)


@application.route('/<new_links>')
def new_stuff(new_links):
    conn = sqlite3.connect("urls.db")
    cur = conn.cursor()

    cur.execute("SELECT * from urltable")
    redirect_link = ''

    data_db = cur.fetchall()

    for row in data_db:
        # checks if link exists
        if str(new_links) in row:
            redirect_link = f"{prefix}{str(row[0])}"
    cur.close()
    return redirect(redirect_link, code=302)


@application.route('/')
def hello():
    return render_template('main.html', result=data)


@application.route('/app', methods=['GET', 'POST'])
def app():
    return render_template('index.html', result=data)
