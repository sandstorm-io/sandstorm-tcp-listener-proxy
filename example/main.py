#!/usr/bin/env python3

import base64
import json
import os
import socket
import sys
import subprocess

from flask import Flask
from flask import request
from flask import render_template
from flask import make_response

import json

app = Flask(__name__)
application = app

def write_state(newState):
    with open("/var/state", "wb") as f:
        json.dump(newState, f)

def read_state():
    if not os.path.exists("/var/state"):
        return None
    with open("/var/state", "rb") as f:
        return json.load(f)

ECHO_PROCESS = None
PROXY_PROCESS = None
def start_proxy(token, localPort=41415, externalPort=41415):
    print 'starting echo server'
    ECHO_PROCESS = subprocess.Popen(['python', '/opt/app/echo.py'], stdout=sys.stdout, stderr=sys.stderr)
    args = ['/opt/app/bin/sandstorm-tcp-listener-proxy', token, str(localPort), str(externalPort)]
    print 'starting proxy server: ' + ' '.join(args)
    PROXY_PROCESS = subprocess.Popen(args, stdout=sys.stdout, stderr=sys.stderr)

@app.route('/', methods=["GET"])
def index():
    content = read_state()
    return render_template("index.html",
            content=content)

@app.route('/caps', methods=["POST"])
def save_cap():
    if request.method == "POST":
        newState = request.form.to_dict()
        write_state(newState)
        start_proxy(newState['token'], externalPort=newState['port'])
    content = read_state()
    return render_template("index.html",
            content=content)

if __name__ == "__main__":
    app.run('0.0.0.0', 8000, debug=True)
