from flask import Flask, request

app = Flask(__name__)

@app.route("/calc", methods = ["GET"])
def calc():
    args = request.args
    v1 = args.get('v1') # クエリパラメータから v1 を取得する．
    v2 = args.get('v2')# クエリパラメータから v2 を取得する．
    op = args.get('op') # クエリパラメータから op を取得する．
    if not v1 or not v2 or not op: # s1, s2, op のどれかが与えられなかった場合
        return "Error: Invalid parameters", 400

    try:
        s1 = int(v1)
        s2 = int(v2)
    except ValueError:
        return "Error: Invalid parameters", 400

    i1 = s1
    i2 = s2

    if op == "add":
        result = i1 + i2
    elif op == "sub":
        result = i1 - i2
    elif op == "mul":
        result = i1 * i2
    elif op == "div":
        if i2 == 0:
            return "Error: Division by zero", 400
        result = i1 / i2
    else:
        return "Error: Invalid operator", 400
    return f'{{"operation":"{i1} {op} {i2}","result":{result}}}', 200

app.run(port = 5001, debug = True, host = "0.0.0.0")
