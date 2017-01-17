"""
Carpaccio server using Flask.
To start the kata, complete the order() function
"""

from flask import Flask, request, jsonify, abort
from taxes import getTotal as calc_tax
from reductions import reduce_total as calc_reduction
import re

app = Flask(__name__)

#Main function of the kata
@app.route("/order", methods=['POST'])
def order():
    try:
        # order is a dict
        order = request.get_json()
        print(order)

        if len(order['prices']) is not len(order['quantities']):
            raise Exception()

        total = sum([a * b for (a,b) in zip(order['prices'], order['quantities'])])
        post_tax = calc_tax(total, order['country'])
        post_reduction = calc_reduction(post_tax, order['reduction'])

        result = {'total': post_reduction}
        # You should probably comment this line before you register your client
        return jsonify(result)
    except:
        print('ABORT')
        abort(400)

#Server's feedback to your work.
@app.route("/feedback", methods=['POST'])
def feedback():
    feedback = request.get_json()

    print(feedback)
    #TODO HERE YOU RECEIVE WHAT THE SERVER THINKS ABOUT YOUR WORK

    return jsonify(request.get_json())

# Returns 'hello world' on any get request
@app.route("/", methods=['GET'])
@app.route("/<path:path>", methods=['GET'])
def index2(path=''):
    return "hello world"

@app.route("/ping", methods=['POST'])
def ping():
    return "pong"
# Subject of the Kata.

def start_server():
    app.run(host='0.0.0.0',
            port=int("5000"))
