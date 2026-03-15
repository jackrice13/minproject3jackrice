from flask import Blueprint, render_template, request, redirect, url_for, flash, g
from .db import get_db
from .auth import login_required   # reuse your existing decorator

bp = Blueprint('companies', __name__, url_prefix='/companies')


@bp.route('/')
@login_required
def index():
    db = get_db()

    # Get every unique vendor name from the KEV catalog, sorted A-Z
    all_vendors = db.execute(
        'SELECT DISTINCT vendor_project FROM kev ORDER BY vendor_project ASC'
    ).fetchall()

    # Get the list of vendors THIS user is already tracking
    tracked = db.execute(
        'SELECT vendor_name FROM tracked_companies WHERE user_id = ?',
        (g.user['id'],)
    ).fetchall()

    # Turn the tracked list into a plain Python set for easy lookup in the template
    # e.g. {'Microsoft', 'Cisco', 'Apache'}
    tracked_set = {row['vendor_name'] for row in tracked}

    return render_template('companies/index.html',
                           all_vendors=all_vendors,
                           tracked_set=tracked_set)


@bp.route('/follow', methods=['POST'])
@login_required
def follow():
    vendor_name = request.form['vendor_name']
    db = get_db()

    try:
        db.execute(
            'INSERT INTO tracked_companies (user_id, vendor_name) VALUES (?, ?)',
            (g.user['id'], vendor_name)
        )
        db.commit()
        flash(f'Now tracking {vendor_name}', 'success')
    except db.IntegrityError:
        # UNIQUE constraint fired — they already follow this company
        flash(f'You are already tracking {vendor_name}', 'warning')

    return redirect(url_for('companies.index'))


@bp.route('/unfollow', methods=['POST'])
@login_required
def unfollow():
    vendor_name = request.form['vendor_name']
    db = get_db()

    db.execute(
        'DELETE FROM tracked_companies WHERE user_id = ? AND vendor_name = ?',
        (g.user['id'], vendor_name)
    )
    db.commit()
    flash(f'Unfollowed {vendor_name}', 'info')

    return redirect(url_for('companies.index'))