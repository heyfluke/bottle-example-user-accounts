# Copyright (c) 2012, John M. Gabriele
# License: MIT (see LICENSE.txt for details)

from bottle import route, run, template, request, response,\
    redirect, install
from bottle_sqlite import SQLitePlugin

import time, random, string

install(SQLitePlugin(dbfile='db/site.db'))


# ----------------------------------------------------------------------
# If the user is logged in, returns the username.
def is_logged_in(db):
    cookie_session_id = request.get_cookie('session_id')
    if not cookie_session_id:
        return False

    c = db.execute('select user_id from sessions where session_id = ?',
                   (cookie_session_id,))
    row = c.fetchone()
    if row:
        c = db.execute('select username from users where id = ?', (row[0],))
        row = c.fetchone()
        return row[0]
    else:
        return False


# ----------------------------------------------------------------------
@route('/')
def main(db):
    username = is_logged_in(db)
    if not username:
        return template('main', username=False)
    else:
        return template('main', username=username)


@route('/about')
def about(db):
    username = is_logged_in(db)
    if not username:
        return template('about', username=False)
    else:
        return template('about', username=username)

@route('/login')
def login(db):
    username = is_logged_in(db)
    if username:
        return template('oops',
                        username=username,
                        message="T'would seem you're already logged in...")
    else:
        return template('login', username=False)


@route('/login', method='POST')
def do_login(db):
    submitted_username = request.forms.get('username')
    # TODO: validate username
    submitted_password = request.forms.get('password')
    # TODO: validate password

    c = db.execute('select id from users where username = ? and password = ?',
                   (submitted_username, submitted_password))
    row = c.fetchone()
    if not row:
        return template('oops',
                        username=False,
                        message="Either incorrect username or password.")
    user_id = row[0]
    # Ok, now log the user in.
    time_now = str(int(time.time()))
    new_session_id = time_now + '-' + \
        ''.join([random.choice(string.lowercase) for i in range(6)])
    db.execute('insert into sessions (session_id, user_id) values (?, ?)',
               (new_session_id, user_id))
    response.set_cookie('session_id', new_session_id)
    redirect('/')


@route('/create-an-account')
def create_an_account(db):
    username = is_logged_in(db)
    if username:
        return template('oops',
                        username=username,
                        message="It may be that you already have an account, given that" +
                                " you're currently logged in.")
    else:
        return template('create-an-account', username=False)


@route('/create-an-account', method='POST')
def do_create_an_account(db):
    submitted_username = request.forms.get('username')
    submitted_password = request.forms.get('password')
    submitted_email = request.forms.get('email')
    # TODO: validate those
    c = db.execute('insert into users (username, email, password) values (?, ?, ?)',
                   (submitted_username, submitted_email, submitted_password))
    return template('info',
                    username=False,
                    message="Account created. Please log in.")


@route('/logout')
def do_logout(db):
    session_id = request.get_cookie('session_id')
    db.execute('delete from sessions where session_id = ?',
               (session_id,))
    response.delete_cookie('session_id')
    redirect('/')

# ----------------------------------------------------------------------
run(host='localhost', port=8080, debug=True, reloader=True)
