from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from KEVTrackr.auth import login_required
from KEVTrackr.db import get_db

bp = Blueprint('kev', __name__)

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
                   SET first_name = ?, last_name = ?, location = ?,
                   updated = CURRENT_TIMESTAMP
                   WHERE user_id = ?""",
                (first_name, last_name, location, user_id)
            )
            db.commit()
            flash('Profile updated successfully.')
            return redirect(url_for('auth.profile'))

        flash(error)

    # GET - fetch current profile data to pre-fill the form
    profile = db.execute(
        "SELECT * FROM profile WHERE user_id = ?", (user_id,)
    ).fetchone()

    return render_template('auth/profile.html', profile=profile)