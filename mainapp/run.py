from flask import (Flask, request, render_template)
import requests
app = Flask(__name__)
IP = "localhost"
PORT = 3000
def build_url(route):
    return F"http://{IP}:{PORT}/{route}"


def build_button(route):
    route = build_url(route)
    return F"<button onclick={route}>Ajouter</button>"
    
@app.route("/")
def hello():
    return F"<head>"\
   	F"<title>Projet AWS</title>"\
	F"<meta charset='utf-8' />"\
	F"<meta name='viewport' content='width=device-width, initial-scale=1, user-scalable=no' />"\
	F"<link rel='stylesheet' href='assets/css/style.css' />"\
        F"<link href='https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css' rel='stylesheet' integrity='sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1' crossorigin='anonymous'>"\
        F"</head>"\
        F"<body>"\
        F"<div class='title'>"\
        F"<h1>Retrouvez toutes les matières enseignées en 4IABD</h1>"\
        F"</div>"\
        F"<br><br>"\
        F"<div class='container'>"\
        F"<div class='row'>"\
        F"<div class='col-sm' style='border: 0.3mm solid black'>"\
        F"<h1>BI&Big Data</h1>"\
        F"<p>30h00</p>"\
        F"<form action = 'http://35.180.99.239:3000/index' method = 'post'>"\
        F"<br>{build_button('transfert/rds')}"\
        F"</form>"\
        F"</div>"\
        F"<div class='col-sm' style='border:  0.3mm solid black'>"\
        F"<h1>Communication Professionelle</h1>"\
        F"<p>15H00</p>"\
        F"<form action = 'http://35.180.99.239:3000/index' method = 'post'>"\
        F"<br>{build_button('transfert/rds')}"\
        F"</form>"\
        F"</div>"\
	F"<div class='col-sm' style='border:  0.3mm solid black'>"\
        F"<h1>Deep Learning</h1>"\
        F"<p>15H00</p>"\
        F"<form action = 'http://35.180.99.239:3000/index' method = 'post'>"\
        F"<br>{build_button('transfert/rds')}"\
        F"</form>"\
        F"</div>"\
        F"<div class='col-sm' style='border:  0.3mm solid black'>"\
        F"<h1>AWS</h1>"\
        F"<p>30h00</p>"\
        F"<form action = 'http://35.180.99.239:3000/index' method = 'post'>"\
	F"<br>{build_button('transfert/rds')}"\
        F"</form>"\
        F"</div>"\
        F"</div>"\
        F"<div class='row'>"\
        F"<div class='col-sm' style='border: 0.3mm solid black'>"\
        F"<h1>Management</h1>"\
        F"<p>15h00</p>"\
        F"<form action = 'http://35.180.99.239:3000/index' method = 'post'>"\
        F"<br>{build_button('transfert/rds')}"\
        F"</form>"\
        F"</div>"\
        F"<div class='col-sm' style='border:  0.3mm solid black'>"\
        F"<h1>Mathématiques</h1>"\
        F"<p>15H00</p>"\
        F"<form action = 'http://35.180.99.239:3000/index' method = 'post'>"\
        F"<br>{build_button('transfert/rds')}"\
        F"</form>"\
        F"</div>"\
	F"<div class='col-sm' style='border:  0.3mm solid black'>"\
        F"<h1>Scala</h1>"\
        F"<p>15H00</p>"\
        F"<form action = 'http://35.180.99.239:3000/index' method = 'post'>"\
        F"<br>{build_button('transfert/rds')}"\
        F"</form>"\
        F"</div>"\
        F"<div class='col-sm' style='border:  0.3mm solid black'>"\
        F"<h1>Spark</h1>"\
        F"<p>30h00</p>"\
        F"<form action = 'http://35.180.99.239:3000/index' method = 'post'>"\
	F"<br>{build_button('transfert/rds')}"\
        F"</form>"\
        F"</div>"\
        F"</div>"\
        F"<div class='row'>"\
        F"<div class='col-sm' style='border: 0.3mm solid black'>"\
        F"<h1>Anglais</h1>"\
        F"<p>27H00</p>"\
        F"<form action = 'http://35.180.99.239:3000/index' method = 'post'>"\
        F"<br>{build_button('transfert/rds')}"\
        F"</form>"\
        F"</div>"\
        F"<div class='col-sm' style='border:  0.3mm solid black'>"\
        F"<h1>Cours electif</h1>"\
        F"<p>15H00</p>"\
        F"<form action = 'http://35.180.99.239:3000/index' method = 'post'>"\
        F"<br>{build_button('transfert/rds')}"\
        F"</form>"\
        F"</div>"\
	F"<div class='col-sm' style='border:  0.3mm solid black'>"\
        F"<h1>E-learning</h1>"\
        F"<p>20H00</p>"\
        F"<form action = 'http://35.180.99.239:3000/index' method = 'post'>"\
        F"<br>{build_button('transfert/rds')}"\
        F"</form>"\
        F"</div>"\
        F"<div class='col-sm' style='border:  0.3mm solid black'>"\
        F"<h1>Open</h1>"\
        F"<p>OOH00</p>"\
        F"<form action = 'http://35.180.99.239:3000/index' method = 'post'>"\
	F"<br>{build_button('transfert/rds')}"\
        F"</form>"\
        F"</div>"\
        F"</div>"\
        F"</body>"\


@app.route("/transfert/rds")
def transfert():
    return requests.get(url=build_url("/transfert/rds")).text

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3001)
