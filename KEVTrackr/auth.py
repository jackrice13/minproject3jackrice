import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from KEVTrackr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

#Register Section of BP
@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        location = request.form['location']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                #create user/pwd
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?, ?)",
                    (username, generate_password_hash(password)),
                    )
                    # Get the new user's ID that just created
                user=db.execute(
                    "SELECT id FROM user WHERE username = ?", (username,)
                ).fetchone()

                # Insert the profile using that user ID
                db.execute(
                     "INSERT INTO profile (user_id, first_name, last_name, location) VALUES (?, ?, ?, ?)",
                     (user['id'], first_name, last_name, location),
                )
                db.commit()
            except db.IntegrityError:
                error = f"User {username} is already registered."
            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template('auth/register.html')

#Login Section of the BP
@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('kev.index'))

        flash(error)
    return render_template('auth/login.html')
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('kev.index'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view

@bp.route('/profile', methods=('GET', 'POST'))
def profile():
    db = get_db()
    user_id = g.user['id']

    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        location = request.form['location']
        error = None

        if not first_name:
            error = 'First name is required.'

        if error is None:
            db.execute(
                """UPDATE profile
                   SET first_name = ?,
                       last_name  = ?,
                       location   = ?,
                       updated    = CURRENT_TIMESTAMP
                   WHERE user_id = ?""",
                (first_name, last_name, location, user_id)
            )
            db.commit()
            flash('Profile updated successfully.')
            return redirect(url_for('auth.profile'))

        flash(error)

    profile = db.execute(
    "SELECT * FROM profile WHERE user_id = ?", (user_id,)
    ).fetchone()

    return render_template('auth/profile.html', profile=profile)
