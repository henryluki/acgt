#coding = utf-8
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/get_order_list', methods=['get'])
def get_order_list():
  data = dict({"success": "success"})
  return jsonify(data)

@app.route('/get_order', methods=['get'])
def get_order():
  data = dict({"success": "success"})
  return jsonify(data)

@app.route('/get_article_list', methods=['get'])
def get_article_list():
  data = dict({"success": "success"})
  return jsonify(data)

@app.route('/get_article', methods=['get'])
def get_article():
  data = dict({"success": "success"})
  return jsonify(data)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)