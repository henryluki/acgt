# -*- coding: utf-8 -*-
# generate by acgt
from flask import Flask, jsonify, request
app = Flask(__name__)

% if routes:
% for m in routes:
% for r in m["detail"]:
@app.route('{{ "/" + m["module"]+ "/" + r["name"]}}', methods=['{{r["method"]}}'])
def {{r["name"]}}():
% if any(r["arguments"]):
% for a in r["arguments"]:
  {{a}} = request.args.get('{{a}}')
% end
% end
  data = dict({"success": "success"})
  return jsonify(data)

% end
% end
@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)