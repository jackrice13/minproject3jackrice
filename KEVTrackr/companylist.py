from flask import Blueprint, render_template
from KEVTrackr.db import get_db

bp = Blueprint('companylist', __name__, url_prefix='/companylist')

@bp.route('/')
def companylist():
    db = get_db()
    kevs = db.execute("""
        SELECT c.id, c.company_name
        FROM company c
        ORDER BY c.id ASC 
    """).fetchall()
    return render_template('kev/company.html', company=kevs)