from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
   return "<h1>Hello, world!</h1>"

# flask routes
@app.route('/anas')
def anas():
   return "<h2>Hello, Anas!</h2>"

@app.route('/<string:name>')
def hello(name):
   name = name.capitalize()
   return f"Hello, {name}!"

if __name__ == "__main__":
    app.run(debug=True)