from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "try calling http://localhost:[port]/name"

@app.route('/<string:name>/')
def hello(name):
    return "Hello " + name
	
if __name__ == '__main__':
	app.run(debug=True)
    
