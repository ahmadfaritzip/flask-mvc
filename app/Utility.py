#!/usr/bin/python3
# -*- coding: utf-8 -*-
from flask import make_response, jsonify

def toDictionaryArray(data):
    x = []
    for dt in data:
        a = {}
        keys = dt.keys()
        for d in keys:
            a[d] = str(dt[d])
        x.append(a)
    return x

def sendResponse(result):
    resp = make_response(jsonify(result))
    resp.mimetype = 'application/json'
    return resp

def allowed_file(filename, ALLOWED_EXTENSIONS):
  return '.' in filename and \
         filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS