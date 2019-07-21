from flask import Flask

# always refer to yourself
app = Flask(__name__)

# ROUTES yay
@app.route('/')
def index():
    return "Howdy Ya'll"

# debug=True -> any time I make changes we want flask ot auto-restart
# host='0.0.0.0' -> listen on all addresses that can get here
app.run(debug=True, port=8000, host='0.0.0.0')
