from flask import Flask
from flask import request
# request is a global object available everywhere!
# request has an args property that is a dictionary so we access it with args.get(<key_name>)


# always refer to yourself
app = Flask(__name__)

# ROUTES that render views when requested
@app.route('/')
def query_string_view(name='Mikaela'):
    """
    Views are functions that return HTTP responses. repsonse must be a string
    Using a query string in the URL puts a key in the args dictionary, ex: ../?name="Jimmy"
    """
    name = request.args.get('name', name)
    return "Howdy Ya'll. {} is AwEsOmE!.".format(name)

@app.route('/<name>')
def clean_view(name):
    return "Actually, {} is AwEsOmE!.".format(name)

@app.route('/<int:number>')
def int_input(number):
    """specifiy a type in the url"""
    return "I am {}, and I have always been an integer. Two of me makes {}.".format(number, number*2)
@app.route('/convert/<number>')
def int_maker(number):
    """
    Remember that input is always a string.
    """
    integer = int(number)
    return "My string is {}, but if you change me to an int, you can add one and I become {}.".format(number, integer+1)


# debug=True -> any time I make changes we want flask ot auto-restart
# host='0.0.0.0' -> listen on all addresses that can get here
app.run(debug=True, port=8000, host='0.0.0.0')
