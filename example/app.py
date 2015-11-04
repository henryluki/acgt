# -*- coding: utf-8 -*-
# generate by acgt
from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/order/get_order_list', methods=['get'])
def get_order_list():
  id = request.args.get('id')
  data = dict({"success": "success"})
  return jsonify(data)

@app.route('/order/get_order', methods=['post'])
def get_order():
  id = request.form.get('id')
  data = dict({"success": "success"})
  return jsonify(data)

@app.route('/article/get_article_list', methods=['get'])
def get_article_list():
  id = request.args.get('id')
  data = dict({"success": "success"})
  return jsonify(data)

@app.route('/article/get_article', methods=['get'])
def get_article():
  data = dict({"success": "success"})
  return jsonify(data)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)