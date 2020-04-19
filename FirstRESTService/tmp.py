# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 15:07:05 2020

@author: sacin
"""

from flask import Flask,request,jsonify 
#from flask_cors import CORS, cross_origin  
import datetime
# Flask constructor takes the name of  
# current module (__name__) as argument. 

app = Flask(__name__)
#cors = CORS(app)
#app.config['CORS_HEADERS'] = 'Content-Type'
  
# The route() function of the Flask class is a decorator,  
# which tells the application which URL should call  
# the associated function. 
@app.route('/encry',methods = ['POST']) 
#@cross_origin()
# ‘/’ URL is bound with hello_world() function. 
def hello_world():
    val=request.form['enc']
    msg=dict()
    msg['msg']='encrypted text:'+str(val)
    return jsonify(msg)

@app.route('/decry',methods = ['POST'])
#@cross_origin()
def respn():
    val=request.form['enc']
    msg=dict()
    msg['msg']='decrypted text:'+str(val)
    return jsonify(msg)

@app.route('/hello',methods = ['GET'])
#@cross_origin()
def hello():
    return "hello the time is "+datetime.datetime.now().strftime("%H:%M:%S")

# main driver function 
if __name__ == '__main__': 
  
    # run() method of Flask class runs the application  
    # on the local development server. 
    app.run(host="0.0.0.0",port=9800,threaded=True)