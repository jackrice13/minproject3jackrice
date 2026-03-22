### INF601 - Advanced Programming in Python
### Jack Rice
### Mini Project 3
 
 
# Project Title
 
### KEVTrackr-Mini Project 3
 
## Description
 
## About KEVTrackr

KEVTrackr is a Flask-based web application designed to help small and medium-sized business (SMB) IT teams monitor and respond to actively exploited vulnerabilities. It pulls data directly from the [CISA Known Exploited Vulnerabilities (KEV) Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — a curated list of CVEs that have been confirmed as exploited in the wild — and presents it in a searchable, sortable dashboard. Users can create an account, follow the specific software vendors relevant to their environment, and filter the KEV table to surface only the vulnerabilities that matter to their organization. Rather than sifting through thousands of CVEs from broad vulnerability databases, KEVTrackr narrows the focus to confirmed, real-world threats, giving lean IT teams a practical starting point for prioritizing patching and remediation efforts. 
## Getting Started
 
### Dependencies
 
Please install the pip requirements

```
pip install -r requirements.txt
```

### Executing program
 
* How to run the program
* Step-by-step bullets


Install all required Python packages by running:
```
pip install -r requirements.txt
```
Initialize the database
Create the SQLite database and build all required tables by running
```
flask --app KEVTrackr init-db
```
Download KEV data
Pull the latest Known Exploited Vulnerabilities from the CISA feed and prepopulates the database by running, currently gets the last 30 days of data:

```
flask --app KEVTrackr download-kev
```
Start the application
Launch the Flask development server by running:
```
flask --app KEVTrackr run
```
## Help
 
Any advise for common problems or issues.
```
command to run if program contains helper info
```
 
## Authors
 
Contributors names and contact info
 
ex. Dominique Pizzie  
ex. [@DomPizzie](https://twitter.com/dompizzie)
 
## Version History

* 0.1
    * Initial Release
 

## Acknowledgments
 

KEVTrackr was built using the following open-source libraries and data sources:

### Data Source
- [CISA Known Exploited Vulnerabilities (KEV) Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — The authoritative source of actively exploited vulnerability data maintained by the Cybersecurity and Infrastructure Security Agency.

### Backend
- [Flask](https://flask.palletsprojects.com/) — Lightweight Python web framework used to handle routing, templating, and application logic.
- [SQLite](https://www.sqlite.org/) — Embedded relational database used for storing KEV data, user accounts, and company tracking information.

### Frontend
- [Bootstrap 5](https://getbootstrap.com/) — CSS framework used for responsive layout, components, and dark-themed styling.
- [Bootstrap Table](https://bootstrap-table.com/) — jQuery-based table plugin used to power the sortable, searchable KEV data table.
- [jQuery](https://jquery.com/) — JavaScript library used as a dependency for Bootstrap Table.
- [Jinja2](https://jinja.palletsprojects.com/) — Python templating engine (bundled with Flask) used to render dynamic HTML pages.


### Related Claude AI Conversations

[Claude AI](https://claude.ai/share/b7703fdf-3a3b-4e4b-9fee-f1f5b649dd42)

[Claude AI](https://claude.ai/share/42b2b2ff-a145-466c-828f-49b76a3cc4d3)

[Claude AI](https://claude.ai/share/155d721b-0567-42f6-9fc6-4dc0a7873890)