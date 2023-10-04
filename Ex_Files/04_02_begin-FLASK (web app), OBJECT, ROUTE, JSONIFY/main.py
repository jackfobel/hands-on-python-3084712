from flask import Flask

app = Flask(__name__)  # instantiate a web app object

@app.route("/")
def hello():
  return "Hello World!"

app.run(debug=True)