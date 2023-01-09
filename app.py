from flask import Flask, jsonify, request

app = Flask(__name__)

from products import products

@app.route('/ping')
def ping():
    return jsonify({"message":"it's working!"})

@app.route('/products', methods=['GET'])
def getProucts():
    return jsonify({"products":products} )

@app.route('/products/<string:name>')
def getProduct(name):
    productFound = [product for product in products if product['name'] == name]
    if (len(productFound) > 0):
        return jsonify({"message":"the product is found", "products": productFound})
    else:
        return jsonify({"message":"the product has not been found", "products": []})

@app.route('/products',methods=['POST'])
def addProduct():
    product = {
        "name" : request.json['name'],
        "prce" : request.json['prce'],
        "quantity" : request.json['name']
    }
    products.append(product)
    return jsonify({"message": "product has beed added succesfully", "product":product})

@app.route('/products/<string:name>', methods = ['PUT'])
def editProducts(name):
    productFound = [product for product in products if product['name'] ==  name]
    product = {
        "name" : request.json['name'],
        "prce" : request.json['prce'],
        "quantity" : request.json['name']
    }
    if(len(productFound) > 0):
        productFound[0]['name'] = product['name']
        productFound[0]['price'] = product['prce']
        productFound[0]['quantity'] = product['quantity']
        return jsonify({'respnse' : "product has been updated", "product": productFound[0]})
    else:
        return jsonify({'respone': "no product hase been found"})

@app.route('/products/<string:name>', methods = ['DELETE'])
def deleteProduct(name):
    productFound = [ product for product in products if product['name'] == name]
    if (len(productFound) > 0 ):
        products.remove(productFound[0])
        return jsonify({"response" : "product has been deleted successfully"})
    else:
        return jsonify({"response": "product has not been found"})

if __name__ == "__main__":
    app.run(debug=True, port = 4000)