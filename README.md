### INF601 - Advanced Programming in Python
### Jack Rice
### Mini Project 3
 
 
# Project Title
 
Simple overview of use/purpose.
 
## Description
 
An in-depth paragraph about your project and overview of use.
 
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
* 
* 0.1
    * Initial Release
 

## Acknowledgments
 
Inspiration, code snippets, etc.



Related Claude AI Conversations

[Claude AI](https://claude.ai/share/b7703fdf-3a3b-4e4b-9fee-f1f5b649dd42)

[Claude AI](https://claude.ai/share/42b2b2ff-a145-466c-828f-49b76a3cc4d3)

[Claude AI](https://claude.ai/share/155d721b-0567-42f6-9fc6-4dc0a7873890)