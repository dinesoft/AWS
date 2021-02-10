from flask import (Flask, request, render_template)
import requests

app = Flask(__name__)

IP = "localhost"
PORT = 3000

def build_url(route):
    return F"http://{IP}:{PORT}/{route}"

def build_html_url(route, name):
    route = build_url(route)
    return F"<a href={route} target='_blank'>{name}</a>"
    
@app.route("/")
def hello():
    return F"<h1>BI&Big Data</h1>"\
            F"<p>30h00</p>"\
            F"<form action = 'http://35.180.99.239:3000/index' method = 'post'>"\
            F"<br>{build_html_url('transfert/rds')}"\
            F"</form>"
                
@app.route("/load/s3")
def loadS3():
    return requests.get(url=build_url("/load/s3")).text
    
@app.route("/load/rds")
def loadRDS():
    return requests.get(url=build_url("/load/rds")).text

@app.route("/transfert/rds")
def transfertToRDS():
    return requests.get(url=build_url("/transfert/rds")).text


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3001)
