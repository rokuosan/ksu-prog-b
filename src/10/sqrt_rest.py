from flask import Flask, Response
import math


app = Flask(__name__)

@app.route('/sqrt/<num>')
def sqrt(num):
    if int(num) < 0:
        return "", 400
    return str(math.sqrt(int(num)))

app.run(port = 5001, debug = True, host = "0.0.0.0")
