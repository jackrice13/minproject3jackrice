import click
from flask import Blueprint, render_template, request, g
from KEVTrackr.db import get_db

bp = Blueprint('kev', __name__, url_prefix='/kev')

@bp.route('/')
def index():
    db = get_db()
    filter_tracked = request.args.get('filter') == 'tracked'

    # Only filter if the user is logged in AND they requested it
    if filter_tracked and g.user is not None:
        kevs = db.execute("""
            SELECT k.cve_id, k.vendor_project, k.product, k.vulnerability_name,
                   k.date_added, k.short_description, k.required_action, k.due_date,
                   c.company_name
            FROM kev k
            JOIN company c ON k.company_id = c.id
            WHERE k.vendor_project IN (
                SELECT vendor_name FROM tracked_companies WHERE user_id = ?
            )
            ORDER BY k.date_added DESC
        """, (g.user['id'],)).fetchall()
    else:
        kevs = db.execute("""
            SELECT k.cve_id, k.vendor_project, k.product, k.vulnerability_name,
                   k.date_added, k.short_description, k.required_action, k.due_date,
                   c.company_name
            FROM kev k
            JOIN company c ON k.company_id = c.id
            ORDER BY k.date_added DESC
        """).fetchall()

    return render_template('kev/index.html', kevs=kevs, filter_tracked=filter_tracked)