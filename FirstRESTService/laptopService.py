from flask import Flask, session, jsonify, request, render_template, flash, redirect, url_for
import dbconnection
from wtforms import Form, StringField, validators
from flask_session import Session
import random


app = Flask(__name__)
sess = Session(app)

class AddLaptopForm(Form):
    brand_name = StringField('Brand Name')
    processor = StringField('Processor')
    ram = StringField('RAM')
    screen_size = StringField('Screen Size')


@app.route('/', methods = ['GET'])
def hello_world():
    return "Hello world"


@app.route('/getLaptops', methods = ['POST', 'GET'])
def get_laptops():
    print("sessionkey at this getLaptops is : "+str(app.config['SECRET_KEY']))
    db_cursor, conn = dbconnection.get_cursor()
    db_cursor.execute("SELECT * FROM laptops")
    result = db_cursor.fetchall()
    db_cursor.close()
    conn.close()
    laptops = []
    for laptop in result:
        laptops.append(laptop)
        #print(laptop)
    #session['laptop_data'] = laptops
    #return jsonify(laptops)
    return render_template('displayLaptopList.html', data=laptops)


@app.route('/addLaptopForm', methods=['POST', 'GET'])
def add_laptop_forwarding():
    print("sessionkey at this addLaptopform is : "+str(app.config['SECRET_KEY']))
    return render_template('addNewLaptop.html')


@app.route('/addLaptop', methods=['POST', 'GET'])
def add_laptop():
    #print("sessionkey at this addLaptop is : "+str(app.config['SECRET_KEY']))
    print("Inside add laptop")
    try:
        db_cursor, conn = dbconnection.get_cursor()
        
        #print(request.method)

        if request.method == 'POST':
            form = AddLaptopForm(request.form)
            print("inside request method")
            brand_name = form.brand_name.data
            processor = form.processor.data
            ram = form.ram.data
            screen_size = form.screen_size.data

            db_cursor.execute("INSERT INTO laptops (brandname, prcessor, RAM, screen_size) "
                              "VALUES (%s, %s, %s, %s)", (brand_name, processor, ram, screen_size))
            conn.commit()
            print("Success")
            #flash("Your response has been recorded")
            db_cursor.close()
            conn.close()
            print("Connection closed")
            #return redirect(url_for('/'))
            return get_laptops()
            #return render_template('blank.html')
            #return "Successfully added!"

        else:
            print("Not added")
            return render_template('blank.html')
        print("Not added")
        return render_template('blank.html')
        
    except Exception as e:
        # flash("Error in adding new laptop")
        print("Error in adding new laptop")
        return str(e)

@app.route("/sampleJSON",methods=["GET"])
def sampleJSON():
    
    return jsonObj

if __name__ == '__main__':
    #global session
    app.secret_key = str(random.random())#'secret laptop key'
    #app.config['SECRET_KEY'] = app.secret_key
    #print("secret key called : "+app.secret_key)
    #app.config['SESSION_TYPE'] = 'filesystem'
    #app.config.update(SECRET_KEY=str(random.random()))
    #session.init_app(app)
    app.debug = True        

    app.run(host='0.0.0.0', port=8000,threaded=True)

