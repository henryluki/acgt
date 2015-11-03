#coding = utf-8
from flask import Flask, jsonify
app = Flask(__name__)

% if routes:
% for m in routes:
% for r in m:
@app.route('{{ "/" + r["name"]}}', methods=['{{r["method"]}}'])
def {{r["name"]}}():
  data = dict({"success": "success"})
  return jsonify(data)

% end
% end
@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)