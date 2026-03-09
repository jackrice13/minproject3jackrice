import requests
import click
from datetime import datetime, timedelta


def download_kev():
    from KEVTrackr.db import get_db
    db = get_db()

    url = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
    response = requests.get(url)
    kev_data = response.json()

    cutoff = datetime.now() - timedelta(days=30)

    new_entries = [
        v for v in kev_data["vulnerabilities"]
        if datetime.strptime(v["dateAdded"], "%Y-%m-%d") >= cutoff
    ]

    inserted = 0
    skipped = 0

    for entry in new_entries:
        vendor = entry["vendorProject"]

        #  Company table check
        existing_company = db.execute(
            "SELECT id FROM company WHERE company_name = ?", (vendor,)
        ).fetchone()

        if existing_company is None:
            db.execute(
                "INSERT INTO company (company_name) VALUES (?)", (vendor,)
            )
            company = db.execute(
                "SELECT id FROM company WHERE company_name = ?", (vendor,)
            ).fetchone()
            print(f"  New company added: {vendor}")
        else:
            company = existing_company

        #  KEV table check
        existing_kev = db.execute(
            "SELECT id FROM kev WHERE cve_id = ?", (entry["cveID"],)
        ).fetchone()

        if existing_kev is None:
            db.execute("""
                INSERT INTO kev (
                    company_id,
                    cve_id,
                    vendor_project,
                    product,
                    vulnerability_name,
                    date_added,
                    short_description,
                    required_action,
                    due_date
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                company['id'],
                entry["cveID"],
                entry["vendorProject"],
                entry.get("product"),
                entry.get("vulnerabilityName"),
                entry.get("dateAdded"),
                entry.get("shortDescription"),
                entry.get("requiredAction"),
                entry.get("dueDate")
            ))
            print(f"  [INSERTED] {entry['cveID']} - {vendor}")
            inserted += 1
        else:
            print(f"  [SKIPPED]  {entry['cveID']} - already exists")
            skipped += 1

    db.commit()

    #  Summary
    print(f"\n Download Complete ")
    print(f"  Inserted : {inserted}")
    print(f"  Skipped  : {skipped}")
    print(f"  Total    : {inserted + skipped}")


@click.command('download-kev')
def download_kev_command():
    """Download latest KEV entries from CISA."""
    download_kev()
    click.echo('KEV data updated.')
