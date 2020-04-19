from flask import Flask, jsonify
import  dbconnection

app = Flask(__name__)

Laptops = [
    {
        'id': 101,
        'company': 'Acer',
        'processor': 'i7',
        'RAM': '8 GB',
        'Size': '14 inches'
    },
    {
        'id': 202,
        'company': 'Dell',
        'processor': 'i5',
        'RAM': '8 GB',
        'Size': '15 inches'
    },
    {
        'id': 303,
        'company': 'HP',
        'processor': 'i5',
        'RAM': '16 GB',
        'Size': '15.5 inches'
    }
]


@app.route('/')
def hello_world():
    return "Hello world"


@app.route('/v1/getLaptopQuotes')
def getLaptopList():
    laptops = []
    for laptop in Laptops:
        laptops.append(laptop)
    return jsonify(laptops)


@app.route('/v1/saveLaptop', methods=["POST"])
def postLaptop():
    laptopNew = {
        'id': 404,
        'company': 'Asus',
        'processor': 'i9',
        'RAM': '4 GB',
        'Size': '16 inches'
    }
    laptops = []
    for laptop in Laptops:
        laptops.append(laptop)
    return jsonify(laptops)


if __name__ == 'main':
    app.run()
